import pandas as pd
# df = pd.read_excel('202201_202201_연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관',usecols='B,E:O')
df = pd.read_excel('202201_202201_연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관')
# df.set_index('행정기관',inplace=True)
print(df[0:3])
# 10~19세 컬럼을 출력해보세요.
print(df['10~19세'])
# 부산광역시 row만 출력해보세요.
# print(df.loc['부산광역시'])
# print(df.index)
# print(df.loc['부산광역시  '])
# rename - index이름을 변경
# df.rename(index={'부산광역시  ':'부산광역시'},inplace=True)
# index 이름 변경
df.index.values[2]='부산광역시'
# print(df.loc['부산광역시'])

# index이름 변경후 검색
print(df.columns)
# rename - columns이름을 변경
df.rename(columns={'0~9세':'9세'},inplace=True)
print(df.columns)

print(df[df.columns[-1]])
print(df.columns[-1])
print(df)