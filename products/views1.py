from django.shortcuts import render
from products.models import *
from products.serializer import *
from category.serializer import *
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ProductView(APIView):
    
    def get(self,request):
        product = Product.objects.all().order_by('id')
        serializer = ProductSerializer(product,many = True).data
        return Response(serializer,  status=status.HTTP_200_OK)
    
    def post(request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)



class VariantView(APIView):

    def get(self,request,product_id):
        product = Product.objects.get(id=product_id)
        variant = Variant.objects.filter(product = product)
        serializer = VariantSerializer(variant).data
        return Response(serializer,status=status.HTTP_200_OK)
    

    def post(self,request):
        serializer = VariantSerializer(data  = request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)



