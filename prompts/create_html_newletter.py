from langchain.prompts import PromptTemplate



def generate_newsletter_html_prompt(news: list[str])->str :

    no_of_stories=len(news)

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

  

    news_page="====\n".join(news)

    html_generate_prompt_template='''
        You are my digital asistant. Given a whole news page with {num_stories} where each story starts with ====\n and Title starts
        with ** and ends with ** create an index.html page with provided template. **Do not skip or summarize stories**.
        Here is the html template {story_template}.Please add each story inside <div class="content"></div>.
        Here is the whole news page {whole_news}.
        Include **30 story** from the page in the final HTML. 
     '''
    
    prompt = PromptTemplate(
            template=html_generate_prompt_template,
            input_variables=["whole_news","story_template","num_stories"]
        )
    
    formatted_prompt = prompt.format(
            num_stories=no_of_stories,
            story_template=template,
            whole_news=news_page
        )

    

    return [formatted_prompt]
