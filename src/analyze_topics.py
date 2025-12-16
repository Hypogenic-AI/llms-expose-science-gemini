import json
import pandas as pd
import argparse
import numpy as np

def analyze_topic_gaps(scientific_topics_path, real_world_topics_path, output_json_path, output_md_path):
    """
    Analyzes the frequency gap between two topic lists.
    """
    with open(scientific_topics_path, 'r') as f:
        scientific_topics = json.load(f)
        
    with open(real_world_topics_path, 'r') as f:
        real_world_topics = json.load(f)

    # Convert keys to lowercase for consistent grouping
    scientific_topics_lower = {k.lower(): v for k, v in scientific_topics.items()}
    real_world_topics_lower = {k.lower(): v for k, v in real_world_topics.items()}

    # Convert to pandas Series, grouping by the new lowercase keys
    scientific_df = pd.Series(scientific_topics_lower).groupby(level=0).sum().astype(int)
    scientific_df.name = "scientific_count"
    
    real_world_df = pd.Series(real_world_topics_lower).groupby(level=0).sum().astype(int)
    real_world_df.name = "real_world_count"

    # Calculate total number of topics (not unique topics)
    total_scientific_topics = scientific_df.sum()
    total_real_world_topics = real_world_df.sum()
    
    # Create a unified dataframe
    df = pd.DataFrame({'scientific_count': scientific_df, 'real_world_count': real_world_df}).fillna(0)

    # Calculate relative frequencies
    df['scientific_freq'] = df['scientific_count'] / total_scientific_topics
    df['real_world_freq'] = df['real_world_count'] / total_real_world_topics
    
    # Add a small epsilon to the denominator to avoid division by zero
    epsilon = 1e-9
    df['gap_score'] = df['real_world_freq'] / (df['scientific_freq'] + epsilon)
    
    # Filter for topics that appear in the real-world corpus
    df = df[df['real_world_count'] > 0].copy()
    
    # Sort by gap score
    df = df.sort_values(by='gap_score', ascending=False)
    
    # Reset index to make topic a column
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'topic'}, inplace=True)
    
    # Capitalize topics for better readability in the final output
    df['topic'] = df['topic'].str.title()
    
    print("Top 20 topics with the highest gap score:")
    print(df.head(20))

    # Save results
    df.to_json(output_json_path, orient='records', lines=True)
    print(f"Full analysis saved to {output_json_path}")
    
    # Save top 50 to markdown
    df.head(50).to_markdown(output_md_path, index=False)
    print(f"Top 50 results saved to {output_md_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze topic gaps between two corpora.")
    parser.add_argument("--scientific_topics", type=str, required=True, help="Path to the scientific topics JSON file.")
    parser.add_argument("--real_world_topics", type=str, required=True, help="Path to the real-world topics JSON file.")
    parser.add_argument("--output_json", type=str, default="results/gap_analysis.jsonl", help="Path to save the output JSON.")
    parser.add_argument("--output_md", type=str, default="results/gap_analysis.md", help="Path to save the output markdown file.")

    args = parser.parse_args()
    
    analyze_topic_gaps(args.scientific_topics, args.real_world_topics, args.output_json, args.output_md)