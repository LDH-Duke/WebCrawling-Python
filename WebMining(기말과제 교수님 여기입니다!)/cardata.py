import requests
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())
# 크롬드라이버 주소 "./chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(service=service, options=chrome_options)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

url = "https://auto.danawa.com/auto/?Work=record&Tab=Model&Month=2022-05-00&MonthTo=2023-05-00"

res = requests.get(url, headers=headers)
res.raise_for_status()

html = res.content.decode('utf-8', 'replace')

soup = BeautifulSoup(html, "html.parser")

ranks = []
names = []
sales_rates = []
market_shares = []
brands = []
urls = []
car_types = []
prices = []
launch_date = []

cars_info = soup.find_all('tr', class_=False)

for i, car_info in enumerate(cars_info):

    try:
        # 랭킹
        rank = car_info.find("td", attrs={"class": "rank"}).get_text()
        ranks.append(rank)
        # 자동차명
        name = car_info.find('td', attrs={"class": "title"}).get_text().strip()
        names.append(name)
        # 판매량
        sales_rate = car_info.find('td', attrs={"class": "num"}).get_text()
        sales_rates.append(sales_rate)
        # 점유율
        market_share = car_info.find_all('td', class_=False, limit=3)
        market_shares.append(market_share[2].get_text())
        # url
        url = car_info.find('a')['href']
        urls.append('https://auto.danawa.com/'+url)

        # print(rank, name, sales_rate,
        #     market_share[2].get_text(), "\n=====================")
        # count += 1
    except Exception as e:
        continue

    if i == 100:
        break

for u in urls:
    browser.get(u)
    browser.implicitly_wait(10)

    html = browser.page_source
    soup2 = BeautifulSoup(html, "html.parser")

    # 브랜드명
    brand = soup2.find('img', attrs={"class": "logo"})['alt']
    brands.append(brand)
    # 타입, 출시일자
    span = soup2.find('span', attrs={"class": "row"})

    car_type = span.find('span', id=False).get_text()
    car_types.append(car_type)

    date = span.find(
        'span', attrs={'id': 'trimLaunchDate'}).get_text().replace(' 출시', '')
    launch_date.append(date)

    # 가격
    price = soup2.find(
        'div', attrs={'class': 'right eTextPriceInfo'}).get_text().replace(',', '')
    prices.append(price)
    print(price)

    # print(brand, car_type, price, date, '\n====')


df = pd.DataFrame(
    {
        "rank": ranks,
        "brand": brands,
        "name": names,
        "type": car_types,
        "price": prices,
        "date": launch_date,
        "sales_rate": sales_rates,
        "market_share": market_shares,
    }
)

df.to_csv('car_data.csv', index=False, encoding='utf-8-sig')
