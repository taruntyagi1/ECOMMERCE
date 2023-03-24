from accounts.models import User
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.urls import reverse
from orders.models import *
from twilio.rest import Client
import random
from django.shortcuts import render,redirect



def send_verification_email(request,user):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    email_subject = "Activate  your account"
    message = render_to_string('activate.html',{
        'user' : user,
        'domain' : current_site,
        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
        'token' : default_token_generator.make_token(user),
        'password' : user.password
    })
    to_email = user.email
    email = EmailMessage(email_subject,message,from_email,to=[to_email])
    email.send()


def send_order_receive_email(request,user):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    email_subject = "Order Receive"
    order_item = OrderItem.objects.filter(user = request.user.id)
    message = render_to_string('order_receive.html',{
        'user' : user,
        'domain' : current_site,
        'order_item' : order_item
        
    })
    to_email = user.email
    email = EmailMessage(email_subject,message,from_email,to=[to_email])
    email.send()



        
    
