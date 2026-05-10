from django.urls import path
from .views import ProductListView, CategoryListView, TagListView, ProductDetailView,product_detail,ProductNewView,index

# URL patterns for the products app
# these are included in the main market/urls.py with an empty prefix

urlpatterns = [
    # serves the main HTML page at http://127.0.0.1:8000/
    path('', index, name='index'),
    
    # query parameters:?search=keyword, search by name or description
    # ?category=1, filter by category ID
    # ?tags=1&tags=2, filter by one or more tag IDs
    
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/tags/', TagListView.as_view(), name='tag-list'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name= 'single-product'),
    path('api/products/<int:pk>/', product_detail, name = 'product-detail'),
    path('api/products/create', ProductNewView.as_view(), name= 'create-product')
]