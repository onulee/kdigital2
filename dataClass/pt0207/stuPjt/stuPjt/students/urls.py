from django.urls import path
from . import views

app_name='students'
urlpatterns = [
    path('reg/',views.regStudent,name='reg'),
    path('regCon/',views.regCon,name='regCon'),
    path('reglist/',views.reglist,name='reglist'),
    path('<str:name>/<str:major>/regview/',views.regview,name='regview'),
    path('<str:name>/regmodify/',views.regmodify,name='regmodify'),
    path('regmodifyCon/',views.regmodifyCon,name='regmodifyCon'),
    path('<str:name>/regdelete/',views.regdelete,name='regdelete'),
]
