from tools.save_news import write_news_file
import os

current_dir=os.path.dirname(__file__)

file_path=os.path.join(current_dir,"test_file.txt")
news_items: list=[]

with open(file_path,"r") as f:
    file_content=f.read()
    news_items=file_content.split("====\n")

print(f"No of news items got::{len(news_items)}")
assert(len(news_items)>1)
write_news_file(news_items)



