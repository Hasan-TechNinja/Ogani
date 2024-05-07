from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(SUBSCRIBE)
admin.site.register(Billing_Details)
admin.site.register(Billing_Detailss)
admin.site.register(Blogs)

class SUBSCRIBE(admin.ModelAdmin):
    list_display = ['id', 'email']
