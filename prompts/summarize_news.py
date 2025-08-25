from langchain_core.prompts import PromptTemplate
from tools.news_feeder import get_latest_news_feed



def get_summarize_newscontent_prompts()-> list[str]:
    
    latest_items=get_latest_news_feed()
    latest_items=latest_items[:30]

    prompt_list=list()

    summarize_news_template="""
        You are a tech journalist. Summarize the following news article in 4-5 sentences,
        highlighting the key facts, context, and implications, and create a catching title.
        Keep a line between summary and title, also quote the source and provide link to the source:

        Title: {title}
        Content: {content}
        Source: {source}
        Link: {link}
        """

    prompt = PromptTemplate(
            template=summarize_news_template,
            input_variables=["title", "content","source","link"]
        )

    for item in latest_items:

        
        # Format the prompt with actual values
        formatted_prompt = prompt.format(
            title=item['title'],
            content=item['content'],
            source=item['source'],
            link=item['link']
        )

        prompt_list.append(formatted_prompt)

    return prompt_list
