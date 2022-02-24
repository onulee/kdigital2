# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
# 학년 컬럼 추가
df['학년']=[3,3,2,1,1,3,2,2]
# 컬럼 추가
df['총합'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']

print(df)

# 컬럼추가
df['결과'] = 'Fail'
print(df)
# 총합 점수가 400이상 인경우
fdata = df['총합'] > 400
# 총합 점수가 400이상이면 결과컬럼에 Pass 입력
df.loc[fdata,'결과'] ='Pass'
# df.loc[df['총합'] > 400,'결과'] ='Pass'
print(df)

# 컬럼부분을 수정
df.loc['4번','학교'] ='디지털고'
print(df)

# 삭제 컬럼-drop(columns-컬럼삭제), drop(index-row삭제)
df.drop(columns=['결과'],inplace=True)
print(df)

# 컬럼을 여러개 삭제
df.drop(columns=['국어','영어','수학'],inplace=True)
print(df)