from django.shortcuts import render, redirect
from django.http import HttpResponse
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

class HomeView(View, Blogs):
    def get(self, request):
        all = Product.objects.all()
        fAll = Product.objects.all()[:3]
        latest=Product.objects.all().order_by('-id')[:3]
        latest2=Product.objects.all().order_by('-id')[3:6]
        # latest = reversed(fAll)
        sAll = Product.objects.all()[4:7]
        lAll = Product.objects.all()[7:10]
        llAll = Product.objects.all()[2:5]
        slAll = Product.objects.all()[5:8]
        products = all
        category = Product.objects.all()
        unique_categories = Category.objects.values('name').distinct()
        for category in unique_categories:
            pass
        blog = Blogs.objects.all()[:3]
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
        fAll=Product.objects.all().order_by('-id')[:3]
        AAll = Product.objects.all()
        n = str(len(AAll))
        sAll = Product.objects.all().order_by('-id')[4:7]
        dAll = Product.objects.all()[5:11]
        return render(request, 'shop-grid.html', locals())
    


# class shopingCartView(View):
#     def get(self, request):
#         user = request.user
#         cart = Cart.objects.filter(user=user)
#         cart_totals = [item.linetotal() for item in cart]
#         return render(request, 'shoping-cart.html',  locals())

#     def post(self, request):
#         user = request.user
#         product_id = request.POST.get('prod_id')
#         product = get_object_or_404(Product, id=product_id)
#         # cart_item, created = Cart.objects.get_or_create(user=user, product=product)
#         created = Cart.objects.create(user=user, product = product)
#         cart_item = Cart.objects.filter(user=user)
#         context = {
#             'cart_item': cart_item,
#             'created': created, 
#         }
#         return render(request, 'shoping-cart.html', context)


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
    blog = Blogs.objects.all()
    # context = {"blog":blog}
    return render(request, 'blog.html', {'b':blog})

def blogDetails(request, pk):
    blog = Blogs.objects.get(pk=pk)
    user = request.user
    context = {"blog": blog, 'user': user}
    return render(request, 'blog-details.html', context)

def checkout(request):
    if request.method == 'POST':

        first_names = request.POST.get('first_name', '') 
        last_name = request.POST.get('last_name', '')
        country = request.POST.get('country', '')
        address = request.POST.get('address', '')
        local_address = request.POST.get('local_address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')

        user = request.user
        cart = Cart.objects.filter(user=user)

        for c in cart:
            Billing_Detailss(
                usr=user,
                f_name=first_names,
                l_name=last_name,
                cntry=country,
                adrs=address,
                lcl_adrs=local_address,
                cty=city,
                stte=state,
                zp=zip,
                phne=phone,
                emil=email,
                product=c.product,
                quantity=c.quantity,
            ).save()
            c.delete() 

        return redirect('home')


    return render(request, 'checkout.html', {}) 

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

# def cart(request):
#     if request.user.is_authenticated:
#         user = request.user
#         product_id = request.GET.get("prod_id")
#         product_quantity = request.GET.get("product_quantity")
#         product = Product.objects.get(id=product_id)
#         try:
#             cart_item = Cart.objects.get(user=user, product=product)
#             cart_item.quantity = product_quantity
#             cart_item.save()
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(user=user, product=product, quantity=product_quantity)
#             cart.save()
#             return redirect("/cart")
        
            
def cart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get("prod_id")
        product_quantity = int(request.GET.get("product_quantity", 1))  # Default to 1 if not provided
        product = Product.objects.get(id=product_id)

        # Try to update quantity if the item exists in the cart
        try:
            cart_item = Cart.objects.get(user=user, product=product)
            cart_item.quantity = product_quantity
            cart_item.save()
        # If it doesn't exist, create a new cart item
        except Cart.DoesNotExist:
            Cart.objects.create(user=user, product=product, quantity=product_quantity)

        # Redirect to the cart page after handling the request
        return redirect("/cart")
    
    # If the user is not authenticated, redirect them to a login page or some other appropriate response
    return redirect("/login")


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        
        subtotal = 0  # Initialize subtotal
        cart_product = [p for p in cart]  # Get all cart items for the current user

        if cart_product: 
            # Calculate the subtotal by adding all line totals
            for p in cart_product:
                p.linetotal = p.quantity * p.product.selling_price  # Calculate line total for each product
                subtotal += p.linetotal  # Add to the subtotal

            return render(
                request, 
                "shoping-cart.html", 
                {'cart': cart, 'subtotal': subtotal}  # Pass the calculated subtotal to the template
            )
    
    # If no cart items, redirect to an empty cart page
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
    messages.success(request, 'Congratulation for your subscriptions!')
    return redirect('home')

def fresh_meat(request):
    Productss = Product.objects.filter(department='Fresh Meat')
    name = Product.objects.filter(department="Fresh Meat")[:1]
    return render(request, 'Fresh_Meat.html', locals())

def vegetables(request):
    Productss = Product.objects.filter(department='Vegetables')
    name = Product.objects.filter(department="Vegetables")[:1]
    return render(request, 'Vegetables.html', locals())

def Fruit_Nut_Gifts(request):
    Productss = Product.objects.filter(department="Fruit & Nut Gifts")
    name = Product.objects.filter(department="Fruit & Nut Gifts")[:1]
    return render(request, 'Fruit_Nut_Gifts.html', locals())

def Fresh_Berries(request):
    Productss = Product.objects.filter(department="Fresh Berries")
    name = Product.objects.filter(department="Fresh Berries")[:1]
    return render(request, 'Fresh_Berries.html', locals())

def fastfood(request):
    Productss = Product.objects.filter(department="Fastfood")
    name = Product.objects.filter(department="Fastfood")[:1]
    return render(request, 'Fastfood.html', locals())

def Ocean_Foods(request):
    Productss = Product.objects.filter(department="Ocean Foods")
    name = Product.objects.filter(department="Ocean Foods")[:1]
    return render(request, 'Ocean_Foods.html', locals())

def Butter_Eggs(request):
    Productss = Product.objects.filter(department="Butter & Eggs")
    name = Product.objects.filter(department="Butter & Eggs")[:1]
    return render(request, 'Butter_Eggs.html', locals())

def Fresh_Onion(request):
    Productss = Product.objects.filter(department="Fresh Onion")
    name = Product.objects.filter(department="Fresh Onion")[:1]
    return render(request, 'Fresh_Onion.html', locals())

def Papayaya_Crisps(request):
    Productss = Product.objects.filter(department="Papaya & Crisps")
    name = Product.objects.filter(department="Papaya & Crisps")[:1]
    return render(request, 'Papayaya_Crisps.html', locals())

def Oatmeal(request):
    Productss = Product.objects.filter(department="Papaya & Crisps")
    name = Product.objects.filter(department="Papaya & Crisps")[:1]
    return render(request, 'Oatmeal.html', locals())

def Fresh_Bananas(request):
    Productss = Product.objects.filter(department="Fresh Bananas")
    name = Product.objects.filter(department="Fresh Bananas")[:1]
    return render(request, 'Fresh_Bananas.html', locals())

        
def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')  
        if query:
            products = Product.objects.filter(name__icontains=query)
            context = {
                'products': products, 
            }
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html', {'error': 'No query provided'})
    else:
        return render(request, 'search.html', {'error': 'Invalid request method'})
    

def Fast_Food(request):
    Productss = Product.objects.filter(category="Fast Food")[:1]
    return render(request, 'Fast_Food.html')

def Dried_Fruit(request):
    Productss = Product.objects.filter(category="Dried Fruit")[:1]
    return render(request, 'Dried_Fruit.html')

def Vegetables(request):
    Productss = Product.objects.filter(category="Vegetables")[:1]
    return render(request, 'Vegetables.html')

def Meat(request):
    Productss = Product.objects.filter(category="Meat")[:1]
    return render(request, 'Meat.html')

def Drink_Fruit(request):
    Productss = Product.objects.filter(category="Drink Fruit")[:1]
    return render(request, 'Drink_Fruit.html')

