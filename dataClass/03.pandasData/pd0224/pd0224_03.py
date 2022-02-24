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

# 컬럼의 데이터 수정
df['SW특기'].str.lower() # 소문자
df['SW특기'].str.upper() # 대문자

df['SW특기']  = df['SW특기'].str.lower()
print(df)

# 고등학교 글자 추가
df['학교']+'등학교'  # 구로고등학교, 디지털고등학교
print(df['학교']+'등학교')
df['학교'] = df['학교']+'등학교'
print(df)

# 컬럼이름으로 검색된 데이터에 모두저장, 등학교 삭제후 저장
df['학교'] = df['학교'].str.replace('등학교','')
print(df['학교'])
