import pandas as pd
# df = pd.read_excel('score.xlsx',index_col='지원번호')
df = pd.read_excel('pandas_code.xlsx')
# print(df)
print(df[['이름','수학']])

print(df.describe())
print(df[['영어','수학']].describe())

print(df.columns)
print(df.columns[0])
print(df['이름'])
print(df[df.columns[0]])

# 다른 폴더에 있는 경우 경로명을 입력하면 됨.
# df = pd.read_excel('C:/data1/score1.xlsx',index_col='지원번호')

# print(df['영어'])
# # print(df[['이름','키']])  #컬럼
# # print(df[0:3])
# # print(df.head(2))
# print(df.loc['1번'])