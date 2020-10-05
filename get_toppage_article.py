import requests
from bs4 import BeautifulSoup

res = requests.get('https://hatenablog.com/')
soup = BeautifulSoup(res.text, 'html.parser')

# 記事一覧を取得
for url in soup.find_all(class_="serviceTop-entry-title"):
    print(url.find('a').get('href'))
    print(url.text)
