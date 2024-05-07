from django.contrib import admin
from . models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'selling_price', 'discount_price', 'size', 'department', 'description', 'Products_Infomation', 'category', 'image', 'date')

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'parent')
admin.site.register(Category, CategoryAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
admin.site.register(Cart, CartAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')
admin.site.register(Project, ProjectAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email', 'message')
admin.site.register(Contact, ContactAdmin)

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email')
admin.site.register(SUBSCRIBE, SubscribeAdmin)

# class Billing_DetailsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'first_name', 'last_name', 'country', 'address', 'local_address', 'city', 'state', 'zip', 'phone', 'email')
# admin.site.register(Billing_Details, Billing_DetailsAdmin) 

class Billing_DetailssAdmin(admin.ModelAdmin):
    list_display = ('id', 'usr', 'f_name', 'l_name', 'cntry', 'adrs', 'lcl_adrs', 'cty', 'stte', 'zp', 'phne', 'emil', 'product', 'quantity')
admin.site.register(Billing_Detailss, Billing_DetailssAdmin)

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'long_description', 'date', 'comment', 'image')
admin.site.register(Blogs, BlogsAdmin)

