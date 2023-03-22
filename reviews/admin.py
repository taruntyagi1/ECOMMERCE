from django.contrib import admin
from reviews.models import *

# Register your models here.
@admin.register(ProductReviews)
class Custom_review(admin.ModelAdmin):
    list_display = ['user','product','review']
    ordering = ('id',)
