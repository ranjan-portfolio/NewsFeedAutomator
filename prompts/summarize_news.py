from langchain_core.prompts import PromptTemplate
from tools.news_feeder import get_latest_news_feed


def get_summarize_newscontent_prompts()-> list[str]:
    latest_items=get_latest_news_feed()

    prompt_list=list()
    for item in latest_items:

        summarize_news_template=f"""
        You are a tech journalist. Summarize the following news article with a catching title
        Keep a line between summary and title, also quote the source and provide link to the source:

        Title: {item['title']}
        Content: {item['content']}
        Source: {item['source']}
        Link: {item['link']}
        """

        prompt = PromptTemplate(
            template=summarize_news_template,
            input_variables=["title", "content","source","link"]
        )

        # Format the prompt with actual values
        formatted_prompt = prompt.format(
            title=item['title'],
            content=item['content'],
            source=item['source'],
            link=item['link']
        )

        prompt_list.append(formatted_prompt)

    return prompt_list
