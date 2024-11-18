import requests

def fetch_news(api_key, topic, max_results=5):
    url = f"https://newsapi.org/v2/everything?q={topic}&pageSize={max_results}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return articles
    else:
        print("Failed to fetch news:", response.status_code)
        return []
