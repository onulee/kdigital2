import time
from tkinter.tix import Tree
# 구글드라이버 selenium
from selenium import webdriver
# keys입력에 관한 메소드
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 출력화면이 나타날때까지 대기하는 메소드
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 메소드
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

browser = webdriver.Chrome()
browser.maximize_window()
url='https://new.land.naver.com/complexes/391?ms=37.49209,126.911547,17&a=APT:ABYG:JGC&e=RETAIL'
browser.get(url)



#스크롤 내림
pre_height = browser.execute_script("return articleListArea.scrollHeight")
print("화면 높이 : ",pre_height)
time.sleep(2)
while True:
    # body스크롤 높이를 체크하는게 아니라, id=articleListArea 스크롤높이를 체크
    browser.execute_script("window.scroll(0,articleListArea.scrollHeight)")
    # 마우스 휠로 스크롤을 내림
    pyautogui.moveTo(50,700)
    time.sleep(2)
    pyautogui.scroll(-pre_height)
    time.sleep(2)
    
    # curr_height = browser.execute_script("return document.body.scrollHeight")
    # ${articleListArea.scrollHeight}
    curr_height = browser.execute_script("return articleListArea.scrollHeight")
    print("스크롤 후 높이 : ",curr_height)
    if curr_height == pre_height:
        break

    pre_height = curr_height
    
        
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

# print(soup.prettify())
