from flask import Flask, request, jsonify, render_template_string
from news_fetcher import fetch_news
from summarizer import summarize_text
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
API_KEY = os.getenv('NEWS_API_KEY')  # Load the API key from the environment variable

# Debug line to check API key loading
logging.debug(f"API_KEY loaded: {API_KEY}")

@app.route('/fetch_summary', methods=['GET'])
def fetch_summary():
    topic = request.args.get('topic')
    if not topic:
        return jsonify({"error": "No topic provided"}), 400
    
    # Fetch news articles, limiting to 5 articles directly from the API
    articles = fetch_news(API_KEY, topic, max_results=5)

    # Display the original articles in the response
    original_articles = [{"title": article["title"], "content": article["content"]} for article in articles if article.get("content")]

    # Combine content of all articles for summarization
    combined_text = "\n\n".join([article['content'] for article in articles if article.get('content')])

    # Summarize all articles into 3 or fewer paragraphs
    combined_summary = summarize_text(combined_text)

    # Create an HTML response displaying original articles and the summary
    html_template = """
    <h1>Original Articles</h1>
    {% for article in articles %}
        <h2>{{ article.title }}</h2>
        <p>{{ article.content }}</p>
        <hr>
    {% endfor %}
    <h1>Combined Summary</h1>
    <p>{{ summary }}</p>
    """
    return render_template_string(html_template, articles=original_articles, summary=combined_summary)

if __name__ == '__main__':
    app.run(debug=True)
