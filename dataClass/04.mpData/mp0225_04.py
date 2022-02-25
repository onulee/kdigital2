import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글적용
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15  # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False #-글자 출력가능
import pandas as pd
df = pd.read_excel('score.xlsx')
print(df['이름'])
print(df['국어'])
print(df['영어'])
print(df['수학'])
x=[1,2,3]
y=[2,4,8]
yy = [2,9,5] 
plt.title('학생성적그래프')
plt.plot(df['이름'],df['국어'],label='국어')
plt.plot(df['이름'],df['영어'],label='영어')
plt.plot(df['이름'],df['수학'],label='수학')
plt.legend()
plt.show()