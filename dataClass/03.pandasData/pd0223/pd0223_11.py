# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# filterdata = df[df.columns[0]] #컬럼의 index으로 출력
# 이름컬럼의 '강'으로 시작하는 row출력
filterdata = df['이름'].str.startswith('강')
print(df[filterdata])

# 이름컬럼의 '열'로 끝나는 row출력
fdata = df['이름'].str.endswith('열')
print(df[fdata])

# 수 글자가 포함되어 있는 row출력
fdata = df['이름'].str.contains('수')
print(df[fdata])

print(df)

langs = ['Python','Java']
# langs변수안의 글자가 있는지 확인해서 row출력
fdata = df['SW특기'].isin(langs)
# 2명 검색
# print(df[fdata])

langs = ['python','java']
fdata = df['SW특기'].str.lower().isin(langs)
# print(df[fdata])

# Nan 아무데이터가 없을때는 contains함수는 에러가 남.
# fdata = df['SW특기'].str.contains('Java')
# print(df[fdata])

# Nan 아무데이터가 없을때 na=True nan출력시켜줌, False는 출력하지 않음.
fdata = df['SW특기'].str.contains('Java',na=False)
print(df[fdata])


