import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글적용
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15  # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False #-글자 출력가능
import pandas as pd
df = pd.read_excel('score.xlsx')

# 파일저장, 출력도 하시오.
# 이름,국어 이름,영어
# marker o, --, x축이름 이름, y축이름 점수
# 범례 왼쪽 위에 표시해서 출력하시오.
plt.xlabel('이름',loc='right')
plt.ylabel('점수',loc='top')

plt.plot(df['이름'],df['국어'],linewidth=2, marker='o',markersize=10,linestyle='--',label='국어')
plt.plot(df['이름'],df['영어'],marker='o',markersize=10,linestyle='--',label='영어')
plt.legend(loc='upper left')
plt.show()

plt.savefig('score.png',dpi=200)

