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


    