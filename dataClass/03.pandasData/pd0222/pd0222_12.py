import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)


# 데이터중에 숫자인경우 개수,평균,표준편차,최대값,최소값이 계산되어 출력
# print(df.describe())

# # 컬럼의 정보를 출력
# print(df.info())

# # 상위5개의 데이터만 출력, 숫자를 넣으면 숫자만큼 출력
# print(df.head(7))

# # 하위5개 데이터만 출력, 숫자를 넣으면 숫자만큼 출력
# print(df.tail(3))

# # 각컬럼을 list형태로 출력
# print(df.values)

# # 데이터의 index 출력
# print(df.index)

# 데이터의 column 출력, columns 주의할것
print(df.columns)

# 행,열(column,row)을 출력
print(df.shape)
print(df)








