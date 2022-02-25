import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
import pandas as pd
df = pd.read_excel('score.xlsx')

# x,y의 데이터
x=[1,2,3]
y=[2,4,8]

# plot : 선, bar: 막대그래프 데이터 넣어서 생성
plt.bar(x,y)
# plt.bar(df['이름'],df['키'])

# 상단 제목 생성
plt.title('라인그래프(Line graph)')

# 그래프 그려줌.
plt.show()