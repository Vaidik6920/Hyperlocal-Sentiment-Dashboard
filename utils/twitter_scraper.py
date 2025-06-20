import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime, timedelta


def scrape_tweets(keyword, location, radius_km, days_back, max_results, region_filter=None):
    until = datetime.utcnow().date()
    since = until - timedelta(days=days_back)
    
    query = f"{keyword} since:{since} until:{until}"
    if location:
        query += f" near:'{location}' within:{radius_km}km"
    if region_filter:
        query += f" {region_filter}"

    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_results:
            break
        tweets.append({
            "date": tweet.date,
            "username": tweet.user.username,
            "content": tweet.content,
            "latitude": tweet.coordinates.latitude if tweet.coordinates else None,
            "longitude": tweet.coordinates.longitude if tweet.coordinates else None,
        })

    return pd.DataFrame(tweets)

