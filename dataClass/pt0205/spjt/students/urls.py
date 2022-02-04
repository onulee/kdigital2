from . import views
from django.urls import path

app_name="students"
urlpatterns = [
    # http://127.0.0.1:8000/students/reg
    path('reg/',views.regStudent,name='reg'),
    # http://127.0.0.1:8000/students/regCon
    path('regCon/',views.regStuCon,name='regCon'),
    path('regAll/',views.regStuAll,name='regAll'),
]
