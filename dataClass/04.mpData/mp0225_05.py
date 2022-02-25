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

# label 범례 출력
plt.plot(x,y,label='범례데이터')
# 범례는 legend구문을 넣어야 출력됨. loc='upper right'
# plt.legend(loc='upper right')
# 범례의 위치 : loc 숫자로 입력해도 가능
# plt.legend(loc=6)
plt.legend(loc=(0.5,0.8))
plt.show()


