from django.urls import path
from . import views

app_name='students'
urlpatterns = [
    path('reg/',views.regStudent,name='reg'),
    path('regCon/',views.regCon,name='regCon'),
    path('reglist/',views.reglist,name='reglist'),
    path('regview/',views.regview,name='regview'),
]
