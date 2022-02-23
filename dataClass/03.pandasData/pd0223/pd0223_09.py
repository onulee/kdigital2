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

# and - & : and조건으로 검색
print(df[  (df['키']>=185) & (df['학교']=='구로고') ])

# or - | : or조건으로 검색
print( df[ (df['키']<170) | (df['키']>200) ] )

print(df.info())