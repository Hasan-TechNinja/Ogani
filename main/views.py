from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from . form import CustomerRegistrationForm
from django.urls import reverse
from django.contrib import messages
from . models import *
from django.http import JsonResponse
from django.core.mail import send_mail

# Create your views here.

class HomeView(View):
    def get(self, request):
        all = Product.objects.all()
        fAll = Product.objects.all()[:3]
        fAll = reversed(fAll)
        sAll = Product.objects.all()[4:7]
        lAll = Product.objects.all()[7:10]
        llAll = Product.objects.all()[2:5]
        slAll = Product.objects.all()[5:8]
        products = all
        category = Product.objects.all()

        unique_categories = Category.objects.values('name').distinct()
       
        for category in unique_categories:
            # print(category['name'])
            pass

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

class shopingCartView(View):
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user)
        cart_totals = [item.linetotal() for item in cart]
        return render(request, 'shoping-cart.html',  locals())

    def post(self, request):
        user = request.user
        product_id = request.POST.get('prod_id')
        product = get_object_or_404(Product, id=product_id)
        # cart_item, created = Cart.objects.get_or_create(user=user, product=product)
        created = Cart.objects.create(user=user, product = product)
        cart_item = Cart.objects.filter(user=user)
        context = {
            'cart_item': cart_item,
            'created': created, 
        }
        return render(request, 'shoping-cart.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('emial')
        message = request.POST.get('message')
        user = request.user
        data = {'name': name, 'user':user, 'message': message}
        user_message = '''
        From: {}
        Name: {}
        Comment: {}
        '''.format(data['user'], data['name'], data['message'])
        send_mail("New message recive by Ogani", user_message, "",["hasantechninja@gmail.com"])
        contact_info = Contact(user=user, name=name, email=email, message=message)
        contact_info.save()
        messages.success(request, 'SMS Sent Successfully')
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
        # return render(request, 'shoping-cart.html', locals())
        return redirect('/cart')
    
def Meat(request):
    all = Product.objects.all()
    fAll = Product.objects.all()[:3]
    sAll = Product.objects.all()[4:7]
    lAll = Product.objects.all()[7:10]
    llAll = Product.objects.all()[2:5]
    slAll = Product.objects.all()[5:8]
    products = all
    pc = Category.objects.get(name = 'Meat')
    p = Product.objects.filter(category = pc)
    return render(request, 'Meat.html', locals())

def project(request):
    if request.user.is_authenticated:    
        subscribe = request.POST.get('subscribe')
    user = request.user
    data = SUBSCRIBE(user=user, email=subscribe)
    data.save()
    messages.success(request, 'Congratulation for your subcriptions!')
    return redirect('home')


