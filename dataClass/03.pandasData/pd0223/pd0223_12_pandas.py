# print(df['이름'])         #컬럼 이름으로 출력
# print(df.columns[0])        #컬럼명 : 이름
# print(df[df.columns[0]])  #컬럼 번호로 출력
# print(df[3:])               #df[컬럼] -> df[슬라이싱은 가능,index출력]
# print(df.loc['1번'])      #index 이름으로 출력
# print(df.iloc[0])         #index 번호로 출력
# print(df.iloc[0:3])         #index 슬라이싱 출력
import pandas as pd
df = pd.read_excel('pandas_code.xlsx')
print(df)

# 영어 60 이상,수학 60점 이상 출력하시오.
fdata = (df['영어']>=90) & (df['수학']>=90) 
print(df.loc[fdata,['이름','학교','영어','수학']])


# 이름이 ch 가 들어가는 사람을 출력하시오.

fdata = df['이름'].str.contains('Darcy')
print(df[fdata])

print(df)

# contains, isin 형태 2가지로 출력하시오.(대소문자 구분 없음)
# 이름에 to문자가 들어 있는 사람이면서,  sw특기가 python 인 사람을 출력하시오.

langs=['python']
fdata = df['sw특기'].str.lower().isin(langs)
print(df[fdata])

# case= False 대소문자 구분없이 to검색, case=True 대소문자 구분검색
namedata = df['이름'].str.contains('to', case=False)
print(df[namedata])
# print(df)

sdata = df['학교']=='단지고'

# & 먼저 처리하고 |를 처리함.
print(df[(fdata) & (namedata) & (sdata) ] )
# print(df[(fdata) | (namedata) & (sdata) ] )
# print(df[(fdata) & (namedata) | (sdata) ] )

 

