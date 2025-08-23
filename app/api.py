from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from src.agent import run_research_pipeline

app = FastAPI(title="Autonomous Research Agent API")

@app.get("/research")
async def research(query: str = Query(..., description="Research question")):
    report = run_research_pipeline(query)
    return {"query": query, "report": report, "pdf": "research_report.pdf"}

@app.get("/download")
async def download_pdf():
    return FileResponse("research_report.pdf", media_type="application/pdf", filename="research_report.pdf")
