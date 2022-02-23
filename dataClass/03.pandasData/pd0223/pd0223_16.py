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

# 이름으로 정렬
print(df.sort_values('이름'))
print(df.sort_values('이름',ascending=False))
# 영어점수 순차정렬, 수학점수 역순정렬
print(df.sort_values(['영어','수학'],ascending=[True,False]))

