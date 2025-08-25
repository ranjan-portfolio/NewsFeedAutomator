from langchain_openai import ChatOpenAI
from llm_client.summarize_news_by_llm import get_suumarized_news_content
from dotenv import load_dotenv
from prompts.create_html_newletter import generate_newsletter_html_prompt
from langsmith import traceable
import logging

logger=logging.getLogger(__name__)
load_dotenv()

@traceable
def generate_indexpage_by_llm(news:list) -> str:

    logger.info("inside generate_indexpage_by_llm...")
    promptlist=generate_newsletter_html_prompt(news)

    llm=ChatOpenAI(model="gpt-4o")
        
    html_response=llm.invoke(promptlist[0])
    
    return html_response.content
