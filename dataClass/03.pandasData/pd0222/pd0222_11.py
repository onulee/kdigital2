import pandas as pd
# 한글인코딩 2가지 방식, euc-kr:한국에만 적용, utf-8:전세계적 인코딩
df = pd.read_csv('월별_20220221.csv',encoding='euc-kr',skiprows=2)
print(df)