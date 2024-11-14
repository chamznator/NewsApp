import requests

def fetch_news(api_key, topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return articles
    else:
        print("Failed to fetch news:", response.status_code)
        return []