import requests
from bs4 import BeautifulSoup

url ="http://corners.gmarket.co.kr/Bestsellers"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
print("응답 코드 : ",res.status_code)

soup = BeautifulSoup(res.text,"lxml")
print("")
print("")
print("")

soup.find("")


# f = open("test1.html","w",encoding="utf-8")
# f.write(res.text)

