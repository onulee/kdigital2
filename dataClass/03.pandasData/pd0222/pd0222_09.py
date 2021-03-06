import pandas as pd
# data = {
#     '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
#     '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
#     '키' : [197, 184, 168, 187, 188, 202, 188, 190],
#     '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
#     '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
#     '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
#     '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
#     '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
#     'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
# }
# df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# df.index.name='지원번호'
# print(df)

# csv파일읽어오기
df=pd.read_csv('score.csv')
# df.set_index('지원번호',inplace=True)
print(df)

# 파일의 1번째 줄을 삭제하고 가져옴.
# df=pd.read_csv('score.csv',skiprows=1)
# print(df)

# 데이터의 1번째 데이터를 삭제하고 가져옴.
# nrows 는 현재출력하는 데이터 개수를 지정
# skiprows=3 3번째줄까지 삭제하고 가져옴, [1,3]=1번,3번 제외하고 가져옴.
# df = pd.read_csv('score.csv',skiprows=[1,3],nrows=3)
# print(df)

# txt파일은 구분자를 넣어서 가져옴.
# df = pd.read_csv('score.txt','\t')
# print(df)

# 엑셀파일 불러오기
# df = pd.read_excel('score.xlsx')
# print(df)

# # index 지원번호컬럼을 지정
# df.set_index('지원번호',inplace=True)
# print(df)

df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)


