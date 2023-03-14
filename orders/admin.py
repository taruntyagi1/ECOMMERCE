from django.contrib import admin
from orders.models import *

# Register your models here.
@admin.register(Orders)
class Order(admin.ModelAdmin):
    
    list_display = ['user','order_number','first_name','last_name','phone_number','email','country','state','total','payment_method','created_at']


@admin.register(Payments)
class Payment(admin.ModelAdmin):
    list_display = ['user','transaction_id','payment_method','amount']

@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ['user','payment','order','product','quantity','price']


    