from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("collectorindex/<int:pk>",views.CollectorIndexPage,name="collectorindex"),
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
    path("pproduct/",views.PProduct,name="pproduct"),
    path("allpproducts/<int:pk>",views.GetAllPProduct,name="allpproducts"),
    path("ppbutton/<int:pk>",views.PPUpdateButton,name="ppbutton"),
    path("ppupdate/<int:pk>",views.UpdateProduct,name="ppupdate"),
    path("deleteproduct/<int:pk>",views.DeleteProduct,name="deleteproduct"),
    path("rpallpro/",views.RPAllProduct,name="rpallpro"),
    path("rpclick/<int:pk>",views.RPButtonClick,name="rpclick"),
    path("rprequest/<int:pk>",views.RPButton,name="rprequest"),
    path("showpreq/",views.ShowPReq,name="showpreq"),
    path("rejectpro/<int:pk>",views.RejectProduct,name="rejectpro"),
    path("rproduct/",views.RProduct,name="rproduct"),
    path("addrproduct/<int:pk>",views.AddRProduct,name="addrproduct"),
    path("allrproducts/<int:pk>",views.GetAllRProduct,name="allrproducts"),
    path("showpro/",views.ShopProduct,name="showpro"),
    path("deleterproduct/<int:pk>",views.DeleteRProduct,name="deleterproduct"),
    path("rpbutton/<int:pk>",views.RPUpdateButton,name="rpbutton"),
    path("rpupdate/<int:pk>",views.UpdateRProduct,name="rpupdate"),
    path("prodesc/<int:pk>",views.ShowPro,name="prodesc"),
    path("compcheckout/",views.CompanyCheckOut,name="compcheckout"),
    path("alogin/",views.AdminLogin,name="alogin"),
    path("adminlogin/",views.ALogin,name="adminlogin"),
    path("adminbutton/<int:pk>",views.AButton,name="adminbutton"),
    path("dashboard/",views.Dashboard,name="dashboard"),
    path("showadmin/",views.SAdmin,name="showadmin"),
    path("adminupdate/<int:pk>",views.AUpdate,name="adminupdate"),
    path("addtocart/<int:pk>",views.AddCart,name="addtocart"), 
    path("showthecart/<int:pk>",views.ShowCart,name="showthecart"),  
    path("deletecart/<int:pk>",views.DelCart,name="deletecart"),
    path("updatecart/<int:pk>",views.UpdateCart,name="updatecart"),
    path("checkout/<int:pk>",views.CartCheckout,name="checkout"),
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
    path('otp/',views.OTP,name='otp'),
    path('otpverify/',views.VerifyOtp,name="otpverify"),
    path('requestaccept/<int:pk>',views.reqaccept,name="requestaccept"),
    path("logout/",views.Logout,name="logout"),
    path("sortplasticreq/",views.SortPlasticRequest,name="sortplasticreq"),
    path("scheduleorder/pickup",views.Schedule,name="scheduleorder"),
    path("pickuprequests/",views.ShowPickUp,name="pickuprequests"),
    path("pickupstatus/<int:pk>",views.PickUpStatus,name="pickupstatus"),
    path("data",views.CustData,name="custdata"),
    path("adddata/",views.AddData,name="adddata"),
    path("Reports/<int:pk>",views.Report,name="report"),
    path("rcdata",views.RCData,name="rcdata"),
]