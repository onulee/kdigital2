import requests
import re

p = re.compile("ca.e") #정규표현식 형태 지정
m = p.match("careful")    # 매칭이 되었는지 확인

if m:
    print("매칭되었습니다.")
    print("m.group() 일치한 단어 출력 : ",m.group())   # 매칭 검사한 단어를 출력시켜줌.
    print("m.string 입력한 단어 출력 : ",m.string)   
    print("m.start() 일치하는 문자열의 시작 index : ",m.start())   
    print("m.end() 일치하는 문자열의 마지막 index : ",m.end())   
    print("m.span() 일치하는 문자열의 시작, 마지막 index : ",m.span())   
else:
    print("매치 되지 않음.")    




