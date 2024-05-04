
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . form import LoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.HomeView.as_view(), name = 'home'),
    path('shoDetails/<int:pk>/', views.shopDetailsView.as_view(), name='shopDetails'),
    path('shopGrid/', views.shopGridView.as_view(), name = 'shopGrid'),
    path('shopingCart/', views.shopingCartView.as_view(), name = 'shopingCart'),
    path('cart/', views.show_cart, name="showcart"),
    path('contact/', views.contact, name = 'contact'),
    path('blog/', views.blog, name = 'blog'),
    path('blogDetails/', views.blogDetails, name = 'blogDetails'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('main/', views.main, name = 'main'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="login.html", authentication_form = LoginForm), name = 'login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name = 'registration'),
    path('logout/', views.logout_user, name='logout'),
    path('meat/', views.Meat, name='meat'),
    path('project/', views.project, name='project'),
    path('subcribe/', views.project, name='subscribe'),
    path('fresh_meat/', views.fresh_meat, name = 'fresh_meat'),
    path('vegetables/', views.vegetables, name='vegetables'),
    path('fruit/', views.Fruit_Nut_Gifts, name='fruit'),
    path('Fresh_Berries/', views.Fresh_Berries, name='Fresh_Berries'),
    path('Fastfood/', views.fastfood, name='Fastfood'),
    path('Ocean_Foods/', views.Ocean_Foods, name='Ocean_Foods'),
    path('Butter_Eggs/', views.Butter_Eggs, name='Butter_Eggs'),
    path('Fresh_Onion/', views.Fresh_Onion, name='Fresh_Onion'),
    path('Papayaya_Crisps/', views.Fresh_Onion, name='Papayaya_Crisps'),
    path('Oatmeal/', views.Fresh_Onion, name='Oatmeal'),
    path('Fresh_Bananas/', views.Fresh_Onion, name='Fresh_Bananas'),
    path('search/', views.search, name = 'search'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
