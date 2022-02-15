# 지니뮤직 차트200 이미지 50장 저장
import requests
from bs4 import BeautifulSoup

url='https://www.genie.co.kr/chart/top200'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 지니뮤직 50개 이미지 링크 검색
imgs = soup.find_all("a",{"class":"cover"})

# 50개 다운로드
for i,img in enumerate(imgs):
    # 이미지 src 링크 추출
    img_url = img.find("img")['src']
    if img_url:
        # 이미지url requests 객체 저장
        img_res = requests.get("http:"+img_url)
        img_res.raise_for_status()
        
        # 저장파일 열기
        with open("genie_{}.jpg".format(i+1),"wb") as f:
            # 파일 저장
            f.write(img_res.content)
        print("http:"+img_url)
    else:
        continue    
print(len(imgs))
# print("http:"+imgs)

