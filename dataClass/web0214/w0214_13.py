# 독립일기 10개 출력하시오.
import requests
from bs4 import BeautifulSoup

# 1-4페이지 까지 제목을 출력
# for page in range(1,5):
url="https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# //*[@id="content"]/table/tbody
tbody1 = soup.find("div",{"id":"content"}).table
cartoons = tbody1.find_all("tr")
print(len(cartoons))
