import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 조건
print(df['키']>=185)

print(df['키'])

# 조건식
filterdata = df['키']>=185
# 조건에 맞는 row출력
print(df[filterdata])

# 조건에 맞지 않는 row출력
print(df[~filterdata])

# loc,iloc -> row출력
print(df.loc[filterdata])
print(df[filterdata])
print(df['1번':'3번'])
# print(df.iloc[0:3])
# print(df[0:3])

