from tools.save_news import write_news_file
from rag.NewsVector import create_vector_db
import os

current_dir=os.path.dirname(__file__)

file_path=os.path.join(current_dir,"test_file.txt")
news_items: list=[]

with open(file_path,"r") as f:
    file_content=f.read()
    news_items=file_content.split("====\n")

print(f"No of news items got::{len(news_items)}")
assert news_items,"No news items found in test_file.txt"
file_path=write_news_file(news_items)
chromadb=create_vector_db(file_path)

query = "Latest AI news. Please extract the full news do not summarize or truncate the news"
retriever = chromadb.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.1},
)
results=retriever.invoke(query)

for i, r in enumerate(results, 1):
    print(f"Result {i}: {r.page_content}")