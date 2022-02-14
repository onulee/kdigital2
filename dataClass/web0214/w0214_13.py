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

tbody1 = soup.find("div",{"id":"content"}).table
cartoons = tbody1.find_all("tr")
count = 0
total = 0
for cartoon in cartoons:
    if cartoon.find("td",{"class":"title"}):
       print(cartoon.find("td",{"class":"title"}).find("a").get_text())
       count += 1
    if cartoon.find("div",{"class":"rating_type"}):
       total = total + float(cartoon.find("div",{"class":"rating_type"}).strong.get_text())
       print(cartoon.find("div",{"class":"rating_type"}).strong.get_text())
       
print("합계 : ",round(total,2))           
print("평균 : ",round(total/count,2))           
    
