from django.contrib import admin

# Register your models here.

from .models import Product, Category, Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
