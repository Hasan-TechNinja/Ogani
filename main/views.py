from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from . form import CustomerRegistrationForm
from django.urls import reverse
from django.contrib import messages
from . models import Product,Cart

# Create your views here.

class HomeView(View):
    def get(self, request):
        all = Product.objects.all()
        fAll = Product.objects.all()[:3]
        sAll = Product.objects.all()[4:7]
        lAll = Product.objects.all()[7:10]
        llAll = Product.objects.all()[2:5]
        slAll = Product.objects.all()[5:8]
        return render(request, 'index.html', locals())
    
    
class shopDetailsView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sd = Product.objects.get(pk = pk)
            all = Product.objects.all()
            rl = Product.objects.filter(category=sd.category).exclude(pk=pk)
            return render(request, 'shop-details.html', locals())
        else:
            return redirect(f"{reverse('login')}?next={request.path}")

    
class shopGridView(View):
    def get(self, request):
        all = Product.objects.all()[:12]
        fAll = Product.objects.all()[:3]
        sAll = Product.objects.all()[4:7]
        dAll = Product.objects.all()[5:11]
        return render(request, 'shop-grid.html', locals())
    
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Cart

class shopingCartView(View):
    def get(self, request):
        # Define context explicitly
        context = {
            'user': request.user,
        }
        return render(request, 'shoping-cart.html', context)

    def post(self, request):
        user = request.user
        product_id = request.POST.get('prod_id')
        # Use get_object_or_404 to ensure the product exists
        product = get_object_or_404(Product, id=product_id)
        
        # Check if a similar entry already exists to avoid duplicates
        cart_item, created = Cart.objects.get_or_create(user=user, product=product)
        
        # Define context explicitly
        context = {
            'cart_item': cart_item,
            'created': created,  # True if new item added, False if already in cart
        }
        return render(request, 'shoping-cart.html', context)


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blogDetails(request):
    return render(request, 'blog-details.html')

def checkout(request):
    return render(request, 'checkout.html')

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'registration.html', locals())
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations Successfully registtration done')
        return render(request, 'registration.html', locals())
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('home')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        return redirect('/shopingCart')