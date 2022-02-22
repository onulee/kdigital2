from . import views
from django.urls import include, path

app_name=""  #app별칭등록
urlpatterns = [
    path('', views.index,name='index'),
]
