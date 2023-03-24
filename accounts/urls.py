from django.urls import path
from accounts.views import *
from . import views


urlpatterns = [
    path('',UserView.as_view()),
    path('verify_otp/',views.send_otp,name='verify_otp')
   

]
