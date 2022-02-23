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

# 조건
# print(df['키']>=185)

print(df.loc[~(df['키']>=185),['이름','학교','키']])
print(df[ ~(df['키']>=185)])

# print(df['키'])

# # 조건식
# filterdata = df['키']>=185
# # 조건에 맞는 row출력
# print(df[filterdata])
# print(df[df['키']>=185])

# 조건에 맞지 않는 row출력
# print(df[~filterdata])

# # loc,iloc -> row출력
# 
# print(df.loc[df['키']>=185,'이름'])
# print(df.loc['1번','이름'])
# print(df[filterdata])
# print(df['1번':'3번'])
# # print(df.iloc[0:3])
# print(df[0:3])





