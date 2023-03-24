from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializer import *
from twilio.rest import Client
import random
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class UserView(APIView):

    def get(self,request):
        
        user = User.objects.get(id = request.user.id)
        serializer = UserSerializer(user).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def post(self,request):

        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data , status=status.HTTP_201_CREATED)



account_sid = 'AC1a4aaf43b387dbc796498a466dff2f84'
auth_token = '9ac1e2a56e28dfd88e033838d8e657c3'
@csrf_exempt
def send_otp(request):
    if request.method == "POST":
        number = request.POST.get('phone_number')
        otp = random.randint(1000,9999)
        request.session['opt'] = otp
        client = Client(account_sid, auth_token)
        message = client.messages .create(
                        body="Your otp for login is {otp}",
                        from_='7906904898',
                        to=number
                    )