import requests
from bs4 import BeautifulSoup
import re

url='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor='
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

# ul1 = soup.find("ul",{"id":"productList"})
items = soup.find_all("li",{"class":re.compile("^search-product")})

for item in items:
    name = item.find("div",{"class":"name"}).get_text()
    price = item.find("strong",{"class":"price-value"}).get_text()
    print(name)
    print(price)
    # 평점이 없는 경우 발생
    rating = item.find("em",{"class":"rating"})
    if rating:
        print(rating.get_text())
    else:
        print("[ 평점 없음 ]")    

# print(len(items))
