import csv
import requests
from bs4 import BeautifulSoup


# 웹스크래핑 기본형태
url='https://finance.naver.com/sise/sise_market_sum.naver?&page=1'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 파일이름 선언
filename="시가총액_20220216.csv"
# 파일 저장
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)


data_rows = soup.find("table",{"class":"type_2"}).find("tbody").find_all("tr")
# data_rows = soup.find(class_='type_2')  # class를 찾는 단축형태
# print(soup.prettify())  # html소스가 정렬이 되어서 출력이 됨

for row in data_rows:
    columns = row.find_all("td")
    # data list형태로 저장이 되어서 넘어옴. [ 1, 삼성전자, 74,500,...]	
    # td가 1개만 있을때는 내용이 없으므로 제외
    if len(columns) <= 1:
        continue
    
    data = [column.get_text().strip() for column in columns ]
    # writerow로 저장을 하려면 list형태로 저장이 되어야 함.
    # data=[]
    # for column in columns:
    #     data = data.append(column.get_text().strip())
        
    # print(data)
    writer.writerow(data)


