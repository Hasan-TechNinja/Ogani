from django.shortcuts import render

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

def registration(request):
    return render(request, 'registration.html')