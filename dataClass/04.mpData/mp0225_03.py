import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글적용
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15  # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False #-글자 출력가능

x=[1,2,3]
y=[192,194,198]

# label 축의 이름을 출력
# x축의 이름, loc=위치(left,center,right), 글자색지정
plt.xlabel('이름',loc='right',color='red')
# y의 이름, lic=위치(top,center,bottom)
plt.ylabel('키',loc='center',color='#ff0000')


# 그래프 y의 간격표시
plt.yticks([190,192,195,197,198,200])
# 그래프 x의 간격표시
plt.xticks([1,2,3])

# 상단의 title
plt.title("꺽은선 그래프")

plt.plot(x,y,label='A반 키크기')
plt.legend()
plt.show()