from . import views
from django.urls import include, path

app_name='blockhtml'
urlpatterns = [
    path('notice_list/', views.notice_list,name='notice_list'),
    
]
