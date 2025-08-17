
import feedparser
from newspaper import Article
from datetime import datetime, timedelta

feeds = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://mashable.com/feed/",
    "https://www.wired.com/feed/rss"
]

def get_latest_news_feed() -> list:
    now = datetime.utcnow()
    last_24h = now - timedelta(hours=24)
    latest_items = []

    for feed in feeds:
        d = feedparser.parse(feed)
        for entry in d.entries:
           # print(entry)
            published = datetime(*entry.published_parsed[:6])
            if published > last_24h:
                article=Article(entry.link)
                article.download()
                article.parse()
                latest_items.append({
                    "title": entry.title,
                    "link": entry.link,
                    "content":article.text,
                    "published": published,
                    "source": feed
                })
    print(f"No of news item received from news feeder {len(latest_items)}")
    return latest_items
