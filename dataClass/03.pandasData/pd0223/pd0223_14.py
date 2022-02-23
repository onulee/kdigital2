# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
import numpy as np
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)
# nan데이터를 채울때 사용
print(df.fillna('없음'))

# dropna nan데이터를 지울때 사용
# nan 컬럼 1개만 있어도 row 삭제
# print(df.dropna(inplace=True))

# axis -> index:row삭제, columns:컬럼삭제
# how -> any:1개라도 nan있으면 삭제, all:모두 nan 일때 삭제
# print(df.dropna(axis='columns',how='any',inplace=True))
df['학교'] = np.nan
print(df)

# 학교 컬럼이 모두 nan이므로 삭제
print(df.dropna(axis='columns',how='all'))





