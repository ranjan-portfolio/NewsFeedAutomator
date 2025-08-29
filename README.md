# NewsFeedAutomator

**Tech Newz Bytezz**  
Live Demo: [https://newautomator.rancher-ranjanaws.com/](https://newautomator.rancher-ranjanaws.com/)

<img width="435" height="622" alt="Screenshot" src="https://github.com/user-attachments/assets/cc9c52bb-d0d0-40c0-9e0b-4bedcccfbf0f" />

## Overview

NewsFeedAutomator is a Python project that automates the process of collecting, summarizing, and distributing the latest technology news. It fetches articles from popular tech RSS feeds, summarizes them using AI, generates an HTML newsletter, and can send updates via email and deploy the newsletter to an S3 bucket for web hosting.

## Features

- **Automated news fetching**: Collects articles from multiple tech RSS feeds within the last 24 hours.
- **AI-powered summarization**: Summarizes news content using LLMs.
- **Newsletter generation**: Produces a styled HTML newsletter ("Tech Newz Bytezz").
- **Distribution**: Sends newsletters to subscribers via email and deploys HTML to S3 with cache invalidation.
- **Extensible agents**: Uses LangChain and OpenAI for orchestrating workflow and tools.

## News Sources

- TechCrunch
- The Verge
- Mashable
- Wired

## How It Works

1. **Fetch News**: Uses `feedparser` and `newspaper3k` to fetch and parse news items from RSS feeds.
2. **Summarize Content**: Utilizes LLMs to summarize the fetched articles.
3. **Generate Newsletter**: Formats the summarized content into an HTML template.
4. **Send and Deploy**: Sends the newsletter by email and uploads it to AWS S3. Optionally, invalidates CloudFront cache for fresh content.

## Project Structure

- `main.py` — Orchestrates the entire workflow.
- `tools/news_feeder.py` — Fetches and parses news feeds.
- `llm_client/` — Summarization and index page generation using LLMs.
- `tools/send_mail.py` — Handles email delivery.
- `tools/deploy_s3.py` — Deploys the newsletter to AWS S3.
- `tools/cache_invalidation.py` — Invalidates CloudFront cache.
- `rag/` — Stores news summaries and vector database scripts.
- `agent/newsletter_manager_agent.py` — Agent-based orchestration with LangChain.

## Quick Start

### Requirements

- Python 3.8+
- pip (Python package installer)
- AWS credentials (for S3/CloudFront operations)
- OpenAI API key (for summarization)

### Installation

```bash
git clone https://github.com/ranjan-portfolio/NewsFeedAutomator.git
cd NewsFeedAutomator
pip install -r requirements.txt
```

### Configuration

Set up environment variables in a `.env` file:
```
OPENAI_API_KEY=your-openai-key
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
...
```

### Running the Project

```bash
python main.py
```

This will fetch the latest tech news, summarize and format them, send out emails, and deploy the newsletter to S3.

## Testing

Basic test examples can be found in `test/`:
```bash
python test/test_news_feed.py
```

## Dependencies

- `feedparser`
- `newspaper3k`
- `boto3`
- `langchain`
- `openai`
- `python-dotenv`
- `re`, `logging`, and other Python standard libraries

## Example Output

A newsletter HTML page with top tech articles, delivered to subscribers and available on the web.

---

*For more details, refer to the code and comments in each module.*

''' Tech Newz bytezz link : https://technewzbytez.rancher-ranjanaws.com/
