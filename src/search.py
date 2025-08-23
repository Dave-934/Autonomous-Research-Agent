import requests
from src.config import SERPER_API_KEY

def search_web(query: str, num_results: int = 5):
    """Search Google using Serper.dev API"""
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
    payload = {"q": query, "num": num_results}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Search API failed: {response.text}")

    results = response.json().get("organic", [])
    return [
        {
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        }
        for item in results
    ]

if __name__ == "__main__":
    results = search_web("AI in healthcare 2025")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r['title']} | {r['link']}\n   {r['snippet']}\n")
