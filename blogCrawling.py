# 쿠팡 크롤링 차단으로 인하여 G마켓으로 변경
# 최근 5개 페이지 검색결과 가져오기 (f-string사용)
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(
#     executable_path=r'C:\Users\LEEDONGHE\Desktop\DUKE\study\project\WebCrawling-Python\chromedriver_win32\chromedriver.exe')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

url = "https://blog.naver.com/south0429/223028381157"

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

iframe = soup.find("iframe")
iframe_src = iframe.get("src")
iframe_res = requests.get(url+iframe_src)

iframe_soup = BeautifulSoup(iframe_res.text, 'lxml')

print(iframe_soup)
