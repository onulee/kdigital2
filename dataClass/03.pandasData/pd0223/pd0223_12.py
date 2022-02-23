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

# 영어 60 이상,수학 60점 이상 출력하시오.
fdata = (df['영어']>=90) & (df['수학']>=90) 
print(df.loc[fdata,['이름','학교','영어','수학']])


# 이름이 ch 가 들어가는 사람을 출력하시오.

fdata = df['이름'].str.contains('Darcy')
print(df[fdata])