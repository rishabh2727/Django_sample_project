from django.test import TestCase
from django.urls import reverse

from .models import Category, Product, Tag


class ProductTests(TestCase):
    def setUp(self):
        self.school = Category.objects.create(name='School')
        self.home = Category.objects.create(name='Home')

        self.cheap = Tag.objects.create(name='cheap')
        self.useful = Tag.objects.create(name='useful')

        self.pen = Product.objects.create(
            name='Pen',
            description='Blue pen for school',
            price=5,
            category=self.school,
        )
        self.pen.tags.add(self.cheap, self.useful)

        self.desk = Product.objects.create(
            name='Desk',
            description='Small desk for home',
            price=10,
            category=self.home,
        )
        self.desk.tags.add(self.useful)

    def test_search_products(self):
        response = self.client.get(reverse('product-list'), {'search': 'school'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pen')
        self.assertNotContains(response, 'Desk')

    def test_filter_by_category(self):
        response = self.client.get(reverse('product-list'), {'category': self.home.id})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Desk')
        self.assertNotContains(response, 'Pen')

    def test_filter_by_tag(self):
        response = self.client.get(reverse('product-list'), {'tags': self.cheap.id})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pen')
        self.assertNotContains(response, 'Desk')

    def test_combine_search_category_and_tag(self):
        response = self.client.get(
            reverse('product-list'),
            {
                'search': 'school',
                'category': self.school.id,
                'tags': self.cheap.id,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pen')
        self.assertNotContains(response, 'Desk')
