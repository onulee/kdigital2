# index 이름지정
# df.index.name='목록'
import pandas as pd
df = pd.read_excel('stat_142801.xls',skiprows=2,nrows=2,index_col=0)
df.index.name='목록'
print(df)
print(df.index)
print(df.index.values)

# index이름을 변경
# df.rename(index={'출생아\xa0수':'출생아 수'},inplace=True)
df.rename(index={'출생아\xa0수':'출생아 수','합계\xa0출산율':'합계 출산율'},inplace=True)
# df.index.values[0]='출생아 수'
print(df.loc['출생아 수'])
print(df.index.values)

print(df)
print(df.T)


# print(df['출생아 수'])