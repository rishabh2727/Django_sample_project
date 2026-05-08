from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product, Category, Tag
from .serializers import ProductSerializer, CategorySerializer, TagSerializer


# index view serves the main HTML page to the browser
# this view doesn't touch the database at all
# it just returns the HTML page, and the page then calls the API endpoints using JavaScript

def index(request):
    return render(request, 'products/index.html')

# since we always want all the categories and tags we just set the queryset directly for them.
# return JSON

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# no custom logic is required. return JSON.

class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
# returns products as JSON with optional search and filtering
# supports searching by name/description, filtering by category,tags and both.

class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

# override get_queryset(), to define the custom logic.

    def get_queryset(self):
        
        # using select_related and prefetch_related to optimize the number of queries required.
        queryset = Product.objects.all().select_related('category').prefetch_related('tags')

        # read the search and filter values from the URL
        # for example: /api/products/?search=keyboard&category=2&tags=1&tags=3
        # .get() returns None if the parameter is not in the url.
        
        search = self.request.query_params.get('search', None)
        category = self.request.query_params.get('category', None)
        tags = self.request.query_params.getlist('tags', None)

        #  filter products where the name or description contains the search word.
        # icontains means case insensitive so 'Keyboard' and 'keyboard' both match
        # the | operator means OR, so it checks all three fields.
        if search:
            queryset = queryset.filter(
                description__icontains=search
            ) | queryset.filter(
                name__icontains=search
            ) | queryset.filter(
                category__name__icontains=search
            )

        # user selected a category from the dropdown.
        # filter products that belong to the category that user selected.
        if category:
            queryset = queryset.filter(category__id=category)

        # if the user checks one or more tags, we filter products that
        # have any of those the selected tags.
        # tags__id__in checks if the product's tag id is in the list of selected tag ids
        if tags:
            queryset = queryset.filter(tags__id__in=tags).distinct()

        return queryset.order_by('name')





