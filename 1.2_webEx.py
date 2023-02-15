# 외모지상주의
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=641253&weekday=fri"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")

##1. td태그 안에 class라는 속성의 값으로 title인 코드를 cartoons에 넣음
##2. cartoons의 리스트에서 제목과 url주소를 추출
#       cartoons = soup.find_all("td", attrs={"class": "title"})
#       for cartoon in cartoons:
#           print(cartoon.get_text(), "https://comic.naver.com"+cartoon.a["href"])

##1. 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class": "rating_type"})

for cartoon in cartoons:
    rate= cartoon.find("strong").get_text() #방법1. cartoon.strong.get_text() // 방법2. rate= cartoon.find("strong").get_text()
    total_rates += float(rate)

print("평균 점수 : ",round(total_rates/len(cartoons),3))
