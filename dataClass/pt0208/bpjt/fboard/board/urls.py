from . import views
from django.urls import path

app_name='board'
urlpatterns = [
    path('blist/',views.blist,name='blist'),
    path('bwrite/',views.bwrite,name='bwrite'),
    path('bwriteOk/',views.bwriteOk,name='bwriteOk'),
    path('<str:b_no>/bview/',views.bview,name='bview'),
    path('<str:b_no>/bmodify/',views.bmodify,name='bmodify'), 
    path('bmodifyOk/',views.bmodifyOk,name='bmodifyOk' ),  # 수정저장
]
