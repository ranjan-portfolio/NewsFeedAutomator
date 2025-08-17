#
#
#. Get News Feed--> Summarize it by AI --> Generate HTML feed by AI --> use sendmail as agent to send mail to subscribers
# --> use boto3 to send the generated html file into s3 bucket
#
#

from llm_client.generate_index_page_by_llm import generate_indexpage_by_llm
from tools.send_mail import sendemail
import re


index=generate_indexpage_by_llm()

html_blocks = re.findall(r"```html(.*?)```", index, re.DOTALL)

print(html_blocks[0])

result=sendemail(html_blocks[0])

print(result)
