from langchain_openai import ChatOpenAI
from prompts.summarize_news import get_summarize_newscontent_prompts
from dotenv import load_dotenv
import os
from langsmith import traceable
from datetime import datetime
from tools.save_news import write_news_file
import logging

logger=logging.getLogger(__name__)

load_dotenv()

@traceable
def get_suumarized_news_content() -> list[str]:
    logging.info("inside get_suumarized_news_content....")
    prompts=get_summarize_newscontent_prompts()

    llm=ChatOpenAI(model="gpt-4o")

    summarized_news_list: list[str]=[]

    for prompt in prompts:
        
        summarized_news=llm.invoke(prompt)
        summarized_news_list.append(summarized_news.content)
   
    return summarized_news_list
