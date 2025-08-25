import os
from datetime import datetime
import os
import logging

logger=logging.getLogger(__name__)

def write_news_file(newslist :list)-> str:
    logger.info("inside write_news_file ...")
    timenow=datetime.now()
    formatted_date_string=timenow.strftime("%d%m%Y%H%M%S")
    summary_file_name="summary_"+formatted_date_string+".txt"

    current_file_path=os.path.dirname(__file__)

    document_path=os.path.join(current_file_path,"..","rag","documents",summary_file_name)
    print(f"got news items in save_news:: {len(newslist)}")
    try:
        for news in newslist:
            with open(document_path,"a") as f:
                f.write(news)
    except Exception as e:
        logger.error(f"Exception occured..{e}")
    return document_path

   


    