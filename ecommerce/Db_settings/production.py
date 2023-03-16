from ecommerce.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Ecommerce',
        'USER': 'postgres',
        'PASSWORD': 'tarunroot',
        'HOST': 'database-2.cvuk9hr7ijcp.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
       
    }
}