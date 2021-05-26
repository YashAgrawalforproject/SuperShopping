from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('shop/about/', views.about, name="AboutUs"),
    path('shop/contact/', views.contact, name="ContactUs"),
    path('shop/tracker/', views.tracker, name="TrackingStatus"),
    path('shop/search/', views.search, name="Search"),
    path('shop/products/<int:myid>', views.productView, name="ProductView"),
    path('shop/checkout/', views.checkout, name="Checkout"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('shop/postReview', views.postReview, name="postReview"),



]
