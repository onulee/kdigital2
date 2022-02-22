import pandas as pd

# 1~500번까지 삭제하고 501번째 부터 출력
df = pd.read_excel('pandas_code.xlsx',skiprows=[i for i in range(1, 500)],nrows=10)
# df = pd.read_excel('pandas_code.xlsx',skiprows=[1,2,3,4,....500],nrows=10)
# 500번만 지우고 1-10번까지 출력
df = pd.read_excel('pandas_code.xlsx',skiprows=[500],nrows=10)
print(df)


