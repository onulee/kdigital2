# 다음 금융 > 국내 > 외국인/기관매매
# 순매수 종목 30개 파일로 저장

import csv
import requests
from bs4 import BeautifulSoup


# 웹스크래핑 기본형태
url='https://new.land.naver.com/complexes/101516?ms=37.4820913,126.8983193,17&a=APT:ABYG:JGC&e=RETAIL'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# //*[@id="boxInfluentialInvestors"]/div[2]
data_rows = soup.find("div",{"class":"item_area"})
print(data_rows)

