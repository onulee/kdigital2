import pandas as pd
# df = pd.read_excel('score.xlsx',index_col='지원번호')
df = pd.read_excel('pandas_code.xlsx')
# print(df.describe())

print(df['영어'].count())
print(df['sw특기'].count())

print(df['학교'].unique())  # 중복제거후 유일값 출력
print(df['학교'].nunique()) # 중복제거 후 유일값 개수 출력
print(df['학교'])

# 1개의 컬럼만 출력
# print(df['국어'].describe())
# print(df[['국어','영어']].describe())

# # 1개의 컬럼 최소값
# print(df['국어'].min())
# # 최대값
# print(df['국어'].max())

# # 상위 5개만 출력
# print(df['국어'].nlargest())

# # 하위 5개만 출력
# print(df['국어'].nsmallest())

# # 평균
# print(df['국어'].mean())

# # 합계
# print(df['국어'].sum())

# # 국어성적 리스트 개수
# print(df['국어'].count())
# print(df['SW특기'].count())

# # print(df)