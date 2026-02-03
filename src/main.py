from news_fetcher import fetch_market_news

def main():
    print("Fetching market news....\n")

    articles = fetch_market_news(limit=10)

    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article.title}")
        print(f"    Source: {article.source}\n")

    

if __name__ == "__main__":
    main()
