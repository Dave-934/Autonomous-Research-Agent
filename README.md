# Autonomous-Research-Agent: Next-Gen Conversational Research Automation

This project is an in-development, multi-turn Autonomous Research Agent (ARA). It intelligently answers research queries by searching the web, semantically retrieving and summarizing sources, and generating structured, cite-rich reports—or providing natural conversational replies as context dictates. Built with LangChain, OpenAI, Pinecone, Serper.dev, and Streamlit, ARA aims to mimic the workflow of a real researcher, letting you ask follow-ups and always retaining context.

***

## Features

- **Multi-turn conversation:** Remembers your previous questions and answers—adjusts context for follow-up queries.
- **Intent-based response:** Distinguishes between research queries (structured reports) and casual chat (conversational replies).
- **Real-time web search:** Uses Serper.dev (Google Search) for live internet results with robust paraphrased summarization.
- **Vector database retrieval:** Stores and retrieves semantic document embeddings using Pinecone.
- **LLM-driven summarization:** Leverages OpenAI’s GPT-4o-mini via LangChain for natural, high-quality synthesis.
- **Citable, PDF-friendly reports:** Generates markdown and PDF research reports with Introduction, Key Findings, Sources, and Summary.
- **Modern Streamlit interface:** Web UI with typewriter effect for engaging, “ChatGPT-like” user experience.
- **FastAPI backend:** Enables research automation and custom app integrations.
- **Docker deployment:** Simple, production-friendly containerization for local and cloud use.

***

## Requirements

- **Python 3.11+**
- **OpenAI API key** (for GPT model)
- **Serper.dev API key** (Google Search/Web API)
- **Pinecone API key** (vector database; account required)
- **(Optional: Docker for deployment)**

***

## Python Dependencies

_Typical Requirements (see requirements.txt for full list):_

- `langchain`
- `langchain-openai`
- `openai`
- `pinecone-client`
- `faiss-cpu` (optional, local vector store)
- `streamlit`
- `fastapi`
- `requests`
- `python-dotenv`
- `reportlab` (for PDF report output)

***

## Setup

1. **Clone this repository and enter the project folder.**
```
git clone https://github.com/Dave-934/Autonomous-Research-Agent.git
cd Autonomous-Research-Agent
```
   
2. **Set up your environment variables:**
    - Create a `.env` file in the root:

```
OPENAI_API_KEY=your_openai_key
SERPER_API_KEY=your_serper_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX=your_pinecone_index
```

3. **Install Dependencies:**
```
pip install -r requirements.txt
```
4. **(Optional) Build and run via Docker:**
```
docker build -t ara-bot .
docker run -p 8000:8000 ara-bot
```


***

## Usage

- **Interactive web app:**
  ```
  streamlit run app/streamlit_app.py
  ```
  - Type your research queries or chat—context and memory persist.
- **REST API:**
  - Stat with FastAPI:
    ```
    uvicorn app.api:app --reload
    ```
    - Access /research via GET or use /download for PDF reports.
- Get instant structured reports or brief answers based on your intent.
- **Download** source-cited PDF reports from your browser.

***

## Notes

- **Conversational memory:** Maintains multi-turn context—follow-up questions leverage previous turns intelligently.
- **Intent detection:** Replies conversationally to greetings/thanks, but delivers structured reports for research or analytical queries.
- **Typewriter effect:** See assistant’s answers printed letter-by-letter for a dynamic, engaging chat.
- **PDF reporting:** All research reports can be saved as PDF from the UI.
- **Development Status:** This project is in active development—expect feature improvements, code refactoring, and possible breaking changes as it evolves.

***

## Troubleshooting

- **"KeyError"/API errors:** Check your .env values; ensure API keys are valid and have quota.
- **No sources/reports generated:** Make sure web search API is enabled and working.
- **Slow responses:** Web search and LLM calls depend on network/API speed; check service status and local connection.
- **Streamlit UI not updating:** Restart with Ctrl+C and rerun streamlit run ... if app hangs or UI glitches.
- **PDF not downloading:** Check browser pop-up/settings or file directory permissions.

***

