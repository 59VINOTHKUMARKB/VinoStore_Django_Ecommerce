# app_name/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'app_name'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('productdetails/', views.productdetails, name='productdetails'),
    path('account/', views.account, name='account'),
    path('games/', views.games, name='games'),
    path('about/', views.about, name='about'),
]
