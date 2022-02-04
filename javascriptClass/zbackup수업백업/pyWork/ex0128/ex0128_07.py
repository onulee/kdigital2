from logging import exception
import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

## 
cartoons = soup.find_all("tr")
total_num=0
count=0

for cartoon in cartoons:
    try:
        c_title = cartoon.find("td",{"class":"title"}).a.get_text()
        c_num = cartoon.find("div",{"class":"rating_type"}).strong.get_text()
        total_num += float(c_num) #string -> float
        count += 1
        print("제목 : {},평점 : {}".format(c_title,c_num))
    except:
        pass 
print("전체 점수 : ",round(total_num,2))
print("평균 점수 : ",round(total_num/count,2))       
    

# cartoons = soup.find_all("td",{"class":"title"})
# for cartoon in cartoons:
#     print(cartoon.a.get_text())
    
# cartoons2 = soup.find_all("div",{"class":"rating_type"})
# for cartoon2 in cartoons2:
#     print(cartoon2.strong.get_text())    

# for cartoon in cartoons:
#     cartoon_num = cartoon.find("td",{"class":"num"})
#     print(cartoon_num)
#     cartoon_title = cartoon.a.get_text()
#     print(cartoon_title)
    # print("제목 : {}, 평점 :{}".format(cartoon_title,cartoon_num))
    