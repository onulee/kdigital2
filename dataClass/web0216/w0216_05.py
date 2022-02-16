from selenium import webdriver
import time  # 시간 지연
import random  # 지연시간을 랜덤으로 처리
from selenium.webdriver.common.keys import Keys #키보드 관련 메소드
# 크롬 드라이버 연결
browser = webdriver.Chrome()
# 페이지 이동
browser.get("http://www.naver.com")
# class link_login 선택후 클릭
browser.find_element_by_class_name("link_login").click()

# 자바스크립트로 id,pw를 input에 입력해주는 명령어
input_js = 'document.getElementById("id").value="{id}"; document.getElementById("pw").value="{pw}";'.format(id="aaa",pw="1111")
# 3초동안 대기
time.sleep(3)
# 자바스크립트 구문 실행
browser.execute_script(input_js)
# 2초동안 대기
time.sleep(2)
browser.find_element_by_id("log.login").click()
