from django.db import models
from django.contrib.auth.models import User
# Create your models here.


SIZE_CHOICE = (
    ('Large', 'Large'),
    ('Medium', 'Medium'),
    ('Small', 'Small'),
    ('Tiny', 'Tiny'),
)

DEPARTMENTS = (
    ('Fresh Meat', 'Fresh Meat'),
    ('Vegetables', 'Vegetables'),
    ('Fruit & Nut Gifts', 'Fruit & Nut Gifts'),
    ('Fresh Berries', 'Fresh Berries'),
    ('Ocean Foods', 'Ocean Foods'),
    ('Butter & Eggs', 'Butter & Eggs'),
    ('Fastfood', 'Fastfood'),
    ('Fresh Onion', 'Fresh Onion'),
    ('Papaya & Crisps', 'Papaya & Crisps'),
    ('Oatmeal', 'Oatmeal'),
    ('Fresh Bananas', 'Fresh Bananas'),
)


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='Category image', blank=True, null=True )
    parent = models.ForeignKey( 'self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Add to category'


class Product(models.Model):
    name = models.CharField(max_length=100, blank = False, null = False)
    selling_price = models.FloatField( blank=False, null=False)
    discount_price = models.FloatField( blank=True, null= True, default=0.00)
    size = models.CharField(choices=SIZE_CHOICE, max_length=100, blank=True, null=True)
    department = models.CharField(choices=DEPARTMENTS, max_length=200, blank=True, null=True)
    description = models.CharField(max_length=300, verbose_name='Short Description')
    Products_Infomation = models.TextField(max_length=1000, verbose_name='Product Information')
    category = models.ForeignKey( Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product Image')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}"
    
    def linetotal(self):
        return self.product.selling_price * self.quantity
    
class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.ImageField(upload_to='Project', blank=False, null=False)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"
    

class SUBSCRIBE(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

class Billing_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    local_address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.user.username}"
        
class Billing_Detailss(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100, blank=True, null=True)
    l_name = models.CharField(max_length=100, blank=True, null=True)
    cntry = models.CharField(max_length=10, blank=True, null=True)
    adrs = models.CharField(max_length=200, blank=True, null=True)
    lcl_adrs = models.CharField(max_length=200, blank=True, null=True)
    cty = models.CharField(max_length=200, blank=True, null=True)
    stte = models.CharField(max_length=100, blank=True, null=True)
    zp = models.CharField(max_length=50, blank=True, null=True)
    phne = models.CharField(max_length=20, blank=True, null=True)
    emil = models.EmailField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usr.username}"
    
#-----------------------------Start-----------------------------------------    
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='Blog')
    price = models.IntegerField()
    discount_price = models.IntegerField()
#-----------------------------End------------------------------------------------

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='Blog')

    def __str__(self):
        return self.title