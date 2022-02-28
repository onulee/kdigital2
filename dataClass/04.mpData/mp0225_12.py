import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글적용
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15  # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False #-글자 출력가능
import pandas as pd
df = pd.read_excel('score.xlsx')

day=[1,2,3]
az=[2,4,8] #단위(만명)
pfizer=[5,1,3]
moderna=[1,2,5]

plt.plot(day,az,label='az',marker='o',markersize=7)
plt.plot(day,pfizer,label='pfizer',marker='o',markersize=7,linestyle='--')
plt.plot(day,moderna,label='moderna',marker='o',markersize=7,linestyle=':')
plt.legend(ncol=3)
plt.show()