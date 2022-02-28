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
# linewidth 선의 두께.
# marker 지점표시 o=둥근표시,v-삼각형,x-x표시
# markersize -> marker크기설정
# markerfacecolor->marker색, markeredgecolor-> marker테두리색
# linestyle 스타일 설정 None->없음, : - 점선, -- - dash긴점선 , -., - 실선
# alpha: 선의 투명도 조절
# plt.plot(df['이름'],df['국어'],linewidth=2, color='pink',  marker='o',markersize=10,markerfacecolor='yellow', markeredgecolor='red', linestyle='--', label='년도')
# plt.plot(df['이름'],df['영어'],linewidth=2, color='g', marker='o',ms=10,mfc='yellow', mec='red', ls='--', label='년도',alpha=0.4)
# plt.plot(x,y,linewidth=2, marker='o',markersize=10,markerfacecolor='yellow', markeredgecolor='red', linestyle='--', label='년도')
# plt.plot(x,y,linewidth=2, marker='o',ms=10,mfc='yellow', mec='red', ls='--', label='년도')
# line 스타일을 축약해서 사용가능 r-color,o-marker,-- - 선종류 
plt.plot(df['이름'],df['국어'],'ro--',markersize=4 )
plt.legend()
plt.show()


