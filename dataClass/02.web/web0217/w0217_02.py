# headless 사용안함
# 야놀자 검색 > 제주리조트
# 일자 : 2/25-27
# 리조트를 저장, 출력하시오.

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

browser = webdriver.Chrome()
browser.maximize_window()
url='https://www.yanolja.com/'
browser.get(url)

# time.sleep(2)
# 검색클릭
browser.find_element_by_xpath('//*[@id="__next"]/section/header/div/div[3]/button[1]').click()

# 검색창 제주리조트 입력
elem = browser.find_element_by_class_name('SearchInput_input__342U2')
elem.send_keys('제주리조트')
elem.send_keys(Keys.ENTER)

#화면이 나타날때까지 대기
# WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[1]/main/div/section[2]/div/div/div[1]')))
time.sleep(5)

#스크롤 내림
pre_height = browser.execute_script("return document.body.scrollHeight")
time.sleep(2)
while True:
    browser.execute_script("window.scroll(0,document.body.scrollHeight)")
    # 마우스 휠로 스크롤을 내림
    pyautogui.scroll(-pre_height)
    time.sleep(2)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == pre_height:
        break

    pre_height = curr_height
    
        
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

print(soup.prettify())




