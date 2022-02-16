from selenium import webdriver
from selenium.webdriver.common.keys import Keys #키보드 관련 메소드

# 크롬드라이버 로딩 (예:driver)
browser = webdriver.Chrome()
# 페이지 이동
browser.get("http://www.naver.com")

# 페이지에서 class:link_login 것을 클릭
browser.find_element_by_class_name("link_login").click()
# 뒤로 가기 클릭
browser.back()
# 앞으로 가기 클릭
browser.forward()

# 페이지 다시 로딩
browser.refresh()

# 정보찾으려면, requests,beautifulsoup 
# 정보를 찾아서 csv 또는 text 저장

browser.get("http://www.daum.net")
# 브라우저에서 id를 선택
elem = browser.find_element_by_id("q")
# 해당 요소에 글자 입력
elem.send_keys("시가총액")
# 해당 요소의 글자를 삭제
browser.find_element_by_id("q").clear()
elem.send_keys("다음부동산")
# 해당 요소 enter키 입력
elem.send_keys(Keys.ENTER)


