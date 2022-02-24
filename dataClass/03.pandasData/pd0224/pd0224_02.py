import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)

# print(df['학교'])
# # print(df['학교'].replace({'구로고':'단지고'},inplace=True))
# # 학교의 컬럼에서 구로고->단지고 변경, 디지털고->영등포고 변경
# print(df['학교'].replace({'구로고':'단지고','디지털고':'영등포고'},inplace=True))
# print(df['SW특기'].str.lower())

# # sw특기의 데이터를 소문자로 변경해서 저장
# df['SW특기'] = df['SW특기'].str.lower()
# print(df)


# '수'가 들어간 이름을 찾아보시오.
fdata = df['이름'].str.contains('수')
print(df[fdata])

# 영어점수 71점 이상인 사람을 출력하시오.
fdata = df['영어']>=71
print(df.loc[fdata])
# 이름이 '강'이들어가면서 수학점수 80점이상 사람을 출력하시오.
fdata = df['이름'].str.contains('강')
fdata2 = df['수학'] >= 80
print(df[fdata & fdata2])
# sw특기중 python,java인 사람을 출력하시오. 대소문자 구분 없음.
langs = ['python','java']
fdata = df['SW특기'].str.lower().isin(langs)
print(df[fdata])

# python 으로 contains 를 사용하려면 대소문자 구분없음 case=False
fdata = df['SW특기'].str.contains('python',case=False,na=False)
print(df[fdata])
