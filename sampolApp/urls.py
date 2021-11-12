



from django.contrib import admin
from django.urls import path
from sampolApp import views



urlpatterns = [
    path('loginTest', views.myIndexView.as_view(), name="my_index_view"),
    path('dashboard', views.myDashboardView.as_view(), name="my_dashboard_view"),
    path('contactUs', views.myContactUsView.as_view(), name="my_contactUs_view"),
    path('about', views.myAboutView.as_view(), name="my_about_view"),
    path('feature', views.myFeatureView.as_view(), name="my_feature_view"),
    path('login', views.LoginView.as_view(), name="my_login_view"),
    path('logout', views.logout_view, name="my_logout_view"),
    path('signup', views.mySignUpView.as_view(), name="my_signup_view"),  
    path('addUser', views.myAddUserView.as_view(), name="my_addUser_view"),
    path('addProduct', views.myAddProductView.as_view(), name="my_addProduct_view"),
    path('addType', views.myAddTypeView.as_view(), name="my_addType_view"),
    path('delete_customer/<str:username>', views.delete_customer, name="delete_customer"),
    path('delete_product/<int:item_code>', views.delete_product, name="delete_product"),
    path('delete_product_type/<int:type_code>', views.delete_product_type, name="delete_product_type"),
    path('edit_customer/<str:username>', views.edit_customer, name="edit_customer"),
    path('edit_product/<int:item_code>', views.edit_product, name="edit_product"),
    path('edit_menu_type/<int:type_code>', views.edit_product_type, name="edit_product_type"),
    path('add_to_cart/<int:item_code>', views.add_to_cart, name="add_to_cart"),
    path('remove_to_cart/<int:item_code>', views.remove_to_cart, name="remove_to_cart"),
    path('qtyCounter/<int:item_code>', views.qtyCounter, name="qtyCounter"),
    path('cart', views.myCartView.as_view(), name="my_cart_view"),
   
]