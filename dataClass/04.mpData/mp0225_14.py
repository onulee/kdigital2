import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글적용
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15  # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False #-글자 출력가능
import pandas as pd
df = pd.read_excel('score.xlsx')

plt.bar(df['이름'],df['국어'])
plt.xticks(df['이름'],rotation=45)

plt.show()