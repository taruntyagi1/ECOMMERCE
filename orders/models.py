from django.db import models
from accounts.models import User
from products.models import Product,Variant

# Create your models here.
STATUS  = (
    ("Accepted", 'Accepted'),
    ('Completed' , 'Completed'),
    ('Cancelled' , 'Cancelled')
)

PAYMENT = (
    ('Paypal',"paypal"),
    ("Stripe","Stripe"),
)

class Payments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True,blank = True)
    transaction_id = models.CharField(max_length=200,null = True)
    payment_method = models.CharField(max_length=200,null = True)
    amount = models.CharField(max_length=200,null = True)
    


    class Meta:
        verbose_name_plural = "Payment"


    def __str__(self):
        return self.transaction_id


    

class Orders(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    order_number = models.CharField(max_length=1000,null = True)
    payment = models.ForeignKey(Payments,on_delete=models.SET_NULL,null = True)
    first_name = models.CharField(max_length=100,null = True,blank = True)
    last_name = models.CharField(max_length=100,null = True,blank = True)
    phone_number = models.CharField(max_length=100,null = True,blank = True)
    email = models.EmailField(max_length=200,null = True)
    address = models.CharField(max_length=1000,null = True)
    country  = models.CharField(max_length=100,null = True)
    state = models.CharField(max_length=100,null = True)
    city = models.CharField(max_length=200,null = True)
    pin_code = models.CharField(max_length=200,null = True)
    total = models.CharField(max_length=100,null = True)
    payment_method = models.CharField(max_length=200, null = True)
    status = models.CharField(max_length=200,choices=STATUS,null = True)
    is_ordered = models.CharField(max_length=200,null = True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Orders"

    @property
    def Name(self):
        return self.first_name +" "+ self.last_name
    
    def __str__(self):
        return self.order_number
    


class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    payment = models.ForeignKey(Payments,on_delete=models.SET_NULL,null = True)
    order = models.ForeignKey(Orders,on_delete=models.SET_NULL,null = True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null = True)
    variant = models.ManyToManyField(Variant,null = True)
    quantity = models.IntegerField(null=True,blank = True)
    price = models.FloatField()
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.product.title
    

    class Meta:
        
        verbose_name_plural = "Order Item"