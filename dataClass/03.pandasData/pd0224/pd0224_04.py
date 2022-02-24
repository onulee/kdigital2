# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)

# 컬럼전체에서 해당되는 컬럼만 변경
# df['학교'].replace({'구로고':'영등포고'})
# df['SW특기'] = df['SW특기'].str.lower()

# 컬럼이름 전체 출력
print(df.columns)
# 컬럼 추가
df['총합'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
print(df)
  
# 컬럼의 위치 변경
print(df[['이름','학교','총합']])  
print(df)
  
cols = list(df.columns)
# cols[-1] :data -> list , cols[0:-1] : list
# list의 index로 변경하는 법
df = df[[cols[-1]] + cols[0:-1] ]
# 컬럼의 이름을 나열해서 순서 변경
# df = df[['총합','이름','학교','키','국어','영어','수학','과학','사회','SW특기']]

# 학년 컬럼 추가
df['학년']=[3,3,2,1,1,3,2,2]
print(df)
