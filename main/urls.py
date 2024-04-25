from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('shoDetails/', views.shopDetails, name='shopDetails'),
    path('shopGrid/', views.shopGrid, name = 'shopGrid'),
    path('shopingCart', views.shopingCart, name = 'shopingCart'),
    path('contact/', views.contact, name = 'contact'),
    path('blog/', views.blog, name = 'blog'),
    path('blogDetails/', views.blogDetails, name = 'blogDetails'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('main/', views.main, name = 'main'),
    path('login/', views.login, name = 'login'),
    path('registration/', views.registration, name = 'registration')
]
