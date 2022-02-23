import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 컬럼 전체출력
print(df.columns)
# index 전체출력
print(df.index)

# index의 이름으로 1개 출력
print(df.loc['1번'])
# index의 이름으로 여러개 출력
print(df.loc[['1번','3번','5번']])
# index 지정, 컬럼 지정해서 컬럼을 여러개 출력
print(df.loc['1번',['이름','키']])

# index 여러개, 컬럼도 여러개 출력
print(df.loc[['1번','3번'],['이름','국어']])

# index 슬라이싱 출력
print(df.loc['1번':'5번'])

print(df.loc['1번':'5번','이름':'영어'])
print(df.loc['1번':'5번','SW특기'])




# print(df['이름'])         #컬럼 이름으로 출력
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력