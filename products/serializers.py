from rest_framework import serializers

from .models import Category, Product, Tag

# Main purpose of serializer is to help reduce work of converting the data received in view.py into JSON
# using Meta to expose the set of fields as per the requirements.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)



    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category','created_at', 'updated_at', 'tags', 'stock', 'sku']
        read_only_fields = ['created_at', 'updated_at']

