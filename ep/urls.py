from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("collectorindex/",views.CollectorIndexPage,name="collectorindex"),
    path("index2/",views.Index2Page,name="index2"),
    path("signup/",views.CustomerSignUp,name="signup"),
    path("adminsp/",views.AdminSignUp,name="adminsp"),
    path("adminin/",views.AdminSignIn,name="adminin"),
    path("register/",views.Register,name="register"),
    path("signin/",views.CustomerSignIn,name="signin"),
    path("login/",views.LoginUser,name="login"),
    path("profile/",views.CustomerProfile,name="profile"),
    path("companyprofile/",views.CompanyProfile,name="compamyprofile"),
    path("profiledata/<int:pk>",views.CustomerProfileData,name="profiledata"),
    path("companydata/<int:pk>",views.CompanyProfileData,name="companydata"),
    path("updatebutton/<int:pk>",views.UpdateButtonClick,name="updatebutton"),
    path("cupdate/<int:pk>",views.CompanyUpdateClick,name="cupdate"),
    path("update/<int:pk>",views.UpdateData,name="update"),
    path("companyupdate/<int:pk>",views.CompanyUpdateData,name="companyupdate"),
    path("plasticCollectordata/<int:pk>",views.PlasticCollectorProfileData,name="plasticCollectordata"),
    path("plasticCollectorupdatebutton/<int:pk>",views.PlasticCollectorUpdateButtonClick,name="plasticCollectorupdatebutton"),
    path("plasticCollectorupdate/<int:pk>",views.PlasticCollectorUpdateData,name="plasticCollectorupdate"),
    path("addpproduct/<int:pk>",views.AddPProduct,name="addpproduct"),
    path("product/",views.Product,name="product"),
    path("allpproducts/<int:pk>",views.GetAllPProduct,name="allpproducts"),
    path("ppbutton/<int:pk>",views.PPUpdateButton,name="ppbutton"),
    path("ppupdate/<int:pk>",views.UpdateProduct,name="ppupdate"),
    path("deleteproduct/<int:pk>",views.DeleteProduct,name="deleteproduct"),
    path("rpallpro/",views.RPAllProduct,name="rpallpro"),
    path("rpclick/<int:pk>",views.RPButtonClick,name="rpclick"),
    path("rprequest/<int:pk>",views.RPButton,name="rprequest"),
    path("showpreq/",views.ShowPReq,name="showpreq")

]   