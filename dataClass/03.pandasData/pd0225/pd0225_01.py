import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# df.loc['4번','학교'] = '단지고'
# # df.loc['4번',['학교','SW특기']] = ['단지고','python']
# print(df)

# 컬럼의 내용을 수정
# df['학교'] = df['학교'] + '등학교'
# print(df)

# astype 타입을 변경
# df['키'] = df['키'].astype(str)+'cm'
# print(df)

# 함수 : 입력의 타입을 변경(str) -> cm글자를 붙여서 리턴
def add_cm(height):
    return str(height)+'cm'

# apply함수호출 : int타입 -> str타입, cm붙여서 출력
df['키'] = df['키'].apply(add_cm)

# df['SW특기'] = df['SW특기'].str.lower()

# 글자가 들어오면 첫글자는 대문자, 그외 소문자 - capitalize
# 소문자 : lower, 대문자 : upper
def txtchange(lang):
    if pd.notnull(lang):
        return lang.capitalize()
    return lang

df['SW특기'] = df['SW특기'].apply(txtchange)
print(df)