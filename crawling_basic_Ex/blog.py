# 네이버 자동로그인
import time
import pyperclip
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

# 네이버 접속
browser.get('http://www.naver.com')
browser.implicitly_wait(10)

# 검색탭 클릭 후 입력
search = browser.find_element(By.CSS_SELECTOR, "input#query.search_input")
search.click()
search.send_keys('카페 리뷰')
search.send_keys(Keys.ENTER)
browser.implicitly_wait(10)

# VIEW탭으로 이동 후 블로그 카테고리 선택
browser.find_element(By.LINK_TEXT, "VIEW").click()
browser.implicitly_wait(10)
browser.find_element(By.LINK_TEXT, "블로그").click()
browser.implicitly_wait(10)

# 스크롤 처리
bf_sc = browser.execute_script("return window.scrollY")

while True:
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    at_sc = browser.execute_script("return window.scrollY")

    if at_sc - bf_sc >= 400:
        break
    else:
        bf_sc = at_sc

time.sleep(5)
# for i in range(1, 101):

blog = browser.find_element(By.CSS_SELECTOR, "li#sp_blog_60.bx")
blog.click()

time.sleep(5)

browser.get(browser.current_url)
# content = browser.find_element(By.TAG_NAME, "iframe")

browser.switch_to.frame("mainFrame")
# # WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='mainFrame'and @name='mainFrame']")))
# # browser.switch_to.frame(browser.find_element(By.ID, 'mainFrame'))

# r = browser.page_source

# soup = BeautifulSoup(r, "html.parser")

# a = soup.find_all("div", attrs={"class": "se-module se-module-text"})

# for i in a:
#     print(i.get_text())
