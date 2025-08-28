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
from src.config import OPENAI_API_KEY
from langchain_openai import ChatOpenAI

def is_research_query(query: str) -> bool:
    """
    Simple heuristic to check if user query looks like a research question requiring a report.
    Returns True if yes, False for casual chit-chat or simple questions.
    """
    research_keywords = [
        'what', 'how', 'why', 'tell me', 'explain', 'describe', 'impact', 'effect',
        'trends', 'statistics', 'history', 'analysis', 'research', 'data',
        'report', 'study', 'comparison', 'advantages', 'disadvantages'
    ]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in research_keywords)

def run_research_pipeline(query: str, conversation_history: list[dict] = None, save_pdf: bool = True):
    conversation_history = conversation_history or []

    # Intent classification shortcut
    if not is_research_query(query):
        # Handle casual questions with short conversational response
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            openai_api_key=OPENAI_API_KEY,
            temperature=0.5
        )

        # Compose prompt with optional context from conversation
        context_text = ""
        for turn in conversation_history[-6:]:  # limited context
            role = "User" if turn["role"] == "user" else "Assistant"
            context_text += f"{role}: {turn['content']}\n"
        context_text += f"User: {query}\nAssistant:"

        try:
            response_obj = llm.invoke(context_text)
            response_text = response_obj.content if hasattr(response_obj, "content") else str(response_obj)
        except Exception as e:
            response_text = f"Error generating casual reply: {e}"

        # Update conversation history
        conversation_history.append({"role": "user", "content": query})
        conversation_history.append({"role": "assistant", "content": response_text})

        return {
            "summary": response_text,
            "conversation_history": conversation_history,
            "search_results": [],
            "documents": []
        }

    # Else full research workflow for research questions
    conversation_history.append({"role": "user", "content": query})

    # Step 1: Search web
    results = search_web(query, num_results=5)

    # Step 2: Store in Pinecone
    upsert_search_results(results)

    # Step 3: Retrieve relevant docs
    docs = query_documents(query, top_k=3)

    # Step 4: Summarize with multi-turn context
    summary = summarize_documents_with_context(conversation_history, docs)

    # Update conversation history with assistant's reply
    conversation_history.append({"role": "assistant", "content": summary})

    # Optionally save PDF report
    if save_pdf:
        save_report_as_pdf(summary, filename="research_report.pdf")

    return {
        "summary": summary,
        "conversation_history": conversation_history,
        "search_results": results,
        "documents": docs
    }

# For standalone testing
if __name__ == "__main__":
    query = "Latest trends in AI for 2025"
    report = run_research_pipeline(query)
    if "error" in report:
        print(f"Error: {report['error']}")
    else:
        print("\n=== Research Report ===\n")
        print(report["summary"])
