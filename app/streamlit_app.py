import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.agent import run_research_pipeline

st.set_page_config(page_title="Autonomous Research Agent", page_icon="🤖", layout="wide")

st.title("🤖 Autonomous Research Agent")
st.write("Ask me a question and I’ll generate a structured research report with sources.")

query = st.text_input("Enter your research topic/question:")

if st.button("Run Research"):
    if not query.strip():
        st.warning("⚠️ Please enter a valid research question.")
    else:
        with st.spinner("🔎 Researching..."):
            report = run_research_pipeline(query)

        st.success("✅ Research complete! PDF saved as `research_report.pdf`")

        # Show formatted preview
        st.subheader("📄 Report Preview")
        st.markdown(report)

        # Download PDF
        filename = "research_report.pdf"
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                st.download_button(
                    label="📥 Download PDF Report",
                    data=f,
                    file_name=filename,
                    mime="application/pdf"
                )
