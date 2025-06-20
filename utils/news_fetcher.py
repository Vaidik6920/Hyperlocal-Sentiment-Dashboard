import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_news_articles(keyword, api_key, days_back):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days_back)
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": keyword,
        "from": start_date.strftime('%Y-%m-%d'),
        "to": end_date.strftime('%Y-%m-%d'),
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 100,
        "apiKey": api_key
    }

    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])

    data = [{
        "date": a["publishedAt"],
        "content": a["title"] + ". " + a.get("description", ""),
        "source": a["source"]["name"]
    } for a in articles if a.get("title")]

    return pd.DataFrame(data)

