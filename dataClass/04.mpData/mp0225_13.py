import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글적용
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15  # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False #-글자 출력가능
import pandas as pd
df = pd.read_excel('score.xlsx')


label = ['강나래','강태원','강호림']
values = [190,187,184]
colors=['red','blue','green']
# 막대그래프, colors list로 지정해서 사용가능
# 선의 두께조절
plt.bar(label, values,color=colors, width=0.2)

plt.show()