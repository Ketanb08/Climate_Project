from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home,name="home"),
    path('contact', views.contact,name="contact"),
    path('services', views.services,name="services"),
    path('about', views.about,name="about"),
    path('login', views.loginUser,name="login"),
    path('logout', views.logoutUser,name="logout"),
    path('data',views.data,name="data"),
    path('setdata',views.setdata,name="setdata"),
]