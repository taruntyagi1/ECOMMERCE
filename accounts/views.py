from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializer import *

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



