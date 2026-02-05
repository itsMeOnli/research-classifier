import scholarly
import time
import random
import re

class ScholarScraper:
    def __init__(self, delay_range=(1, 3)):
        self.delay_range = delay_range

    def extract_author_id(self, url):
        match = re.search(r"user=([^&]+)", url)
        return match.group(1) if match else None

    def extract_publications(self, profile_url, start_year):
        author_id = self.extract_author_id(profile_url)
        if not author_id:
            raise ValueError("Invalid Google Scholar URL")

        author = scholarly.scholarly.fill(
            scholarly.scholarly.search_author_id(author_id)
        )

        publications = []
        for pub in author.get("publications", []):
            filled = scholarly.scholarly.fill(pub)
            year = int(filled["bib"].get("pub_year", 0))

            if year >= start_year:
                publications.append({
                    "title": filled["bib"].get("title", ""),
                    "year": year,
                    "authors": filled["bib"].get("author", ""),
                    "abstract": filled["bib"].get("abstract", ""),
                    "url": filled.get("pub_url", ""),
                    "citations": filled.get("num_citations", 0),
                })

            time.sleep(random.uniform(*self.delay_range))

        return publications
