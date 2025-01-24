from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('search_verb/', views.search_verb, name="search-verbs"),
    
]