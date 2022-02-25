import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글적용
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15  # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False #-글자 출력가능
import pandas as pd
df = pd.read_excel('score.xlsx')
# score.xlsx파일을 읽어와서
# x값 : 이름, y값 : 국어로 해서
# 범례데이터, x,y축 이름 넣어서 출력하시오.


plt.title('국어성적그래프')
plt.xlabel('이름',color='purple',loc='right')
plt.ylabel('국어성적',color='purple',loc='top')
plt.plot(df['이름'],df['국어'],label='국어점수')
plt.legend(loc='upper left')

plt.show()
