from django.contrib import admin
from cart.models import *

# Register your models here.
class custom_cart(admin.ModelAdmin):
    list_display = ['user','is_paid']
    ordering = ('id',)


class custom_cart_item(admin.ModelAdmin):
    list_display = ['cart','product','price','quantity']
    ordering = ('id',)


admin.site.register(Cart,custom_cart)
admin.site.register(CartItems,custom_cart_item)

@admin.register(Voucher)
class CustoomVoucher(admin.ModelAdmin):
    list_display = [
        'voucher_code','discount_type','discount_value'
    ]

