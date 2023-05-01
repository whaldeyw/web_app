from django.urls import path
from  . import views

urlpatterns = [
    path('', views.indexe, name='home'),
    path('about', views.about, name='about')
]