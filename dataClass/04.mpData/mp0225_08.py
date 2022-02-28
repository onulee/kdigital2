import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글적용
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15  # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False #-글자 출력가능
import pandas as pd
df = pd.read_excel('score.xlsx')

x=[1,2,3]
y=[2,4,8]

# figure그래프의 외형설정
# figsize:그래프 크기조정 dpi: 해상도, facecolor : 그래프 배경색지정
plt.figure(figsize=(10,5),facecolor='yellow')
# plt.figure(figsize=(10,5),dpi=200,facecolor='yellow')

plt.plot(df['이름'],df['국어'])
plt.plot(df['이름'],df['영어'])
plt.plot(df['이름'],df['수학'])

plt.show()