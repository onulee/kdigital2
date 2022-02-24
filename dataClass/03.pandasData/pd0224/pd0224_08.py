# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# df.replace({'구로고':'영등포고'},inplace=True)
# print(df)

print(df.columns)
print(df[df.columns[0]])

# 컬럼명을 변경
# df.rename(columns={'이름':'name','학교':'school'},inplace=True)
# print(df)

# 전체 컬럼명을 변경할때 사용
# df.columns = ['name','school','grade'...........]

# 구로고,디지털고 + 고등학교를 입력해서 출력해보세요.
df['학교'] = df['학교']+'등학교'
print(df)

df['음악'] = 100
print(df)

df['총합'] =df['총합'] + 100
print(df)

# 키 + cm , astype타입을 변경
df['키'] = df['키'].astype(str) +'cm'
print(df)