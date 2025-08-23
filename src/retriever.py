import pinecone
from langchain_openai import OpenAIEmbeddings
from src.config import OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_INDEX

# Direct host from Pinecone console (copy/paste)
HOST = "https://research-agent-index-8ba122z.svc.aped-4627-b74a.pinecone.io"

# Connect to Pinecone (v3)
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX, host=HOST)

# OpenAI embeddings (1536 dimensions)
embeddings = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY,
    model="text-embedding-3-small"
)

def upsert_search_results(results: list[dict]):
    """Insert search results into Pinecone"""
    vectors = []
    for i, res in enumerate(results):
        text = f"{res['title']} - {res['snippet']} (Source: {res['link']})"
        vector = embeddings.embed_query(text)
        vectors.append((f"doc-{i}", vector, {"text": text}))
    index.upsert(vectors)

def query_documents(query: str, top_k: int = 5):
    """Query Pinecone for relevant documents"""
    vector = embeddings.embed_query(query)
    results = index.query(vector=vector, top_k=top_k, include_metadata=True)
    return [match["metadata"]["text"] for match in results["matches"]]
