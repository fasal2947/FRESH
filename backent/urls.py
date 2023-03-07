from django.urls import path
from backent import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('saveaddadmin/', views.saveaddadmin, name="saveaddadmin"),
    path('displayadmin/', views.displayadmin, name="displayadmin"),
    path('editadmin/<int:dataid>/', views.editadmin, name="editadmin"),
    path('updateadmindata/<int:dataid>/', views.updateadmindata, name="updateadmindata"),
    path('deleteadmindata/<int:dataid>/', views.deleteadmindata, name="deleteadmindata"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('savecategorypage/', views.savecategorypage, name="savecategorypage"),
    path('displaycategoryfn/', views.displaycategoryfn, name="displaycategoryfn"),
    path('edtcategory/<int:dataid>/', views.edtcategory, name="edtcategory"),
    path('Updatecategorypage/<int:dataid>/', views.Updatecategorypage, name="Updatecategorypage"),
    path('Deletecategory/<int:dataid>/', views.Deletecategory, name="Deletecategory"),
    path('productpage/', views.productpage, name="productpage"),
    path('productsavepage/', views.productsavepage, name="productsavepage"),
    path('displayproductfn/', views.displayproductfn, name="displayproductfn"),
    path('editproductpage/<int:dataid>/', views.editproductpage, name="editproductpage"),
    path('updateproductdata/<int:dataid>/', views.updateproductdata, name="updateproductdata"),
    path('Deleteproduct/<int:dataid>/', views.Deleteproduct, name="Deleteproduct"),
    path('lognpagee/', views.lognpagee, name="lognpagee"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('logout/', views.logout, name="logout"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('displaycontactpage/', views.displaycontactpage, name="displaycontactpage"),
    path('Deletecontactpage/<int:dataid>/', views.Deletecontactpage, name="Deletecontactpage")
]