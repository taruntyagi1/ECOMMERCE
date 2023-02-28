from rest_framework import serializers
from category.models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'title','slug','image','description','created_at','updated_at'
        )