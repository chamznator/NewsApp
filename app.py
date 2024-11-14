from flask import Flask, request, jsonify
from news_fetcher import fetch_news
from summarizer import summarize_text

app = Flask(__name__)
API_KEY = '014342c398174682bcc04311d4b82051'  # Replace with your actual News API key

@app.route('/fetch_summary', methods=['GET'])
def fetch_summary():
    topic = request.args.get('topic')
    if not topic:
        return jsonify({"error": "No topic provided"}), 400
    
    articles = fetch_news(API_KEY, topic)
    summaries = [summarize_text(article['content']) for article in articles if article['content']]
    
    return jsonify({"summaries": summaries})

if __name__ == '__main__':
    app.run(debug=True)