import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')

print(df['이름']) # 컬럼의 이름으로 출력
print(df)
print(df.columns[0]) #컬럼의 index의 이름

print(df.columns[2])

print(df.columns[-1])

print(df['SW특기'])

# df.columns[-1] -> 이름을 가져와서 df[ ]안에 넣어줌.
print(df[df.columns[-1]])

# columns 출력
print(df['이름'])         #column index이름으로 출력
print(df[df.columns[-1]]) #column index번호로 출력

# row 출력
print(df.loc['1번']) #row index이름으로 출력
print(df.iloc[3])    #row index번호로 출력



