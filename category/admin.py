from django.contrib import admin
from category.models import  *

# Register your models here.
class custom_category(admin.ModelAdmin):
    list_display = ['title','slug','created_at','updated_at']
    ordering = ('id',)

admin.site.register(Category,custom_category)