# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
df = pd.read_excel('pandas_code.xlsx')
print(df)

# 학교로 그룹, 학년 그룹해서 평균 출력을 해보세요.

print(df.groupby(['학교']).mean())

# 학교 그룹으로 해서 이름, sw특기 count출력
print(df.groupby('학교')['이름','sw특기'].count())

print(df.count())