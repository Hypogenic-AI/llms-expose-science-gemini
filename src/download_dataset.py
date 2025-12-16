
import argparse
from datasets import load_dataset

def download_dataset(dataset_name, save_path):
    """
    Downloads a dataset from Hugging Face and saves it to disk.
    """
    try:
        print(f"Downloading dataset: {dataset_name}")
        dataset = load_dataset(dataset_name)
        print(f"Saving dataset to: {save_path}")
        dataset.save_to_disk(save_path)
        print("Dataset downloaded and saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download a dataset from Hugging Face.")
    parser.add_argument("--dataset_name", type=str, required=True, help="Name of the dataset on Hugging Face Hub.")
    parser.add_argument("--save_path", type=str, required=True, help="Path to save the dataset.")
    
    args = parser.parse_args()
    
    download_dataset(args.dataset_name, args.save_path)
