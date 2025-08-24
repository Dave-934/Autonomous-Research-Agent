# from src.search import search_web
# from src.retriever import upsert_search_results, query_documents
# from src.summarizer import summarize_documents
# from src.report import save_report_as_pdf

# def run_research_pipeline(query: str, save_pdf: bool = True):
#     # Step 1: Search
#     results = search_web(query, num_results=5)

#     # Step 2: Store in Pinecone
#     upsert_search_results(results)

#     # Step 3: Retrieve docs
#     docs = query_documents(query, top_k=3)

#     # Step 4: Summarize
#     summary = summarize_documents(query, docs)

#     # Step 5: Export to PDF
#     if save_pdf:
#         save_report_as_pdf(summary, filename="research_report.pdf")

#     return summary

# if __name__ == "__main__":
#     query = "Latest trends in AI for 2025"
#     report = run_research_pipeline(query)
#     print("\n=== Research Report ===\n")
#     print(report)





















from src.search import search_web
from src.retriever import upsert_search_results, query_documents
from src.summarizer import summarize_documents_with_context
from src.report import save_report_as_pdf

# def run_research_pipeline(query: str, conversation_history: list[dict] = None, save_pdf: bool = True):
#     try:
#         conversation_history = conversation_history or []

#         # Build context from history for prompt
#         context_text = ""
#         for turn in conversation_history:
#             context_text += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"
#         context_text += f"User: {query}\n"

#         # Step 1: Search web based on current query
#         results = search_web(query, num_results=5)

#         # Step 2: Store results in Pinecone
#         upsert_search_results(results)

#         # Step 3: Retrieve relevant documents
#         docs = query_documents(query, top_k=3)

#         # Step 4: Summarize documents with conversation context
#         summary = summarize_documents_with_context(context_text, docs)

#         # Step 5: Save report as PDF if desired
#         if save_pdf:
#             save_report_as_pdf(summary, filename="research_report.pdf")

#         # Append current turn to conversation history to keep memory
#         new_history = conversation_history + [{"user": query, "assistant": summary}]

#         return {
#             "query": query,
#             "search_results": results,
#             "documents": docs,
#             "summary": summary,
#             "conversation_history": new_history
#         }

#     except Exception as e:
#         return {"error": str(e), "query": query}

def run_research_pipeline(query: str, conversation_history: list[dict] = None, save_pdf: bool = True):
    try:
        conversation_history = conversation_history or []

        # Append the current user question to conversation history
        conversation_history.append({"role": "user", "content": query})

        # Search and embed as before
        results = search_web(query, num_results=5)
        upsert_search_results(results)
        docs = query_documents(query, top_k=3)

        # Summarize with full conversation history
        summary = summarize_documents_with_context(conversation_history, docs)

        # Append assistant's response to history
        conversation_history.append({"role": "assistant", "content": summary})

        if save_pdf:
            save_report_as_pdf(summary, filename="research_report.pdf")

        return {
            "query": query,
            "search_results": results,
            "documents": docs,
            "summary": summary,
            "conversation_history": conversation_history,
        }
    except Exception as e:
        return {"error": str(e), "query": query}


if __name__ == "__main__":
    query = "Latest trends in AI for 2025"
    report = run_research_pipeline(query)
    if "error" in report:
        print(f"Error during research: {report['error']}")
    else:
        print("\n=== Research Report ===\n")
        print(report["summary"])
