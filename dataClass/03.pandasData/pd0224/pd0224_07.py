# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
# 컬럼을 삭제
# df.drop(columns=['총합'],inplace=True)
print(df)
# row를 삭제
# df.drop(index='4번',inplace=True)
# print(df)
# # row를 여러개 삭제
# df.drop(index=['5번','6번'],inplace=True)
# print(df)

# # 국어점수 60점 이하
# fdata = df['국어'] <= 60
# print(df[fdata])
# # 국어점수 60점 이하 인 index 삭제
# df.drop(index=df[fdata].index,inplace=True)
# print(df)
# 컬럼전체 list로 변경
cols = list(df.columns)
print(cols)
# 슬라이싱:list, 1개str->list변경해야 함.
df = df[cols[0:2]+[cols[9]]+cols[2:8]+cols[10:12]+[cols[8]] ]
print(df)

# 파일저장
df.to_excel('score.xlsx')
