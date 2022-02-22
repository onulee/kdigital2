from . import views
from django.urls import include, path

app_name="students"  #app별칭등록
urlpatterns = [
    path('reg/', views.regStudent,name='reg'),
    path('regCon/', views.regStuCon,name='regCon'),
]
