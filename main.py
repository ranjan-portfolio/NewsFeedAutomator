#
#
#. Get News Feed--> Summarize it by AI --> Generate HTML feed by AI --> use sendmail as agent to send mail to subscribers
# --> use boto3 to send the generated html file into s3 bucket
#
#

from llm_client.generate_index_page_by_llm import generate_indexpage_by_llm
from llm_client.summarize_news_by_llm import get_suumarized_news_content
from tools.send_mail import sendemail
from tools.deploy_s3 import deploy_html_toS3
from tools.cache_invalidation import invalidate_cloudfront_cache
from tools.save_news import write_news_file
import re
from rag.NewsVector import create_vector_db


news_list=get_suumarized_news_content()
file_path=write_news_file(news_list)
create_vector_db(file_path)
index=generate_indexpage_by_llm(news_list)
html_blocks = re.findall(r"```html(.*?)```", index, re.DOTALL)
email_response=sendemail(html_blocks[0])
print(email_response)
s3_response=deploy_html_toS3(html_blocks[0])
print(s3_response)
print("going to invalidate cloudfront cache")
status=invalidate_cloudfront_cache()
print(status)

