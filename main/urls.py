from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . form import LoginForm

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
    path('accounts/login/', auth_views.LoginView.as_view(template_name="login.html", authentication_form = LoginForm), name = 'login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name = 'registration'),
    path('logout/', views.logout_user, name='logout'),
]
