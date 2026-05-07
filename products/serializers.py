from .models import Product, Category, Tag
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = ['id', 'name']
    
class TagSerializer(serializers.ModelSerializer):
    model = Tag
    fields = ['id', 'name']
    

# making the product serializer nested, so full details are returned.
class ProductSerializer(serializers.ModelSerializer):
    name = Product
    category = CategorySerializer()
    tags = TagSerializer()
    fields = ['id','name', 'price', 'description']








