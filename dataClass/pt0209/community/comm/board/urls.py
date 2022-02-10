from . import views
from django.urls import include, path

app_name='board'
urlpatterns = [
    path('blist/', views.blist,name='blist'),                  # 게시판리스트
    path('bwrite/', views.bwrite,name='bwrite'),               # 글쓰기form
    path('bwriteOk/', views.bwriteOk,name='bwriteOk'),         # 글쓰기저장
    path('<str:b_no>/bview/', views.bview,name='bview'),       # 뷰페이지
    path('<str:b_no>/bmodify/', views.bmodify,name='bmodify'), # 수정form
    path('bmodifyOk/', views.bmodifyOk,name='bmodifyOk'),      # 수정저장
    path('<str:b_no>/bdelete/', views.bdelete,name='bdelete'), # 삭제
    path('<str:b_no>/breply/', views.breply,name='breply'),    # 댓글쓰기form
    path('breplyOk/', views.breplyOk,name='breplyOk'),         # 댓글쓰기저장
]
