# app_name/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'app_name'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('product/', views.product_list, name='product_list'),
    path('product/', views.product, name='product'),
    path('product/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('productdetails/', views.product_list2, name='product_list2'),
    path('productdetails/', views.productdetails, name='productdetails'),
    path('productdetails/add_to_order/', views.add_to_order, name='add_to_order'),
    path('productdetails2/', views.product_list3, name='product_list3'),
    path('productdetails2/', views.productdetails2, name='productdetails2'),
    path('productdetails2/add_to_order/', views.add_to_order, name='add_to_order'),
    path('productdetails3/', views.product_list4, name='product_list'),
    path('productdetails3/', views.productdetails3, name='productdetails3'),
    path('productdetails3/add_to_order/', views.add_to_order, name='add_to_order'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.custom_login, name='login'),
    path('games/update_rewards_table/', views.update_rewards_table, name='update_rewards_table'),
    path('games/', views.games, name='games'),
    path('games/update_rewards_table/', views.update_rewards_table, name='update_rewards_table'),
    path('about/', views.about, name='about'),
    path('logout/', views.custom_logout, name='logout'),
    path('get_cart_items/',views.get_cart_items, name='get_cart_items'),
    
]
