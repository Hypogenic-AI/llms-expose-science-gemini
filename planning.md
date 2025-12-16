## Research Question
Can Large Language Models (LLMs) systematically identify and expose important scientific and societal problems that are under-researched or ignored, by analyzing discrepancies between well-funded, benchmarked topics and real-world needs?

## Background and Motivation
AI for science has excelled at accelerating research in existing, well-defined paradigms. However, there is a risk that it reinforces existing biases in funding and focus, neglecting "messy" real-world problems that are not easily benchmarked. This research aims to develop and test a method that uses LLMs as "gap detectors" to make science more answerable to societal needs by highlighting areas where pain is high, but academic attention is low.

## Hypothesis Decomposition
The core hypothesis can be broken down into the following testable components:
1.  **Corpus Divergence:** There is a measurable divergence in topics discussed in formal scientific literature versus those discussed in "real-world" texts (e.g., incident reports, clinical notes).
2.  **LLM as Topic Extractor:** An LLM can effectively extract, normalize, and quantify the frequency of topics from both scientific and real-world text corpora.
3.  **Discrepancy as an Indicator:** A high ratio of a topic's frequency in a real-world corpus compared to a scientific corpus is a strong indicator of a potentially under-researched area.
4.  **Superiority over Baselines:** An LLM-based approach to topic extraction will identify more nuanced and meaningful gaps than traditional statistical methods like topic modeling.

## Proposed Methodology

### Approach
I will conduct a comparative analysis of topic frequencies across two distinct domains: aviation safety and clinical health. For each domain, I will create two corpora: one representing scientific research (academic paper abstracts) and one representing real-world issues (incident reports or clinical notes).

I will employ a dual-pronged approach for analysis:
1.  **Baseline Analysis:** Use traditional, non-LLM topic modeling (`contextualized-topic-models`) to establish a baseline of statistically derived topics.
2.  **LLM-based Analysis:** Use a state-of-the-art LLM (e.g., GPT-4.1, Claude Sonnet 4.5) to perform a more semantically aware topic extraction and normalization.

The primary output will be a "Gap Score" for each topic, highlighting those with high real-world prevalence but low scientific focus.

### Experimental Steps

**Phase 1: Environment and Data Setup**
1.  **Install Dependencies:** Install necessary Python libraries (`pandas`, `requests`, `openai`, `matplotlib`, `scikit-learn`, `contextualized-topic-models`) using `uv add`.
2.  **Prepare Datasets:** Load the pre-gathered datasets: `ASRS-ChatGPT` for aviation and `Asclepius-Synthetic-Clinical-Notes` for clinical data.

**Phase 2: Experiment 1 - Aviation Safety Domain**
1.  **Scientific Corpus Creation:** Fetch ~500-1000 recent academic paper abstracts related to "aviation safety" from the arXiv API.
2.  **Real-World Corpus:** Load the `ASRS-ChatGPT` dataset.
3.  **Baseline Topic Modeling:** Apply the `contextualized-topic-models` library to both corpora to extract topics and their frequencies.
4.  **LLM Topic Extraction:** Process both corpora in chunks with an LLM. The prompt will instruct the model to identify and normalize key topics related to aviation safety incidents.
5.  **Gap Score Calculation:** For both the baseline and LLM approaches, calculate a Gap Score for each topic: `Gap Score = (Relative Frequency in ASRS data) / (Relative Frequency in arXiv data)`.
6.  **Analysis:** Qualitatively analyze the top 10-15 topics with the highest Gap Scores from the LLM approach. Compare them to the baseline results to assess whether the LLM provides more insightful findings.

**Phase 3: Experiment 2 - Clinical Health Domain**
1.  **Scientific Corpus Creation:** Fetch ~500-1000 recent abstracts from arXiv related to a broad set of common medical conditions.
2.  **Real-World Corpus:** Load a sample from the `Asclepius-Synthetic-Clinical-Notes` dataset.
3.  **Repeat Analysis:** Repeat steps 3-6 from the aviation experiment, adapting the LLM prompt for a clinical context (e.g., extracting conditions, symptoms, patient complaints).

### Baselines
The primary baseline will be the `contextualized-topic-models` library. This will allow for a direct comparison between a traditional, statistical topic modeling approach and the proposed semantic, LLM-based extraction method. The baseline helps test the hypothesis that LLMs offer a more powerful way to identify nuanced gaps.

### Evaluation Metrics
-   **Quantitative:** The primary metric will be the **Gap Score**, a ratio calculated for each topic. A table of top-ranked topics will be the main quantitative output.
-   **Qualitative:** The success of the experiment will be judged by a qualitative, manual analysis of the top-ranked "gap" topics. The evaluation criteria will be:
    -   **Plausibility:** Does the identified gap seem like a real-world issue that might be overlooked?
    -   **Actionability:** Does the finding suggest a clear direction for new research?
    -   **Novelty:** Is the finding non-obvious and genuinely insightful?

### Statistical Analysis Plan
This research is primarily exploratory and qualitative. The main analysis will involve ranking topics by their Gap Score. Formal statistical significance testing is not the primary goal, but rather the generation of plausible, high-potential research gaps for human review.

## Expected Outcomes
-   **Supporting the Hypothesis:** The experiment would support the hypothesis if the LLM-based analysis produces a ranked list of topics where the top items are plausibly under-researched. For example, finding that "physician burnout" or "patient dissatisfaction with wait times" has a much higher prevalence in clinical notes than in the academic literature would be a successful outcome.
-   **Refuting the Hypothesis:** The hypothesis would be refuted if the identified gaps are nonsensical, already well-researched, or if the traditional topic modeling baseline produces results of equal or higher quality.

## Timeline and Milestones
-   **Environment & Data Setup:** 1 hour
-   **Experiment 1 (Aviation):** 2-3 hours
-   **Experiment 2 (Clinical):** 2-3 hours
-   **Analysis & Documentation:** 2 hours
-   **Total Estimated Time:** 7-9 hours

## Potential Challenges
1.  **API Reliability and Cost:** The use of external LLM and arXiv APIs introduces dependencies. API calls can fail or be slow. I will implement robust error handling (e.g., retries with exponential backoff). The cost of LLM API calls will be monitored.
2.  **Prompt Engineering:** The quality of the LLM-based topic extraction is highly dependent on the prompt. I may need to iterate on the prompt design to get meaningful, well-normalized topics.
3.  **Corpus Bias:** The scientific corpora from arXiv will be biased towards computer science and physics. For the medical domain, this is a notable limitation. The "real-world" corpora are also not perfect (one is synthetic, the other is self-reported). These limitations will be acknowledged.
4.  **Scalability:** Processing large datasets in chunks with an LLM can be time-consuming. I will start with smaller samples to validate the pipeline before scaling up.

## Success Criteria
The research will be considered successful if it produces a list of at least 5-10 plausible, non-obvious, and potentially actionable research gaps for either the aviation or clinical domain, which are demonstrably more insightful than those produced by the traditional baseline method.