from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    
    path('shop/',views.shop_template),  
]
