from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password =None):

        user = self.model(
            email  = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password):

        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff =  True
        user.is_superuser = True
        user.set_password(password)
        user.save(using = self._db)
        return user
    
USER = 1
VENDOR = 2
USER_ROLES = (
    (USER , 'User'),
    (VENDOR, 'Vendor'),
)

class User(AbstractBaseUser):
    profile_image = models.ImageField(upload_to='photo/user',null = True,blank = True)
    first_name = models.CharField(max_length=100,null = True,blank = True)
    last_name = models.CharField(max_length=100, null = True, blank = True)
    username = models.CharField(max_length=200, unique = True,null = True,blank = True)
    email = models.EmailField(unique = True,null = True,blank = True)
    phone_number = models.CharField(max_length=13,unique=True, null = True,blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    role = models.IntegerField(choices=USER_ROLES,null = True,blank =  True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name','last_name','username']


    
    def __str__(self):
        return self.username
    
    
    def has_perm(self,perm,obj=None):
        return self.is_admin


    def has_module_perms(perms,app_label):
        return True
    

    def get_full_name(self):
        full_name =  self.first_name.capitalize() + " " + self.last_name.capitalize()
        return full_name
