# 풀빌라 9.5이상 리뷰 100
# 이름, 평점, 리뷰, 금액, url링크

import requests
from bs4 import BeautifulSoup

url="https://www.goodchoice.kr/product/result?keyword=%ED%92%80%EB%B9%8C%EB%9D%BC"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

items = soup.find("div",{"id":"poduct_list_area"}).find_all("li",{"class":"list_4 adcno3"})

name = items[0].find("img",{"class":"lazy"})["alt"]
price = items[0].find("div",{"class":"price"}).b.get_text()
score = items[0].find("p",{"class":"score"}).em.get_text()
review = items[0].find("p",{"class":"score"}).find("span").next_sibling.strip()
print(name)
print(price)
print(score)
print(review)

# for item in items:
#     name = item.find("div",{"class":"name"})
#     print(name)
    

# print(len(items))