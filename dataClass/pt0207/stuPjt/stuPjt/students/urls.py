from django.urls import path
from . import views

app_name='students'
urlpatterns = [
    path('reg/',views.regStudent,name='reg')
    
]
