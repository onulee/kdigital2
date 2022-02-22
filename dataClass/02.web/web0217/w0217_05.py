import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtpName = "smtp.naver.com"
smtpPort = 587
sendEmail = "onulee@naver.com"
password = "1111"
# recvEmail = "onulee@naver.com"

title = "파이썬 파일 첨부"
content = "파이썬 이메일 파일 첨부 소스 코드입니다."

# list의 주소에 모두 이메일을 보내보세요.
recvEmails = ['horim159456@naver.com','vawav@naver.com','swaq11@naver.com','onulee@naver.com']

# for문 사용
for recvEmail in recvEmails:
    # MIME객체화
    msg = MIMEMultipart('alternative')
    # msg = MIMEText(content)
    # 내용부분
    part2 = MIMEText(content)
    msg.attach(part2)
    msg['From'] = sendEmail
    msg['To'] = recvEmail
    msg['Subject'] = title

    # 파일첨부
    part = MIMEBase('application',"octet-stream")
    # 파일 읽어오기
    with open("시가총액_20220216.csv","rb") as f:
        # part에 담기
        part.set_payload(f.read())
    # 파일 첨부할수 있는 형태로 인코딩
    encoders.encode_base64(part) 
    # header정보 정의
    part.add_header('Content-Disposition','attachment',filename="시가총액_20220216.csv")

    msg.attach(part)

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
   


