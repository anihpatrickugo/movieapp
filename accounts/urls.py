from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    
    path('<str:username>/', profile_detail, name='profile_detail'),
    path('<str:username>/setting/', profile_setting, name='profile_setting')



]
