import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

search = input("검색어를 입력하세요 : ")

# 방법1
s_data = {'query': search}
Burl = "https://search.naver.com/search.naver"

res = requests.get(Burl, params=s_data, headers=headers)
# requests 패키지를 방식을 이용하여  params에 query값을 넘겨주는 방식도 있다.

# 방법2
# Burl='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
# url = Burl+search
# Burl에 네이버 검색시 나오는 주소값을 들고와서 qurey=까지만 들고와서 input()으로 입력받은 검색결과를 url변수에 Burl + search를 합쳐서 query에 검색결과를 전달하는 기초적인 방법도 존재한다.

res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all("div", attrs={"class": "product_info"})

for item in items:
    title = item.find("a", attrs={"class": "title elss"}).get_text()
    print(title)
