from django.urls import path
from . import views

app_name='students'  #app별칭   http://127.0.0.1:8000/students/reg
urlpatterns = [
    path('reg/',views.regStudent,name='reg'),
]
