import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# index의 번호 출력
# print(df.iloc[0])
# print(df.iloc[3])
# index의 번호로 여러개 출력
print(df.iloc[[3,5]])
# index의 번호로 여러개이면서, 컬럼까지 지정해서 출력
print(df.iloc[[3,5],2])
# index의 번호로 여러개, 컬럼 여러개 지정해서 출력
# print(df.iloc[[1,5],[3,6]])
# # index의 번호 슬라이싱, 컬럼의 번호 슬라이싱해서 출력
# print(df.iloc[0:5,3:6])
# # index슬라이싱과 같음.
# print(df[0:5])
