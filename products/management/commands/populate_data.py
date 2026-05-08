from django.core.management.base import BaseCommand
from products.models import Category, Tag, Product
import random

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Product.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()

        # Create Categories
        categories = ['Electronics', 'Furniture', 'Office Supplies', 'Networking', 'Tools']
        category_objects = []
        for name in categories:
            cat = Category.objects.create(name=name)
            category_objects.append(cat)
            self.stdout.write(f'Created category: {name}')

        # Create Tags
        tags = ['wireless', 'portable', 'office', 'heavy-duty', 'budget',
                'premium', 'new-arrival', 'sale', 'indoor', 'outdoor']
        tag_objects = []
        for name in tags:
            tag = Tag.objects.create(name=name)
            tag_objects.append(tag)
            self.stdout.write(f'Created tag: {name}')

        # Create Products
        products = [
            ('Wireless Keyboard', 'A compact wireless keyboard for office use', 49.99, 'Electronics'),
            ('Standing Desk', 'Adjustable standing desk for better posture', 299.99, 'Furniture'),
            ('Ethernet Cable', 'High speed ethernet cable 10ft', 12.99, 'Networking'),
            ('Power Drill', 'Cordless power drill with multiple bits', 89.99, 'Tools'),
            ('Stapler', 'Heavy duty stapler for office use', 14.99, 'Office Supplies'),
            ('Wireless Mouse', 'Ergonomic wireless mouse with long battery life', 39.99, 'Electronics'),
            ('Office Chair', 'Comfortable mesh office chair', 199.99, 'Furniture'),
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
            ('Tape Measure', '25 foot retractable tape measure', 12.99, 'Tools'),
        ]

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

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))