## Resources Catalog

### Summary
This document catalogs all resources gathered for the research project, including papers, datasets, and code repositories.

### Papers
Total papers downloaded: 2

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Can LLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation | Weicheng Ma, Alice J. d'Agostino, Arman Cohan, Mark Gerstein | 2023 | papers/2507.02694_Can_LLMs_Identify_Critical_Limitations.pdf | Investigates LLMs' ability to find limitations in scientific papers. |
| A large language model for detection of social drivers of health from clinical text | Yanbo Xu, Bhavik Suri, et al. | 2023 | papers/2305.14214_LLM_for_detection_of_social_drivers_of_health.pdf | Shows how LLMs can extract social health drivers from clinical notes. |

See papers/README.md for detailed descriptions.

### Datasets
Total datasets identified: 2

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| Asclepius-Synthetic-Clinical-Notes | HuggingFace | 1.36 GB | Text Generation | datasets/Asclepius-Synthetic-Clinical-Notes/ | Synthetic clinical notes. |
| ASRS-ChatGPT | HuggingFace | 25.5 MB | Text Classification | datasets/ASRS-ChatGPT/ | Aviation safety incident reports. |

See datasets/README.md for detailed descriptions and download instructions.

### Code Repositories
Total repositories identified: 1

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| contextualized-topic-models | https://github.com/MilaNLProc/contextualized-topic-models | Topic modeling | code/contextualized-topic-models/ | Python package for contextualized topic modeling. |

See code/README.md for detailed descriptions.

### Resource Gathering Notes

#### Search Strategy
I used a combination of Google Scholar, the arXiv preprint server, and the Hugging Face platform to find relevant resources. I focused my search on papers and datasets related to the use of LLMs for identifying research gaps, analyzing clinical notes, and incident reports.

#### Selection Criteria
I selected papers that were highly relevant to the research hypothesis and that were published in reputable venues. I chose datasets that were publicly available, well-documented, and relevant to the research questions. For code, I looked for well-maintained repositories with clear documentation.

#### Challenges Encountered
- Some papers were behind paywalls, making them difficult to access.
- Direct download links for some papers were not available or were incorrect.
- The `web_fetch` tool was not always reliable for extracting information from web pages.

#### Gaps and Workarounds
- I was unable to download the paper "Utilizing large language models for identifying future research opportunities in environmental science". I will proceed with the papers I have.
- To overcome the download issues, I relied on finding papers on arXiv whenever possible, as it provides reliable access to PDFs.

### Recommendations for Experiment Design

Based on the gathered resources, I recommend the following for the experiment design:

1. **Primary dataset(s)**: Start with the `ASRS-ChatGPT` dataset, as it is smaller and will be faster to process. Then, move to the `Asclepius-Synthetic-Clinical-Notes` dataset for a more in-depth analysis.
2. **Baseline methods**: Use the `contextualized-topic-models` library to establish a baseline for topic modeling. Compare the results with the analysis performed by general-purpose LLMs like GPT-3.5/4.
3. **Evaluation metrics**: Develop a framework for evaluating the "interestingness" and "novelty" of the identified research gaps. This could involve a combination of automated metrics (e.g., topic coherence) and human evaluation.
4. **Code to adapt/reuse**: The `contextualized-topic-models` library can be directly used for the topic modeling part of the experiment.
