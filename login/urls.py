from django.contrib import admin
from django.urls import path, include
from login import views2
urlpatterns = [
    path('', views2.IndexLogin, name="index"),
   
]
