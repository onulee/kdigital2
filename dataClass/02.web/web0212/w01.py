import requests
from bs4 import BeautifulSoup
# 네이버 웹툰 검색
url = "https://comic.naver.com/webtoon/weekday"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()     #에러시 종료

soup = BeautifulSoup(res.text,"lxml") #text을 lxml파싱해서 soup담음.
print(soup)                                  