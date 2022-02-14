# 독립일기 10개 출력하시오.
import requests
from bs4 import BeautifulSoup
import re

# 1-4페이지 까지 제목을 출력
# for page in range(1,5):
url="https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# div 중 id가 content > table
tbody1 = soup.find("div",{"id":"content"}).table
# tr 모두 찾음
cartoons = tbody1.find_all("tr")
count = 0    # 평점이 있는 개수
total = 0    # 합계
for cartoon in cartoons:
    # td class=title만 출력
    if cartoon.find("td",{"class":"title"}):
       print(cartoon.find("td",{"class":"title"}).find("a").get_text())
       # 개수 1증가
       count += 1
    # div class=rating_type만 출력 
    if cartoon.find("div",{"class":"rating_type"}):
       # 평점 합계
       total = total + float(cartoon.find("div",{"class":"rating_type"}).strong.get_text())
       print(cartoon.find("div",{"class":"rating_type"}).strong.get_text())

# 합계출력 소수점 2자리까지 출력       
print("합계 : ",round(total,2))           
print("평균 : ",round(total/count,2))           
    
