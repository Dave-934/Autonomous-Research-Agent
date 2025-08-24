# from langchain_openai import ChatOpenAI
# from src.config import OPENAI_API_KEY

# # GPT model for summarization
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     openai_api_key=OPENAI_API_KEY,
#     temperature=0.3
# )

# def summarize_documents(query: str, docs: list[str]) -> str:
#     """Summarize retrieved docs into a structured research report"""
#     if not docs:
#         return "No relevant documents found."

#     context = "\n\n".join(docs)
#     prompt = f"""
#     You are a research assistant.
#     The user asked: "{query}".

#     Based on these documents, write a structured research report.

#     Documents:
#     {context}

#     Format as:
#     ## Introduction
#     ## Key Findings
#     ## Sources
#     ## Summary
#     """
#     return llm.invoke(prompt).content

# def summarize_text(text: str) -> str:
#     """
#     Summarizes a given text using OpenAI's Chat model.
#     Used for follow-up Q&A inside the Streamlit app.
#     """
#     llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
#     prompt = f"Summarize or answer based on this text:\n\n{text}"
#     return llm.invoke(prompt).content









from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY

# Initialize LLM once, using modern .invoke() method as per deprecation warning
llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.3
)

# def summarize_documents_with_context(context: str, docs: list[str]) -> str:
#     """Summarize docs based on conversation context for multi-turn refinement."""
#     if not docs:
#         return "No relevant documents found."

#     context_docs = "\n\n".join(docs)
#     prompt = f"""
# You are a research assistant continuing a conversation with the user.

# Conversation history and current query:
# {context}

# Based on the following documents, generate a structured research summary.

# Documents:
# {context_docs}

# Format your response as:
# ## Introduction
# ## Key Findings
# ## Sources
# ## Summary
# """

def summarize_documents_with_context(history: list[dict], docs: list[str]) -> str:
    if not docs:
        return "No relevant documents found."

    dialogue = "The following is a conversation between a user and an assistant.\n\n"
    for turn in history:
        role = "User" if turn["role"] == "user" else "Assistant"
        dialogue += f"{role}: {turn['content']}\n"
    
    dialogue += "Assistant: Based on the following documents, please provide a detailed, structured response.\n\n"
    
    dialogue += "Documents:\n" + "\n\n".join(docs) + "\n"

    dialogue += """
Format your response as:
## Introduction
## Key Findings
## Sources
## Summary
"""

    try:
        # Use .invoke() to call LLM, which returns a message object with .content
        response = llm.invoke(dialogue)
        return response.content  # Extract content from response
    except Exception as e:
        return f"Error in summarization with context: {e}"

def summarize_text(text: str) -> str:
    """
    Summarizes a given text using OpenAI's Chat model.
    Used for follow-up Q&A inside the Streamlit app.
    """
    prompt = f"Summarize or answer based on this text:\n\n{text}"
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error in summarization: {e}"
