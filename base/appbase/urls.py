from django.urls import path
from . import views

app_name = 'appbase'
urlpatterns = [
    path('', views.index, name='index')]