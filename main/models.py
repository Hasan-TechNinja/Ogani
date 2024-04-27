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
        return str(self.id)