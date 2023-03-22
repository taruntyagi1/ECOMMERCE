from django.db import models
from accounts.models import *
from products.models import *

# Create your models here.

class ProductReviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null = True)
    review = models.TextField(blank = True,null = True)


    class Meta:
        verbose_name_plural = "Reviews"


    def __str__(self):
        return self.review
    
