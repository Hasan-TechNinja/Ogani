
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . form import LoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('/a/', views.home, name = 'home'),
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
    path('all/', views.all, name = 'all')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
