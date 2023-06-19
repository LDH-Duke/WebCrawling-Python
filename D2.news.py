# 네이버 자동로그인
import time
import pyperclip
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())
# 크롬드라이버 주소 "./chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(service=service, options=chrome_options)

# 테스트주소
# https://blog.naver.com/gldiflll/223069712166
# https://blog.naver.com/h99980/223095697086
# https://blog.naver.com/junexun/223105245296
# https://blog.naver.com/hyoeth/222993153713

url = 'https://auto.danawa.com/auto/?Work=record&Tab=Model&Month=2022-05-00&MonthTo=2023-05-00'


def find_url(input):  # 크롤링 블로그 url 추출 함수
    # 네이버 접속
    browser.get(
        'https://auto.danawa.com/auto/?Work=record&Tab=Model&Month=2022-05-00&MonthTo=2023-05-00')
    browser.implicitly_wait(10)

    # 검색탭 클릭 후 입력
    search = browser.find_element(By.CSS_SELECTOR, "input#query.search_input")
    search.click()
    search.send_keys(input)
    search.send_keys(Keys.ENTER)
    browser.implicitly_wait(10)

    # VIEW탭으로 이동 후 블로그 카테고리 선택
    browser.find_element(By.LINK_TEXT, "VIEW").click()
    browser.implicitly_wait(10)
    browser.find_element(By.LINK_TEXT, "블로그").click()
    browser.implicitly_wait(10)

    # 스크롤 처리
    # bf_sc = browser.execute_script("return window.scrollY")
    cur_height = browser.execute_script("return document.body.scrollHeight")
    print(cur_height)
    while True:
        browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

        update_height = browser.execute_script(
            "return document.body.scrollHeight")
        time.sleep(2)
        browser.implicitly_wait(10)

        if update_height > 130000:
            print(update_height)
            break

    browser.implicitly_wait(10)
    # 반복문으로 n개 url 값 list에 저장 후 리턴
    url_list = []
    for i in range(701, 1001):
        link_selector = f"div._more_contents_event_base > ul > li#sp_blog_{i} > div > a"
        link = browser.find_element(By.CSS_SELECTOR, link_selector)

        url_list.append(link.get_attribute("href"))

    return url_list


search = '카페 리뷰'
url_list = find_url(search)
# print(url_list, len(url_list))

text = ''
for url in url_list:
    browser.get(url)

    try:
        browser.switch_to.frame("mainFrame")
        r = browser.page_source

        soup = BeautifulSoup(r, "html.parser")

        a = soup.find_all("div", attrs={"class": "se-module se-module-text"})

        for i in a:
            text = text + i.get_text()
            # print(i.get_text())
        # text = text + '='*50

    except:
        print('에러')

    # print('='*50)
with open('data1000.txt', 'w', encoding='utf8') as f:
    f.write(text)
