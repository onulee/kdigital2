import requests
from bs4 import BeautifulSoup

url='https://comic.naver.com/webtoon/weekday'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# 웹툰 모두 출력하시오.
# //*[@id="content"]/div[4]/div[1]/div/ul
soup = BeautifulSoup(res.text,"lxml")
div1 = soup.find("div",{"id":"content"})
div2 = div1.find("div",{"class":"list_area daily_all"})
cartoons = div2.find_all("li")
for idx,cartoon in enumerate(cartoons):
    name1 = cartoon.find("img")["title"]
    print(idx+1,":",name1)

# print("개수 : ",len(cartoons))
# print(cartoons[0])
