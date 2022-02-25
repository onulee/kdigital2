import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 그룹-학교: 디지털고
print(df.groupby('학교').get_group('디지털고'))
print(df.groupby('학교').get_group('구로고'))

# 그룹으로 평균
print(df.groupby('학교')['키'].mean())
# 그룹으로 크기
print(df.groupby('학교')['키'].size()['구로고'])
# 학교별 그룹에서 구로고 학생의 인원수
# print(df.groupby('학교')['키'].size()['구로고'])

# 학년으로 그룹을 해서 키의 평균으로 정렬
print(df.groupby('학년').mean().sort_values('국어',ascending=False))