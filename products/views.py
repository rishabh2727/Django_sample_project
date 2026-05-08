from django.shortcuts import render
from rest_framework.generics import ListAPIView
from models import Product, Category, Tag
from .serializers import ProductSerializer, CategorySerializer, TagSerializer


# Create your views here.

def index(request):
    return render(request, 'products/index.html')

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer





