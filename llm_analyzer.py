import requests
import json

class LLMAnalyzer:
    def __init__(self, model="mistral", endpoint="http://localhost:11434/api/generate"):
        self.model = model
        self.endpoint = endpoint

    def analyze_paper(self, title, abstract):
        prompt = f"""
Analyze the following academic paper and assess alignment with national development priorities.

Title: {title}
Abstract: {abstract}

Return ONLY valid JSON in the following format:
{{
  "objectives": "...",
  "findings": "...",
  "alignment": {{
    "economic_development": "Y/N",
    "human_development": "Y/N",
    "social_development": "Y/N",
    "environmental_development": "Y/N",
    "institutional_development": "Y/N"
  }},
  "national_outcomes": {{
    "sustainable_economic_growth": "Y/N",
    "financial_sustainability": "Y/N",
    "future_ready_workforce": "Y/N",
    "cohesive_society": "Y/N",
    "high_quality_life": "Y/N",
    "environmental_sustainability": "Y/N",
    "distinguished_government_institutions": "Y/N"
  }}
}}
"""

        response = requests.post(
            self.endpoint,
            json={"model": self.model, "prompt": prompt, "stream": False},
            timeout=60
        )
        response.raise_for_status()
        return json.loads(response.json()["response"])
