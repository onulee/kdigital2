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

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

url="https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")
print("접속정보 : ",soup.find("div",{"id":"detected_value"}).a.get_text())
print("프로그램 종료")

browser.quit()

