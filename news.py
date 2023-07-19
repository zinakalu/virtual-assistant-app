import requests
import os

def get_news(query=None):
    url= "https://newsapi.org/v2/top-headlines?country=us&apiKey=a3fc01fbb62d48e6b93e82b4441e7b49"
    if query:
        url += f"&q={query}"
    response = requests.get(url)
    data = response.json()
    return data