import pandas as pd
df = pd.read_excel('202201_202201_연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관',usecols='B,E:O')
print(df)

# 0~9세,10~19세 2개의 컬럼 합으로
# 0~19세 컬럼을 만들어 출력하시오. 
# 숫자변경을 해야 함.
df['0~9세'] = df['0~9세'].str.replace(',','').astype(int)
df['10~19세'] = df['10~19세'].str.replace(',','').astype(int)

# 두 컬럼의 합을 구해서 컬럼을 추가
df['0~19세'] = df['0~9세'] + df['10~19세']
# list 형태 변환
cols = list(df.columns)
# cols[-1] :data -> list , cols[0:-1] : list
# list의 index로 변경하는 법
# 컬럼의 위치이동
df = df[[cols[-1]] + cols[0:-1] ]
df.columns[-1] = ''
print(df)