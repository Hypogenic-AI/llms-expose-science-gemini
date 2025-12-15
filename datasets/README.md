# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT
committed to git due to size. Follow the download instructions below.

## Dataset 1: Asclepius-Synthetic-Clinical-Notes

### Overview
- **Source**: [https://huggingface.co/datasets/starmpcc/Asclepius-Synthetic-Clinical-Notes](https://huggingface.co/datasets/starmpcc/Asclepius-Synthetic-Clinical-Notes)
- **Size**: 1.36 GB
- **Format**: HuggingFace Dataset
- **Task**: Text Generation, Question Answering
- **Splits**: train
- **License**: Not specified

### Download Instructions

**Using HuggingFace (recommended):**
```python
from datasets import load_dataset
dataset = load_dataset("starmpcc/Asclepius-Synthetic-Clinical-Notes")
dataset.save_to_disk("datasets/Asclepius-Synthetic-Clinical-Notes")
```

### Loading the Dataset

Once downloaded, load with:
```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/Asclepius-Synthetic-Clinical-Notes")
```

## Dataset 2: ASRS-ChatGPT

### Overview
- **Source**: [https://huggingface.co/datasets/archanatikayatray/ASRS-ChatGPT](https://huggingface.co/datasets/archanatikayatray/ASRS-ChatGPT)
- **Size**: 25.5 MB
- **Format**: HuggingFace Dataset
- **Task**: Text Classification, Text Generation
- **Splits**: train
- **License**: Not specified

### Download Instructions

**Using HuggingFace (recommended):**
```python
from datasets import load_dataset
dataset = load_dataset("archanatikayatray/ASRS-ChatGPT")
dataset.save_to_disk("datasets/ASRS-ChatGPT")
```

### Loading the Dataset

Once downloaded, load with:
```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/ASRS-ChatGPT")
```
