from django.contrib import admin

from .models import Category, Product, Tag

# makes the admin panel prettier, more useful.

# adds categories to the admin page. we can search by the field, name.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


# adds tags to the admin page.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


# adds products to the admin page. We have filter the products using either category,
# tags and both. 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description')
    filter_horizontal = ('tags',)
    ordering = ('name',)
