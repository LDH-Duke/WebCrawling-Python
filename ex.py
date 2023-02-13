import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# rank1 = soup.find("li", attrs={"class":"rank01"})

webtoon = soup.find("a", text="외모지상주의-430화 통합된 4대크루 [1/2]")

print(webtoon)


