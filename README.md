
# Can LLMs Expose What Science Refuses to See?

This project is a research experiment designed to test the hypothesis that Large Language Models (LLMs) can systematically identify under-researched scientific topics by analyzing discrepancies between scientific literature and "real-world" text data.

## Key Findings

The experiment was conducted in the clinical health domain, comparing academic papers from arXiv with synthetic clinical notes. The key findings strongly support the research hypothesis:

-   **Process-over-Pathology:** The analysis revealed a significant "gap" where topics related to the **process of healthcare** ("MRI", "Biopsy", "Follow-up Care") were highly frequent in clinical notes but almost entirely absent from the scientific abstracts.
-   **Common vs. Novel:** Common symptoms and treatments (e.g., "Abdominal Pain", "Antibiotics") also showed a high gap score, suggesting academic research prioritizes novel diseases and treatments over the management of common, everyday conditions.
-   **LLMs as Gap Detectors:** The LLM-powered pipeline proved effective at extracting, normalizing, and comparing topics at scale, successfully generating a plausible and actionable list of potential research gaps.

The full research report can be found in `REPORT.md`.

## How to Reproduce

1.  **Setup Environment:**
    -   Create a Python 3.10+ virtual environment.
    -   Install `uv` (`pip install uv`).
    -   Run `uv pip install -r requirements.txt` to install all dependencies.

2.  **Set API Key:**
    -   Export your OpenAI API key as an environment variable:
        ```bash
        export OPENAI_API_KEY="your-key-here"
        ```

3.  **Run the Pipeline:**
    The pipeline consists of four main steps. Note that steps 2 and 3 involve significant waiting time due to API calls.

    -   **Step 1: Fetch Scientific Corpus (arXiv)**
        ```bash
        python src/fetch_arxiv.py --query '("clinical note" OR "electronic health record" OR "patient chart")' --max_results 500 --output_file results/arxiv_clinical.jsonl
        ```

    -   **Step 2: Download Real-World Corpus (Hugging Face)**
        ```bash
        python src/download_dataset.py --dataset_name "starmpcc/Asclepius-Synthetic-Clinical-Notes" --save_path "datasets/Asclepius-Synthetic-Clinical-Notes"
        ```

    -   **Step 3: Extract Topics from Both Corpora**
        ```bash
        # Scientific Corpus
        python src/extract_topics.py --input_path results/arxiv_clinical.jsonl --file_type jsonl --text_column abstract --output_path results/topics_scientific.json --num_samples 500

        # Real-World Corpus
        python src/extract_topics.py --input_path datasets/Asclepius-Synthetic-Clinical-Notes --file_type hf --text_column note --output_path results/topics_real_world.json --num_samples 500
        ```

    -   **Step 4: Analyze Topic Gaps**
        ```bash
        python src/analyze_topics.py --scientific_topics results/topics_scientific.json --real_world_topics results/topics_real_world.json
        ```

4.  **View Results:**
    -   The final analysis is saved in `results/gap_analysis.md` and `results/gap_analysis.jsonl`.

## File Structure
-   `src/`: Contains all Python scripts.
-   `datasets/`: Stores downloaded datasets.
-   `results/`: Contains all intermediate and final outputs.
-   `REPORT.md`: Detailed research report.
-   `planning.md`: The initial research plan.
-   `pyproject.toml`: Project dependency definition.
-   `requirements.txt`: A freeze of the dependencies.
