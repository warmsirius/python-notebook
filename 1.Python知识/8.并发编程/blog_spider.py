import requests
from bs4 import BeautifulSoup

urls = [f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)]


def craw(url):
    resp = requests.get(url)
    # print(url, len(resp.text), resp.status_code)
    return resp.text


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]


if __name__ == "__main__":
    craw(urls[0])
    print(parse(craw(urls[0])))
