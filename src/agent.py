from src.search import search_web
from src.retriever import upsert_search_results, query_documents
from src.summarizer import summarize_documents
from src.report import save_report_as_pdf

def run_research_pipeline(query: str, save_pdf: bool = True):
    # Step 1: Search
    results = search_web(query, num_results=5)

    # Step 2: Store in Pinecone
    upsert_search_results(results)

    # Step 3: Retrieve docs
    docs = query_documents(query, top_k=3)

    # Step 4: Summarize
    summary = summarize_documents(query, docs)

    # Step 5: Export to PDF
    if save_pdf:
        save_report_as_pdf(summary, filename="research_report.pdf")

    return summary

if __name__ == "__main__":
    query = "Latest trends in AI for 2025"
    report = run_research_pipeline(query)
    print("\n=== Research Report ===\n")
    print(report)
