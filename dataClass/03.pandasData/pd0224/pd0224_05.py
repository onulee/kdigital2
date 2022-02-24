import pandas as pd
df = pd.read_excel('202201_202201_연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관')
print(df)