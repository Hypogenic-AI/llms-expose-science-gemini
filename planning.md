## Research Question
Can Large Language Models (LLMs) systematically identify and expose under-researched scientific and societal problems by analyzing discrepancies between topics in scientific literature and those found in real-world text sources?

## Background and Motivation
The current paradigm of "AI for Science" often accelerates research in existing, well-funded areas rather than identifying new, impactful problems. Many real-world issues, particularly those affecting marginalized groups or lacking profitability, remain under-researched. This project aims to develop and test a methodology that uses LLMs as "gap detectors" to bridge this divide, making science more accountable to societal needs by highlighting where real-world problems are not being met with scientific attention.

## Hypothesis Decomposition
The central hypothesis can be broken down into the following testable components:
1.  **H1 (Topic Extraction):** An LLM can effectively extract and normalize granular, meaningful topics from unstructured text from both scientific and real-world sources.
2.  **H2 (Corpus Representation):** The distribution of these extracted topics accurately represents the focus areas of each corpus (scientific vs. real-world).
3.  **H3 (Gap Identification):** A quantitative comparison of topic distributions between the corpora can reveal specific topics that are significantly more prevalent in real-world sources than in scientific literature.
4.  **H4 (Qualitative Insight):** The identified "gap" topics are non-obvious and represent meaningful areas of under-researched problems.

## Proposed Methodology

### Approach
My approach is to construct two distinct text corpora: one representing mainstream scientific research and another representing real-world problems. I will then use an LLM to perform a comparative topic analysis to identify discrepancies. The workflow is as follows:

1.  **Corpus Construction:** Assemble two corpora.
    *   **Corpus A (Science):** A collection of scientific paper abstracts. Since one was not provided, I will construct one from a publicly available dataset of arXiv papers, focusing on relevant fields like AI, and health.
    *   **Corpus B (Real-World):** A combination of the provided `Asclepius-Synthetic-Clinical-Notes` and `ASRS-ChatGPT` (aviation safety reports) datasets.
2.  **LLM-based Topic Extraction:** Design a prompt for a powerful LLM (e.g., GPT-4.1) to read a document and output a list of key topics or themes. This approach is favored over traditional methods like LDA for its ability to capture semantic nuance.
3.  **Topic Normalization via Clustering:** Since the LLM will generate textually different but semantically similar topics (e.g., "GDM screening" vs. "gestational diabetes screening"), I will use a sentence-transformer model to embed all extracted topic strings into vectors. Then, I will use a clustering algorithm (e.g., Agglomerative Clustering) to group these vectors, effectively normalizing the topics into semantic clusters.
4.  **Quantitative Analysis:** For each topic cluster, calculate its frequency within Corpus A and Corpus B. A "gap score" will be computed to quantify the discrepancy (e.g., `log2((freq_real_world + 1) / (freq_science + 1))`).
5.  **Qualitative Reporting:** The topics with the highest gap scores will be fed back into an LLM to generate a qualitative summary explaining the potential research gap.

### Experimental Steps
1.  **Environment Setup & Data Acquisition:**
    *   Set up the `uv` virtual environment and install dependencies (`pandas`, `datasets`, `transformers`, `torch`, `scikit-learn`, `openai`, `anthropic`).
    *   Load the two provided datasets.
    *   Download and preprocess the `ccdv/arxiv-summarization` dataset from Hugging Face to create the "Science" corpus. I will filter for relevant categories (e.g., `cs.AI`, `cs.LG`, `q-bio.QM`).
2.  **Topic Extraction:**
    *   Develop and refine a robust prompt for topic extraction.
    *   Write a script to iterate through samples from both corpora, call the LLM API (with caching to manage costs), and store the extracted raw topics.
3.  **Topic Clustering:**
    *   Load all raw topics.
    *   Use a pre-trained `sentence-transformers` model to generate embeddings for each topic.
    *   Apply a clustering algorithm to the embeddings and assign each topic to a semantic cluster.
4.  **Analysis and Gap Identification:**
    *   Calculate frequencies of each cluster in each corpus.
    *   Compute the gap score for each cluster.
    *   Rank clusters by gap score to identify the top under-researched topics.
5.  **Baseline Comparison:**
    *   Run the provided `contextualized-topic-models` on the same corpora.
    *   Qualitatively compare the topics and gaps identified by the baseline with the LLM-based approach.

### Baselines
*   **Primary Baseline:** Contextualized Topic Models (CTM), using the provided `code/contextualized-topic-models` repository. This will show whether the sophisticated semantic understanding of an LLM provides more insightful gaps than a state-of-the-art traditional topic model.
*   **Secondary Baseline:** A simple keyword/n-gram frequency comparison to establish a performance floor.

### Evaluation Metrics
*   **Quantitative:** The primary quantitative output will be the ranked list of "gap scores". I will also measure topic coherence scores for the baseline model.
*   **Qualitative:** The primary evaluation will be a qualitative analysis of the top 5-10 identified gaps. I will assess whether they are:
    *   **Meaningful:** Do they represent real, understandable problems?
    *   **Non-obvious:** Do they uncover something not immediately apparent from a surface-level reading?
    *   **Actionable:** Could they plausibly form the basis of a new research direction?
*   **Rediscovery:** I will check if the method rediscovers known gaps mentioned in the project's background description (e.g., gestational diabetes, endometriosis).

### Statistical Analysis Plan
The core of the analysis is not traditional hypothesis testing with p-values but rather a descriptive and exploratory analysis. The main statistical tool will be the ranking of gap scores. Visualizations like bar charts will be used to compare topic frequencies between the corpora.

## Expected Outcomes
*   **Success:** The system identifies a set of credible, non-obvious research gaps. For example, it might highlight specific patient complaints in clinical notes that do not appear in the academic literature, or frequent failure modes in aviation reports that lack corresponding research in AI safety.
*   **Refutation:** The system produces only obvious or nonsensical gaps (e.g., "patients" is a topic in clinical notes but not in AI papers), or the identified topics are too generic to be meaningful. This would suggest the methodology is flawed or the LLM is not capable of the required nuance.

## Timeline and Milestones
*   **Phase 1 (Planning):** 0.5 hours (Complete)
*   **Phase 2 (Environment & Data Setup):** 1 hour
*   **Phase 3 (Implementation):** 2.5 hours (Includes data loaders, LLM API integration, clustering logic)
*   **Phase 4 (Experimentation):** 2 hours (Running topic extraction and analysis)
*   **Phase 5 (Analysis):** 1.5 hours (Interpreting results, comparing to baseline)
*   **Phase 6 (Documentation):** 1 hour (Writing `REPORT.md` and `README.md`)
*   **Buffer:** 1.5 hours
*   **Total Estimated Time:** 9 hours

## Potential Challenges
*   **API Costs/Latency:** LLM API calls can be expensive and slow. **Mitigation:** Start with a small sample of the data to debug the pipeline and estimate costs. Implement robust caching for API calls.
*   **Noisy Topics:** The LLM may produce noisy or overly generic topics. **Mitigation:** Iterative prompt engineering. The topic clustering step is also designed to merge noisy variations.
*   **Corpus Mismatch:** The "science" and "real-world" corpora may be so different that comparison is meaningless. **Mitigation:** Careful selection of the arXiv categories for the science corpus to ensure some thematic overlap.
*   **No "Science" Dataset Provided:** A corpus of scientific literature was not included in the resources. **Mitigation:** I will construct one by downloading and filtering a public dataset of arXiv abstracts, as detailed in the methodology.

## Success Criteria
The research will be considered successful if the final `REPORT.md` presents a list of at least 3-5 plausible and non-obvious research gaps, supported by both quantitative discrepancy scores and qualitative explanations, which are demonstrably derived from the experimental methodology.
