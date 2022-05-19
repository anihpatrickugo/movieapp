"""tutorials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='index'),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='movie-detail'),
    path('upcoming/<slug:slug>/', UpcomingDetailView.as_view(), name='upcoming-detail'),
    path('about-us/', AboutView.as_view(), name='about-us'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    
]


