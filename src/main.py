import os 
import requests
from dotenv import load_dotenv


load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_market_news():
    if not NEWS_API_KEY:
        raise RuntimeError("Error: news api key isn't set in the environment variables.")

    params = {
        "apiKey": NEWS_API_KEY,
        "category": "business",
        "language": "en",
        "pageSize": 5
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()["articles"]

def main():
    print("This is a market news summarizer. Starting...")
    articles = fetch_market_news()

    for i, article in enumerate(articles, start=1):
        title = article.get("title", "Untitled")
        source = article.get("source", {}).get("name", "Unknown Source")
        print(f"{i}. {title}")
        print(f"Source: {source}")


if __name__ == "__main__":
    main()