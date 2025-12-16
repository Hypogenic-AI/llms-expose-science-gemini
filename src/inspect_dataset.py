
from datasets import load_from_disk

def inspect_dataset(dataset_path):
    dataset = load_from_disk(dataset_path)
    print(dataset['train'].column_names)

if __name__ == "__main__":
    inspect_dataset("datasets/Asclepius-Synthetic-Clinical-Notes")
