# gmarket 베스트 제목, 가격을 출력하시오.

import requests
from bs4 import BeautifulSoup
url='http://corners.gmarket.co.kr/Bestsellers'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# //*[@id="gBestWrap"]/div/div[3]/div[2]/ul/li[1]/a
item1 = soup.find("div",{"id":"topPlusItems"}).find_next_sibling("div")
# item2 = item1.find("li").a.img["alt"]
items = item1.find_all("li")
for idx,item in enumerate(items):
      name1 = item.a.img["alt"]
      price1 = item.find("div",{"class":"s-price"}).strong.span.span.get_text()
      print(idx+1,":",name1)
      print("가격 : ",price1)
