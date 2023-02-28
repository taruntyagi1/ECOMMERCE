from rest_framework import serializers
from products.models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'title','slug','image','max_price','min_Price','description','created_at','updated_at','is_active'
        )


class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variant
        fields = (
            'title','slug','image','max_price','min_Price','description','created_at','updated_at','is_active'
        )