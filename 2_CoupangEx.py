import requests
import re
from bs4 import BeautifulSoup

url = "https://browse.gmarket.co.kr/search?keyword=%eb%85%b8%ed%8a%b8%eb%b6%81&t=a"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
items = soup.find_all("div", attrs={"class":"box__component box__component-itemcard box__component-itemcard--general"})




# print(items[0].find("div", attrs={"class":"name"}).get_text())