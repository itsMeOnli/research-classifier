import streamlit as st
import pandas as pd
import openpyxl
import io
from datetime import datetime

from scholar_scraper import ScholarScraper
from llm_analyzer import LLMAnalyzer
from excel_manager import ExcelManager

st.set_page_config(page_title="Research Profile Analyzer", layout="wide")
st.title("LLM-Based Research Profile Analyzer")

profile_url = st.text_input("Google Scholar Profile URL")
start_year = st.selectbox("Start Year", [2024, 2023, 2022, 2021, 2020])

if st.button("Analyze Publications"):
    scraper = ScholarScraper()
    analyzer = LLMAnalyzer()

    pubs = scraper.extract_publications(profile_url, start_year)

    for p in pubs:
        p["analysis"] = analyzer.analyze_paper(p["title"], p["abstract"])

    st.session_state.data = pubs

if "data" in st.session_state:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)

    if st.button("Export to Excel"):
        wb = openpyxl.Workbook()
        ws = wb.active
        manager = ExcelManager()

        row = 4
        for p in st.session_state.data:
            manager.fill_row(ws, row, p, p["analysis"])
            row += 1

        buffer = io.BytesIO()
        wb.save(buffer)
        st.download_button(
            "Download Excel",
            buffer.getvalue(),
            f"research_output_{datetime.now().strftime('%Y%m%d')}.xlsx"
        )
