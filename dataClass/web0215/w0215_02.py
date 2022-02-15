# 풀빌라 9.5이상 리뷰 100
# 이름, 평점, 리뷰, 금액, url링크

import requests
from bs4 import BeautifulSoup

url="https://www.goodchoice.kr/product/result?keyword=%ED%92%80%EB%B9%8C%EB%9D%BC"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# ul > li 모든 상품의 전체 리스트를 가져오기
items = soup.find("div",{"id":"poduct_list_area"}).find_all("li",{"class":"list_4 adcno3"})

# 리스트 넘어온 것을 반복해서 출력
for idx,item in enumerate(items):
    name = item.find("img",{"class":"lazy"})["alt"]
    price = item.find("div",{"class":"price"}).b.get_text()
    
    # 평점 : 평점이 있는 것만 출력 없으면 넘어감.
    if item.find("p",{"class":"score"}).em:
        score = item.find("p",{"class":"score"}).em.get_text()
        # 평점이 9.5이상만 출력
        if float(score)>=9.5:
            pass
        else:
            continue  # 평점 9.5이하는 출력하지 않음.
    else:
        continue  
    
    # 리뷰 : span을 찾아서 다음에 있는 글자를 출력, strip은 빈공백 제거함수
    if item.find("p",{"class":"score"}).find("span").next_sibling.strip():
        review = item.find("p",{"class":"score"}).find("span").next_sibling.strip()
        # 평점에 있는 괄호제거 (721) -> 721 숫자만 남김.
        review = review[1:-1]
        if int(review)>=100:
            pass
        else:
            continue  # 100개이하는 출력하지 않음.
    else:
        continue 
    print("[ {} ]".format(idx+1))   
    print("제목 : ",name)
    print("가격 : ",price)
    print("평점 : ",score)
    print("리뷰 : ",review)
    print("-"*20)
    

print(len(items))