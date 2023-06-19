import requests
from bs4 import BeautifulSoup


def get_naver_blog_content(search_query, start_date, end_date, num_results):
    url = f"https://search.naver.com/search.naver?where=post&query={search_query}&st=date&date_from={start_date}&date_to={end_date}&date_option=8&srchby=all&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Ar%2Cp%3Afrom{start_date}to{end_date}&nlu_query=&nlo_query=&order_by=1&rcsection=&related_query=&sort=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    
    search_results = soup.select('.sh_blog_top')
    
    for i in range(min(num_results, len(search_results))):
        blog_title = search_results[i].select_one('.sh_blog_title').text
        blog_url = search_results[i].select_one('.sh_blog_title')['href']
        
        blog_response = requests.get(blog_url)
        blog_soup = BeautifulSoup(blog_response.text, 'html.parser')
        
        blog_content = blog_soup.select_one('.se-main-container').text
        
        print(f"Title: {blog_title}")
        print(f"URL: {blog_url}")
        print(f"Content: {blog_content}")
        print("-----------------------------------------")

# 사용 예시
search_query = input("검색어를 입력하세요: ")
start_date = input("검색 시작 날짜를 입력하세요 (YYYYMMDD 형식): ")
end_date = input("검색 종료 날짜를 입력하세요 (YYYYMMDD 형식): ")
num_results = int(input("검색 결과 수를 입력하세요: "))

get_naver_blog_content(search_query, start_date, end_date, num_results)
