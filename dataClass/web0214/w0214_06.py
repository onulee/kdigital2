# s.t 정규표현식 형태
# match으로 비교
# start, sat, ssen, sin, son, sot
import re

m_list = ['start','sat','ssen','sin','son','sot']
p = re.compile('s.t')  #정규표현식
for m_word in m_list:
    m = p.match(m_word)
    if m:
        print("매칭성공")
        print(m.group()) 
        print(m.string) 
        print(m.start()) 
        print(m.end()) 
        print(m.span()) 
    else:
        print("매칭되지 않음")    