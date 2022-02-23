# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
import numpy as np
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 키높이로 정렬, 순차정렬
print(df.sort_values('키'))

# 키높이 역순정렬, ascending=False 역순정렬 됨.
print(df.sort_values('키',ascending=False))

# 첫번째 기준으로 먼저 정렬을 하고, 같은 값이 있을경우 그 다음것을 가지고 정렬
# print(df.sort_values(['수학','영어']))
print(df.sort_values(['수학','영어'],ascending=False))

# 수학-순차정렬, 영어-역순정렬
print(df.sort_values(['수학','영어'],ascending=[True,False]))

# index로 순차정렬
print(df.sort_index())

# index로 역순정렬
print(df.sort_index(ascending=False))