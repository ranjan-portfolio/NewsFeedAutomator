from langchain.prompts import PromptTemplate



def generate_newsletter_html_prompt(news: list[str])->str :

    no_of_stories=len(news)

    print(no_of_stories)

    news_page="====\n".join(news)

    html_generate_prompt_template='''
        You are my digital asistant. Given a whole news page with {num_stories} where each story starts with ====\n and Title starts
        with ** and ends with ** generate an html page with a nav bar and brand Tech newz bytezz with title and story
        Here is the whole news page
        Page: {whole_news}
     '''
    
    prompt = PromptTemplate(
            template=html_generate_prompt_template,
            input_variables=["whole_news","num_stories"]
        )
    
    formatted_prompt = prompt.format(
            num_stories=no_of_stories,
            whole_news=news_page

        )

    

    return [formatted_prompt]
