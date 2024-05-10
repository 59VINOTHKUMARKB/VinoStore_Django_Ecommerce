from django.contrib import admin
from django.urls import path, include
from base.views import index,place_order
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),   
    path('index/', include('base.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('register/', views.register, name='register'),
    path('place_order/<int:product_id>/', views.place_order, name='place_order'),
    path('products_page/', views.products_page, name='products_page'),

]
