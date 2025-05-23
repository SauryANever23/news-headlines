import re
import requests
from bs4 import BeautifulSoup


url1 = 'https://news.ycombinator.com/news' # For ycombinator

res = requests.get(url1)

soup1 = BeautifulSoup(res.text, 'html.parser')

def get_headlines(p) -> list:
    headlines = []
    try:
        for item in p.select(".titleline"):
            headlines.append(item.text)
    except Exception as e:
        print(f"Error {e}")

def get_links(p) -> list:
    spans = p.find_all("span", {"class": "titleline"})
    link_list = []
    try:
        for span in spans:
            links = span.find_all("a", href=True)
            for link in links:
                link_list.append(link['href'])

    except Exception as e:
        print(f"some error occoured: {e}")

    finally:
        return link_list
    
a = get_links(soup1)
print(a)