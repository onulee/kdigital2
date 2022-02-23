# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
df = pd.read_excel('202201_202201_연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관',usecols='B,E:O')

# index 0번째 출력
print(df.iloc[0])
# index 0번째 데이터값을 1,915,401 -> 1915401 ,를 삭제(replace)
df.iloc[0] = df.iloc[0].str.replace(',','').astype(int)
print(df.iloc[0])
print(df)

print(df['0~9세'])

