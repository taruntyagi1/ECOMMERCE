from django.contrib import admin
from accounts.models import User,UserAddress

# Register your models here.
admin.site.register(User)


@admin.register(UserAddress)
class UserAddress(admin.ModelAdmin):
    list_display = ['user','address1','address2','address_type','country','state','city','pin_code']