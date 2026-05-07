from .models import Item, Category, Tag
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = ['id', 'name']
    
class TagSerializer(serializers.ModelSerializer):
    model = Tag
    fields = ['id', 'name']
    

# making the item serializer nested, so full details are returned.
class ItemSerializer(serializers.ModelSerializer):
    name = Item
    category = CategorySerializer(read_only = True)
    tags = TagSerializer(many = True)
    fields = ['id','name', 'price', 'description']








