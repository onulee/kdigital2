import requests

# res = requests.get("http://www.google.com")
res = requests.get("https://www.melon.com/")
# 200정상,  401권한없음, 404페이지없음, 500 서버에러
print("응답코드 : ",res.status_code) 

if res.status_code== 200:
    print("정상200 코드입니다.")
else:
    print("접근할수 없습니다. 응답코드 : ",res.status_code)    
    res.raise_for_status()  # 정상코드가 아니면 프로그램 종료
    print("실행이 확인")     # 실행이 안됨.


# with open("01_google.html","w",encoding="utf-8") as f:
#     f.write(res.text) 