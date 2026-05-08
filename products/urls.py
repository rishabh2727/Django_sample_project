from django.urls import path
from .views import ProductListView, CategoryListView, TagListView, index

urlpatterns = [
    path('', index, name='index'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/tags/', TagListView.as_view(), name='tag-list'),
]