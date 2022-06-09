from django.contrib import admin
from .models import Product
from .models import *


# Register your models here.

admin.site.site_header='SPIIDIFY DASHBOARD'
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','discount_price','category','description','image')
admin.site.register(Product,ProductAdmin)


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)