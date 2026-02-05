# LLM-Based Research Classification Automation

This project automates the extraction, analysis, and structured reporting of academic research publications using Large Language Models (LLMs).

>[!note]
> This repository demonstrates the technical approach and workflow. It uses public data and is intended for educational and demonstration purposes only.

## Overview
The application:
- The system uses a **self-hosted Mistral LLM** served locally via Ollama.
- Scrapes publications from Google Scholar profiles
- Analyzes titles and abstracts using an LLM
- Classifies research against national development priorities
- Outputs structured Excel reports for institutional use

## Technologies
- Python
- Streamlit
- Google Scholar (scholarly)
- LLMs (Mistral via Ollama)
- Pandas
- OpenPyXL

## Use Case
Designed to reduce manual effort in research reporting and classification workflows by automating repetitive analysis tasks while maintaining consistency and traceability.

## Limitations
- Analysis is based solely on publication titles and abstracts and does not replace full peer review.
- LLM outputs are probabilistic and should be validated for critical decision-making.
- Google Scholar scraping may be subject to rate limits or changes in availability.

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
