import requests
from bs4 import BeautifulSoup

for page in range(2017,2022):
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(page)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    # img url이 있는 링크 검색
    imgs = soup.find_all("img",{"class":"thumb_img"})

    # 역대 순위 5개를 가져옴.
    for idx,img in enumerate(imgs):
        img_url = img['src']
        print(img_url)
        # 각각의 이미지의 링크를 가져와서 저장 시킴
        img_res = requests.get(img_url) 
        img_res.raise_for_status()
        
        # 파일 저장
        with open("movie_{}_{}.jpg".format(page,idx+1),"wb") as f:
            f.write(img_res.content)
        
        # 이미지 5개가 다운로드 되면 종료
        if(idx==4):
            break


