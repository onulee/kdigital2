from email.mime.multipart import MIMEMultipart
import smtplib                             
from email.mime.text import MIMEText

smtpName = "smtp.naver.com"                  
smtpPort = 587                              

sendEmail = "onulee@naver.com"
password = "1111"
recvEmail = "onulee@naver.com"

title = "파이썬~~"                                
content = "안녕하세용"                                

# 메일 기본 정보 설정
msg = MIMEText(content)    
# msg = MIMEMultipart('alternative')                  
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title                   

s = smtplib.SMTP(smtpName , smtpPort)         
s.starttls()                                
s.login(sendEmail , password)                 
s.sendmail(sendEmail, recvEmail, msg.as_string()) 
s.close()  


# 파일 첨부
# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "파이썬_이메일_2일차"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "파이썬 코딩연습 (이메일보내기) 2일차 실습숙제"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 첨부파일 보내기
part = MIMEBase('application', "octet-stream")
with open("articles.xlsx", 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename="재난지원금기사.xlsx")
msg.attach(part)

# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())