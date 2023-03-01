from django.urls import path
from accounts.views import *
from . import views

urlpatterns = [
    path('',UserView.as_view()),
   

]
