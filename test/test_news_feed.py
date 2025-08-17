from tools.news_feeder import get_latest_news_feed
import json


latest_items=get_latest_news_feed()

with open("example.txt", "w") as file:
    for item in latest_items:
        file.write(item["title"] + "\n")
        file.write("===========\n")
        file.write(item["content"] + "\n\n")