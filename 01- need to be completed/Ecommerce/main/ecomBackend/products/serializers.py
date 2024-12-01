from rest_framework import serializers
from .models import Products, Categories, Brand


class Categories_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ['created_at', 'updated_at', 'meta_data']


class Brand_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ['created_at', 'updated_at', 'meta_data']


class Products_Serializers(serializers.ModelSerializer):
    # brand = Brand_Serializers()
    # categories = Categories_Serializers(many=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())

    class Meta:
        model = Products
        exclude = ['created_at', 'updated_at', 'meta_data']
