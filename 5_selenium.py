#네이버 자동로그인
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) #불필요한 메시지 제거

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options) #크롬드라이버 주소 "./chromedriver_win32/chromedriver.exe"




#1. 네이버 이름
browser.get("http://www.naver.com")
time.sleep(2)


#2. 로그인 버튼 클릭
user_id = "ehdgml506"
user_pw = "ckrdlckrdl159!!"

elem = browser.find_element(By.CLASS_NAME , "link_login")
elem.click()

#3. id, pw 입력
login_id = browser.find_element(By.ID, "id")
login_id.click()
pyperclip.copy(user_id)
login_id.send_keys(Keys.CONTROL, 'v')

login_pw = browser.find_element(By.ID, "pw")
login_pw.click()
pyperclip.copy(user_pw)
login_pw.send_keys(Keys.CONTROL, 'v')

#4. 로그인 버튼 클릭 후 브라우저 등록 버튼 클릭
browser.find_element(By.ID,'log.login').click()
browser.find_element(By.ID, "new.save").click()
