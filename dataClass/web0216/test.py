from csv import writer
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import requests
from bs4 import BeautifulSoup


# 크롬 드라이버를 사용함. 
# 같은 위치에 있지 않으면 c:\download\chromedriver.exe 위치지정
browser = webdriver.Chrome()
browser.get("https://m.sports.naver.com/beijing2022/medal/index")

time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")

with open('test.html',"w",encoding="utf-8") as f:
    f.write(soup.prettify())
# print(browser.page_source)