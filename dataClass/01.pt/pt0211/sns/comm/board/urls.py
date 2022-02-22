from . import views
from django.urls import include, path

app_name='board'
urlpatterns = [
    path('blist/',views.blist,name='blist'),
]
