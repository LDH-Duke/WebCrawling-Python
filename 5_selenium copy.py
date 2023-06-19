# 네이버 자동로그인
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())
# 크롬드라이버 주소 "./chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(service=service, options=chrome_options)


# 1. 네이버 이름
browser.get("https://blog.naver.com/hsyf221/223101879596")
# https://blog.naver.com/hyoeth/222993153713
# https://search.naver.com/search.naver?query=%EC%B9%B4%ED%8E%98%20%EB%A6%AC%EB%B7%B0&nso=&where=blog&sm=tab_opt
content = browser.find_element(By.TAG_NAME, "iframe")
# print(content)

browser.switch_to.frame(content)

r = browser.page_source


soup = BeautifulSoup(r, "html.parser")

# border = soup.select('#postListBody')
# border = soup.find(id='postListBody')
# print(border)
# a = border.find_all("div", attrs={"class": "se-module se-module-text"})
a = soup.find_all("div", attrs={"class": "se-module se-module-text"})

for i in a:
    print(i.get_text())
