from django.db import models

# Create your models here.

# We need a model for products, categories and tags, that will be stored in the
# database and have fields acting as columns.
# Product only belongs to one category, while a product can have multiple tags

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits= 8, decimal_places= 2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name= 'products', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,related_name= 'products')
    
    def __str__(self):
        return self.name


    



    




