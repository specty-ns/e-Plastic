from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("signup/",views.CustomerSignUp,name="signup"),
    path("adminsp/",views.AdminSignUp,name="adminsp"),
    path("register/",views.Register,name="register"),
    

]