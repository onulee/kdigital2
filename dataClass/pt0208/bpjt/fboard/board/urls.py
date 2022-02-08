from . import views
from django.urls import path

app_name='board'
urlpatterns = [
    path('blist/',views.blist,name='blist' ),
]
