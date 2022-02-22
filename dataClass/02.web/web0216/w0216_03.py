from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버를 사용함. 
# 같은 위치에 있지 않으면 c:\download\chromedriver.exe 위치지정
browser = webdriver.Chrome()
browser.get("http://www.naver.com")

# id가 query인 정보를 가져옴.
elem = browser.find_element_by_id("query")
# elem 안의 정보를 출력
elem
# id가 query인 부분에 시가총액 글자 입력
elem.send_keys("시가총액")
# 글자입력후 enter키 입력
elem.send_keys(Keys.ENTER)

# requests, beautifulsoup 사용해서 정보를 가져옴.
# csv저장

# elem = browser.find_element_by_class_name("spnew ico_logo")
elem = browser.find_element_by_xpath("//*[@id='header_wrap']/div/div[1]/div[1]/div/h1/a")
elem.click()

elem = browser.find_element_by_id("query")
elem.send_keys("쿠팡")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_class_name("direct_link")
elem.click()



