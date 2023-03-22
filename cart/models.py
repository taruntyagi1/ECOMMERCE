from django.db import models
from products.models import *
from accounts.models import User
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True,blank = True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

class CartItems(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank = True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null = True,blank = True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null = True,blank = True)
    variant = models.ManyToManyField(Variant,blank  = True)
    price = models.IntegerField(null =True,blank = True)
    quantity = models.IntegerField(null=True,blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    discount_amount = models.CharField(max_length=1000,null = True,blank = True)

    
            


    def get_cart_total(self):
        user_id = self.user.id
        user = User.objects.get(id = user_id)
        cart = Cart.objects.get(user = user)
        cart_items = CartItems.objects.filter(user = user,cart = cart)
        total_price = 0
        for item in cart_items:
            total_price += item.price
            if item.discount_amount:
                total_price -= int(item.discount_amount)
        total_price = str(total_price)
        return total_price




VOUCHER_DISCOUNT = (
    ('Fixed', 'Fixed'),
    ('Percentage', 'Percentage'),
) 

class Voucher(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank = True)
    # cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null = True,blank = True)
    # cart_item = models.ForeignKey(CartItems,on_delete=models.CASCADE,null = True,blank = True)
    voucher_code = models.CharField(max_length=1000,null = True,blank = True)
    discount_type = models.CharField(max_length=1000,choices=VOUCHER_DISCOUNT,null = True,blank = True)
    discount_value = models.IntegerField(null = True,blank = True)
    min_value = models.IntegerField(null = True,blank = True)
    max_discount = models.IntegerField(null = True,blank = True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.voucher_code