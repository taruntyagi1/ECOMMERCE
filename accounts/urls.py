from django.urls import path
from accounts.views import *

urlpatterns = [
    path('',UserView.as_view())
]
