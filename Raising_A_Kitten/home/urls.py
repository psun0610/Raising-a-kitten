from django.urls import path
from . import views

app_name = 'rak'

urlpatterns = [
    path('', views.start, name='start'),
    path('/home', views.home, name='home')
]
