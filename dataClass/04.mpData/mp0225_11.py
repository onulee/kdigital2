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
plt.figure(figsize=(5,3))
plt.plot(x,y,marker='o')
# plt.yticks([2,4,8,9])
# 좌표표시 위에 데이터 출력 ha:수평정렬(가운데정렬)
for idx,txt in enumerate(y):
    plt.text(x[idx],y[idx]+0.2,txt,ha='center',color='blue')

# 그래프 안내선 표시    
plt.grid(axis='x',linestyle='--',alpha=0.5,color='red')    
plt.grid(axis='y',linestyle='--',alpha=0.5,color='red')    
plt.show()