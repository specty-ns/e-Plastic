from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("index2/",views.Index2Page,name="index2"),
    path("signup/",views.CustomerSignUp,name="signup"),
    path("adminsp/",views.AdminSignUp,name="adminsp"),
    path("register/",views.Register,name="register"),
    path("signin/",views.CustomerSignIn,name="signin"),
    path("profile/",views.CustomerProfile,name="profile"),
    path("login/",views.Login,name="login"),
    path("adminin/",views.AdminSignin,name="adminin"),
    path("profiledata/<int:pk>",views.ProfileData,name="profiledata"),
    path("update/<int:pk>",views.CustomerProfileUpdate,name="update"),
    path("edata/<int:pk>",views.UpdateData,name="edata"),
    path("ddata/<int:pk>",views.CustomerProfileDelete,name="ddata"),
    path("adata/<int:pk>",views.AdminProfile,name="adata"),    
    

    

]