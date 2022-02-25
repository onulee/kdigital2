import pandas as pd
data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)

print(df.sort_values('개봉 연도',ascending=False))
# print(df['개봉 연도'].sort_values())

fdata = df['평점'] > 9
print(df[fdata])

print(df.info())
# def txtchange(lang):
#     return str(lang)+'점'

# df['평점'] = df['평점'].apply(txtchange)
# print(df)

# df['평점'] = df['평점'].astype(str) + '점'
# print(df)

# 평점중에 평점 평균이상인 row만 출력하시오.
print(df['평점'].mean())
fdata = df['평점'] > df['평점'].mean()
print(df[fdata])