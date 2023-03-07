from django.urls import path
from frontapp import views

urlpatterns = [
    path('homeepgess/', views.homeepgess, name="homeepgess"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('OrderPAGE/', views.OrderPAGE, name="OrderPAGE"),
    path('TestimoniaPage/', views.TestimoniaPage, name="TestimoniaPage"),
    path('displayprdctPage/<itemCatg>', views.displayprdctPage, name="displayprdctPage"),
    path('ProductSinglee/<int:dataid>', views.ProductSinglee, name="ProductSinglee"),
    path('loginregister/', views.loginregister, name="loginregister"),
    path('savecostemerdetails/', views.savecostemerdetails, name="savecostemerdetails"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('chckoutpage/', views.chckoutpage, name="chckoutpage"),
    path('savecheckout/', views.savecheckout, name="savecheckout")
]