from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY

# GPT model for summarization
llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.3
)

def summarize_documents(query: str, docs: list[str]) -> str:
    """Summarize retrieved docs into a structured research report"""
    if not docs:
        return "No relevant documents found."

    context = "\n\n".join(docs)
    prompt = f"""
    You are a research assistant.
    The user asked: "{query}".

    Based on these documents, write a structured research report.

    Documents:
    {context}

    Format as:
    ## Introduction
    ## Key Findings
    ## Sources
    ## Summary
    """
    return llm.invoke(prompt).content

def summarize_text(text: str) -> str:
    """
    Summarizes a given text using OpenAI's Chat model.
    Used for follow-up Q&A inside the Streamlit app.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    prompt = f"Summarize or answer based on this text:\n\n{text}"
    return llm.invoke(prompt).content

