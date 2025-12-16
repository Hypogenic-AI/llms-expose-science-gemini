
import os
import argparse
import json
import pandas as pd
from datasets import load_from_disk
from openai import OpenAI
from tenacity import retry, wait_exponential, stop_after_attempt
from tqdm import tqdm
import random

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(5))
def get_topics_from_text(text_chunk):
    """
    Uses OpenAI's GPT model to extract clinical topics from a text chunk.
    """
    if not isinstance(text_chunk, str) or not text_chunk.strip():
        return []

    # Truncate text to avoid exceeding token limits
    max_chunk_size = 8000 # Approx characters for 2048 tokens
    truncated_text = text_chunk[:max_chunk_size]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106", # Fast and good at JSON mode
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a medical research analyst. Your task is to extract key clinical topics from the provided text. "
                        "Focus on medical conditions, symptoms, treatments, procedures, and medications. "
                        "Normalize the topics (e.g., 'heart attack' and 'myocardial infarction' should both be 'Myocardial Infarction'). "
                        "Provide your output as a JSON object with a single key 'topics' which contains a list of unique topic strings."
                    ),
                },
                {"role": "user", "content": truncated_text},
            ],
            temperature=0.0,
        )
        result_text = response.choices[0].message.content
        topics = json.loads(result_text).get("topics", [])
        # Ensure all topics are strings and clean them up
        return [str(topic).strip() for topic in topics if isinstance(topic, str) and topic.strip()]
    except (json.JSONDecodeError, AttributeError, Exception) as e:
        print(f"Could not parse topics from LLM response: {e}")
        return []

def process_corpus(file_path, file_type, text_column, num_samples):
    """
    Loads a corpus, samples it, and extracts topics from the text.
    """
    print(f"Loading corpus from {file_path}...")
    if file_type == 'jsonl':
        df = pd.read_json(file_path, lines=True)
    elif file_type == 'hf':
        dataset = load_from_disk(file_path)
        df = dataset['train'].to_pandas()
    else:
        raise ValueError("Unsupported file type. Use 'jsonl' or 'hf'.")

    if num_samples > 0 and num_samples < len(df):
        df = df.sample(n=num_samples, random_state=42)
    
    print(f"Processing {len(df)} documents...")
    all_topics = []
    for text in tqdm(df[text_column], desc="Extracting topics"):
        topics = get_topics_from_text(text)
        all_topics.extend(topics)
        
    return all_topics

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract topics from a corpus using an LLM.")
    parser.add_argument("--input_path", type=str, required=True, help="Path to the input file or directory.")
    parser.add_argument("--file_type", type=str, required=True, choices=['jsonl', 'hf'], help="Type of the input file.")
    parser.add_argument("--text_column", type=str, required=True, help="Name of the column containing the text.")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save the output JSON file.")
    parser.add_argument("--num_samples", type=int, default=500, help="Number of samples to process from the corpus.")
    
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    topics = process_corpus(args.input_path, args.file_type, args.text_column, args.num_samples)
    
    if topics:
        topic_counts = pd.Series(topics).value_counts().to_dict()
        
        # Convert all keys to string to be JSON compliant
        topic_counts = {str(k): v for k, v in topic_counts.items()}

        with open(args.output_path, 'w') as f:
            json.dump(topic_counts, f, indent=2)
        print(f"Successfully extracted and saved {len(topic_counts)} unique topics to {args.output_path}")
    else:
        print("No topics were extracted.")
