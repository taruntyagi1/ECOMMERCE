from django.db import models
from category.models import *
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=1000,null = True,blank = True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null = True,blank = True)
    slug = models.SlugField(max_length=1000,null = True,blank = True)
    image = models.ImageField(upload_to='photo/product',null=True,blank = True)
    max_price = models.IntegerField(null = True,blank = True)
    min_price = models.IntegerField(null = True,blank = True)
    description = models.TextField(null=True,blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
    
  
VARIANT_CHOICES = (
    ('Color' , 'Color'),
    ('Size' , 'Size'),
)
    

class Variant(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null = True,blank = True)
    max_price = models.IntegerField(null = True,blank = True)
    min_price = models.IntegerField(null = True,blank = True)
    variant_type = models.CharField(max_length=200,choices=VARIANT_CHOICES,null = True,blank = True)
    variant_value = models.CharField(max_length=200,blank=True,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.variant_type} {self.variant_value}'



class Product_images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null = True,blank = True)
    image = models.ImageField(upload_to='photo/product_images',null = True,blank = True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.product.title
