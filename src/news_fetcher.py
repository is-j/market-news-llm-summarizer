import os
import requests
from dotenv import load_dotenv
from models import Article

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_market_news(limit: int = 10) -> list[Article]:
    if not NEWS_API_KEY:
        raise RuntimeError("Error: news api key isn't set in the environment variables.")
        
    params = {
        "apiKey": NEWS_API_KEY,
        "category": "business",
        "language": "en",
        "pageSize": limit
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()
    articles = []

    for item in data["articles"]:
        articles.append(
            Article(
                title=item.get("title", "No title"), 
                source=item.get("source", {}).get("name", "Unknown"),
                published_at=item.get("publishedAt", ""),
                content=item.get("description"),
            )
        )
    return articles 

