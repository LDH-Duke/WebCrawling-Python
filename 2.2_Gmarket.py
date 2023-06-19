# 쿠팡 크롤링 차단으로 인하여 G마켓으로 변경
# 최근 5개 페이지 검색결과 가져오기 (f-string사용)
import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

for i in range(1, 6):
    url = f"https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&t=a&k=32&p={i}"

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.find_all("div", attrs={
                          "class": "box__component box__component-itemcard box__component-itemcard--general"})

    print('===========')
    print(f'{i}페이지')
    print('===========')
    for item in items:
        name = item.find("span", attrs={"class": "text__item"}).get_text()
        price = item.find(
            "strong", attrs={"class": "text text__value"}).get_text()

        rate = item.find("span", attrs={"class": "image__awards-points"})
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점이 없습니다."

        buy_cnt = item.find(
            "li", attrs={"class": "list-item list-item__pay-count"})
        if buy_cnt:
            buy_cnt = buy_cnt.get_text()
        else:
            buy_cnt = "구매자가 없습니다."

        rink = item.find("a", attrs={"class": "link__item"}).attrs["href"]

        print(f"제품명 : {name}", f"\n가격 : {price}", f"\n평점 : {rate}",
              f"\n구매자 수 : {buy_cnt}", f"\n링크 : {rink}")
        print("="*120)
