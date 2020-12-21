import requests

urls = [f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)]


def craw(url):
    resp = requests.get(url)
    print(url, len(resp.text))


craw(urls[0])
