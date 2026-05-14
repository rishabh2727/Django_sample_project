from django.core.management.base import BaseCommand
from products.models import Category, Tag, Product
import random
# this is the management script, run this with 
# python manage.py populate_data
# we extend the basecommand class here, we have a handle function
class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        # clear existing data
        Product.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()

        # create Categories
        categories = ['Electronics', 'Furniture', 'Office Supplies', 'Networking', 'Tools','Misc']
        category_objects = []
        for name in categories:
            cat = Category.objects.create(name=name)
            category_objects.append(cat)

        # Create Tags
        tags = ['wireless', 'portable', 'office', 'heavy-duty', 'budget',
                'premium', 'new-arrival', 'sale', 'indoor', 'outdoor']
        tag_objects = []
        for name in tags:
            tag = Tag.objects.create(name=name)
            tag_objects.append(tag)

        # create products here, which are list of dictionary items, that we use.
        products = [
            ('Wireless Keyboard', 'compact wireless keyboard ', 50, 'Electronics'),
            ('Standing Desk', 'Adjustable standing desk for better posture', 21, 'Furniture'),
            ('Ethernet Cable', 'High speed ethernet cable 10ft', 3, 'Networking'),
            ('Power Drill', 'Cordless power drill with multiple bits', 20, 'Tools'),
            ('Stapler', 'Heavy duty stapler for office use', 14, 'Office Supplies'),
            ('Wireless Mouse', 'Ergonomic wireless mouse with long battery life', 35, 'Electronics'),
            ('Office Chair', 'Comfortable mesh office chair', 199, 'Furniture'),
            ('Network Switch', '8 port gigabit network switch', 45.99, 'Networking'),
            ('Hammer', 'Steel hammer with rubber grip', 19.99, 'Tools'),
            ('Printer Paper', 'A4 printer paper 500 sheets', 9.99, 'Office Supplies'),
            ('USB Hub', '7 port USB hub with power adapter', 34.99, 'Electronics'),
            ('Bookshelf', 'Wooden 5 tier bookshelf', 149.99, 'Furniture'),
            ('WiFi Router', 'Dual band wireless router', 79.99, 'Networking'),
            ('Screwdriver Set', 'Set of 12 screwdrivers', 24.99, 'Tools'),
            ('Sticky Notes', 'Pack of 10 colorful sticky note pads', 7.99, 'Office Supplies'),
            ('Monitor', '27 inch 4K display monitor', 399.99, 'Electronics'),
            ('Desk Lamp', 'LED desk lamp with adjustable brightness', 29.99, 'Furniture'),
            ('Cable Organizer', 'Cable management box for desk', 15.99, 'Office Supplies'),
            ('Laptop Stand', 'Adjustable aluminum laptop stand', 44.99, 'Electronics'),
            ('jacket', '', 45, 'Misc'),
            ('towel', 'white towel for shower', 12, 'Misc'),
            ('plates', 'dining plates', 12, 'Misc'),
            ('pillows', '', 2.99, 'Misc')
        ]

        # using loop to assign the dictionary elements to the objects created
        # for catrgory and tags
        for name, description, price, category_name in products:
            category = Category.objects.get(name=category_name)
            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                category=category
            )
            # Assign 2-3 random tags to each product
            random_tags = random.sample(tag_objects, random.randint(2, 3))
            product.tags.set(random_tags)
            self.stdout.write(f'Created product: {name}')
