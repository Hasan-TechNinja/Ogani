from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('shop_details/', views.shop_details, name='shop-details'),
    path('shop_grid/', views.shop_grid, name = 'shop-grid'),
    path('shoping_cart', views.shoping_cart, name = 'shoping-cart'),
    path('contact/', views.contact, name = 'contact'),
    path('blog/', views.blog, name = 'blog'),
    path('blog_details/', views.blog_details, name = 'blog-details'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('main/', views.main, name = 'main')
]
