from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.fun,name='fun'),
    path('advcals',views.advcals,name='advcals')
]
