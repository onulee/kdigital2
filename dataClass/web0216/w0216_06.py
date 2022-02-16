import csv
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 크롬 드라이버 로딩
browser = webdriver.Chrome()
url = 'https://m.sports.naver.com/beijing2022/medal/index'
browser.get(url)
time.sleep(3)
browser.find_element_by_class_name("Medal_button_more__2oy_Q").click()

# 클릭후 db에서 가져오는 시간이 걸림. 시간지연
time.sleep(3)
# 소스 바로 가져옴.
soup = BeautifulSoup(browser.page_source,"lxml")

with open("naver_oly3.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())
    # f.write(browser.page_source)
    
print("프로그램 저장완료")  


# 웹스크래핑 기본형태
# url='https://m.sports.naver.com/beijing2022/medal/index'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

  