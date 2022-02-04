from . import views
from django.urls import path

app_name=""
urlpatterns = [
    # http://127.0.0.1:8000/
    path('',views.index,name='index'),
]
