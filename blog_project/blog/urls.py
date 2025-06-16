from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.detail, name='detail'),
    path('', views.index, name='index'),
]