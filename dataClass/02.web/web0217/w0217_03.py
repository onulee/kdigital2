# 네이버증권 > 시가총액
# 1-50까지 글자를 엑셀해 보기

# 네이버 로그인을 해서 메일페이지까지 이동까지 하는 것을 해보세요.
#------------------
# 자기 자신의 메일로 정보를 발송하시오.
# horim159456@naver.com

import smtplib
from email.mime.text import MIMEText

# smtp서버명
smtpName = "smtp.naver.com"
# smtp port번호
smtpPort = 587
# 자신의 이메일
sendEmail = "onulee@naver.com"
# 자신의 비밀번호
password = "1111"
# 받는 사람의 이메일
recvEmail = "onulee@naver.com"

# 글자 보내기 제목,내용
title = "파이썬으로 이메일 보내기 확인"
content = "파이썬으로 이메일 보내기 합니다."

#MIME 객체
msg = MIMEText(content)
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title

# 메일 서버 정보 smtp.naver.com/587
s = smtplib.SMTP(smtpName , smtpPort)         
# 메일 서버 접근
s.starttls()    
# 메일 서버 로그인                            
s.login(sendEmail , password)   
# 메일 발송              
s.sendmail(sendEmail, recvEmail, msg.as_string()) 
# 메일 닫기
s.close()  




