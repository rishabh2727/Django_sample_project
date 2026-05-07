from django.contrib import admin

# Register your models here.

from .models import Item, Category, Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Item)
