from django.db import models
from django.utils.text import slugify
import random

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=1000,null = True,blank = True)
    slug = models.SlugField(max_length=1000,null = True,blank = True)
    image = models.ImageField(upload_to='photo/category',null=True,blank = True)
    description = models.TextField(null=True,blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category,self).save(*args,**kwargs)