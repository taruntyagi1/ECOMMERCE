from django.contrib import admin
from products.models import *

# Register your models here.
class custom_product(admin.ModelAdmin):
    list_display = ['title','category','min_price','max_price','image','is_active']
    ordering = ('id',)

class custom_image(admin.ModelAdmin):
    list_display = ['product','image','is_active']
    ordering = ('id',)

class custom_variant(admin.ModelAdmin):
    list_display = ['product','variant_type','variant_value','is_active']
    ordering = ('id',)

admin.site.register(Product,custom_product)
admin.site.register(Variant,custom_variant)
admin.site.register(Product_images,custom_image)
