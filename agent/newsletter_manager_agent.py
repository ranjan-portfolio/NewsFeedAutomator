from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch,TavilyCrawl,TavilyExtract
from langchain_core.prompts import ChatMessagePromptTemplate
from dotenv import load_dotenv
from langchain.agents import initialize_agent,AgentType
from langchain.tools import Tool
from tools.deploy_s3 import deploy_html_toS3
from tools.cache_invalidation import invalidate_cloudfront_cache
from tools.send_mail import sendemail

load_dotenv()

tavily_search=TavilySearch(max_result=5)
tavily_extract=TavilyExtract()
tavily_crawl=TavilyCrawl()

model= ChatOpenAI(model="gpt-4o-mini")


deploy_tool=Tool(
    name="DeployHTMLtoS3",
    func=deploy_html_toS3,
    description="The tool deploys html to S3"
)

invalidate_cache=Tool(
    name="InvalidateCloudFrontCache",
    func=invalidate_cloudfront_cache,
    description="The tool invalidates cloud front cache",
    
)

send_email=Tool(
    name="SendEmail",
    func=sendemail,
    description="The tool sends email to subscribers"
)


agent=initialize_agent(
    tools=[tavily_search,tavily_extract,tavily_crawl,deploy_tool,invalidate_cache,send_email],
    llm=model,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)





template='''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Newz Bytezz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        nav {
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: center;
        }
        nav h1 {
            margin: 0;
        }
        .powered-by {
            font-size: 0.9em;
            color: #bbb;
            margin-top: 4px;
            font-style: italic;
        }
        .content {
            padding: 20px;
        }
        .story {
            margin-bottom: 40px;
        }
        .title {
            font-weight: bold;
            font-size: 1.5em;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

    <nav>
        <h1>Tech Newz Bytezz</h1>
        <div class="powered-by">Powered by AI</div>
    </nav>

    <div class="content">
    </div>

</body>
</html>

     '''

query = f"""
    Use Taveily Crawl with maxdepth=1 to get latest 30 technology news articles from past 24 hrs. 
    Please use following urls for crawling.
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://mashable.com/feed/",
    "https://www.wired.com/feed/rss"
    Then format the news in below JSON format
    - title
    - full story/content
    - source name
    - link
    Then Create an html page index.html using following template {template} and insert each json item inside
    <div class="content"> with new div <div class="story"></div>
    Then Use SendEmail to send email html page index.html to subscribers
    Then Use DeployHTMLtoS3 to deploy the index.html to S3 
    Then Use InvalidateCloudFrontCache cloudfront cache
    
""" 

# Though doing the work but not giving reliable output
print(agent.run(query))




