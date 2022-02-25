import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 그룹화 2개를 동시할때 학교 기준으로 1차 그룹,2차 학년으로 그룹 :  합계
# print(df.groupby(['학교','학년']).sum())
# print(df.groupby(['학교','학년']).mean())

# print(df.groupby(['학교','학년']).mean().sort_value('키'))

# 학교의 그룹으로 각학교별 이름컬럼 count해서 출력
print(df.groupby('학교')['이름'].count())
# Nan 부분은 count를 하지 않음.
print(df.groupby('학교')['SW특기'].count())
print(df.groupby('학교')['이름','SW특기'].count())