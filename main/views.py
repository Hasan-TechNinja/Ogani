from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def shop_details(reqeust):
    return render(reqeust, 'shop-details.html')

def shop_grid(request):
    return render(request, 'shop-grid.html')

def shoping_cart(request):
    return render(request, 'shoping-cart.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def checkout(request):
    return render(request, 'checkout.html')

def main(request):
    return render(request, 'main.html')