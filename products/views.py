from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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

# no custom logic is required. return JSON

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
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

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
# field__lookup
# relation__field
# relation__field__lookup

        # user selected a category from the dropdown.
        # filter products that belong to the category that user selected.
        # the double underscore is django's way of going deeper into the related model
        if category:
            queryset = queryset.filter(category__id=category)

        # if the user checks one or more tags, we filter products that
        # have any of those the selected tags.
        # tags__id__in checks if the product's tag id is in the list of selected tag ids
        if tags:
            queryset = queryset.filter(tags__id__in=tags).distinct()
        
        # how we have to basically run the query where price is greater than equal to
        # that would translate to, price__gte
        # price is the field on the Products model, and we use a lookup called gte
        # that becomes price__gte
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
            

        return queryset.order_by('name')

# we use this view to just get one single product from the database. The user will input
# the id in the url, and drf automatically gets the id from there and filters the results
# we do not need to override the get_queryset()
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all().select_related('category').prefetch_related('tags')
    serializer_class = ProductSerializer
    
    
# same thing implemented in function based views:

# logic:
#     thinking process:

# have an api decorator, or otherwise check inside the function, it is a get request,
# so request.method should be equal to GET,
# otherwise we do not allow any other methods, and give error, with status code 405.

# next: we should have proper error handling, so we dont end up returning a server error.
# we have a try, except block for function based views in most of rhe cases. 

# then the data is passed as a parameter to the serializer, and we return the response
@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.select_related('category').prefetch_related('tags').get(pk=pk)
    except Product.DoesNotExist:
        return Response({"detail": "product does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)



# CreateAPIView handles POST requests. When data comes in, DRF passes
# it to the serializer which validates it — checking required fields exist,
# relationships point to real objects, data types are correct. 
# If validation passes, the serializer saves it to the database 
# and returns the created object with a 201 status. If validation fails,
# it returns the specific errors with a 400 status.
# One thing I had to think about was the serializer design — for 
# reading I use nested serializers to return full category and tag objects.
# But for writing I need separate fields that accept IDs — 
# so I added write_only fields that map to the same model fields
# using the source parameter."

    

class ProductNewView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# for function based views, we need to do many more steps, like
# annotating the function with the api decorator, 
# pass the incoming data to the serializer, and specifically run if serializer.isvalid method
# after that we save it to the database.
# then do error handling, and return proper status codes, like 201 for created.

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 201)
        
    return Response(serializer.errors, status=400)
    