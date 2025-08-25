
import feedparser
from newspaper import Article
from datetime import datetime, timedelta
import logging

logger=logging.getLogger(__name__)


feeds = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://mashable.com/feed/",
    "https://www.wired.com/feed/rss"
]

def get_latest_news_feed() -> list:
    logger.info("Inside get_latest_news_feed...")
    try:
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
        logger.info(f"No of news item received from news feeder {len(latest_items)}")
    except Exception as e:
        logger.error("Error occured while getting news feed") 
    return latest_items
