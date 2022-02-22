import pandas as pd

data = {
    '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
    '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

# data pandas 2차원데이터로 변환
# df=pd.DataFrame(data)
# print(df)

# 컬럼을 지정해서 가져올수 있음. 컬럼의 순서를 변경할수 있음.
# df=pd.DataFrame(data,columns=['이름','국어','영어','수학','학교','키'])
# print(df)

#index를 추가해서 DataFrame변환
df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'],columns=['국어','영어','수학'])
print(df)
# index만 출력
print(df.index)

# index이름 지정
df.index.name='지원번호'
print(df)

# inplace=True를 해야 실제 반영이 됨.
# df.reset_index(inplace=True)
# print(df)
# index지정되어 있는 컬럼 삭제
df.reset_index(drop=True,inplace=True)
print(df)

# index 이름으로 지정
df.set_index('이름',inplace=True)
print(df)

# index 지정취소
df.reset_index(inplace=True)
print(df)

# index 키로 지정으로 해보세요.
df.set_index('키',inplace=True)
print(df)

df.reset_index(inplace=True)
print(df)







