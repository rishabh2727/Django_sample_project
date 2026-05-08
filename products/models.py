from django.db import models


# A category model/table for grouping the products into one category like Clothing etc.
# A product can only have one category.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

# using meta class here, so admin panel shows categories instead of categorys.
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Tags are labels that can be added to products. 
# One product can have multiple tags, even None.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# product is the main model that users will search and filter. 
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)

    def __str__(self):
        return self.name
