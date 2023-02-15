import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all("img", attrs={"class":"thumb_img"})
    print(f"{year}년 1~5위 영화")
    for idx, image in enumerate(images):
        image_url = image['src']
        if image_url.startswith("//"): #.startswith("문자열 or 튜플") 해당 문자열이나 튜플로 시작하는가에 대해 true false값으로 반환(대소문자 구분)
            image_url = "https:"+image_url

        image_res = requests.get(image_url)
        with open("{}image{}.jpg".format(year,idx+1), "wb") as f:
            f.write(image_res.content)
        if idx >= 4:
            break