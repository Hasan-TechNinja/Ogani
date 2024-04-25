from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from . form import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def shopDetails(reqeust):
    return render(reqeust, 'shop-details.html')

def shopGrid(request):
    return render(request, 'shop-grid.html')

def shopingCart(request):
    return render(request, 'shoping-cart.html')

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