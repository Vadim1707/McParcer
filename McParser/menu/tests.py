from rest_framework.test import APITestCase
from rest_framework import status
from .models import McFoodInfo


class ProductViewSetTests(APITestCase):

    def setUp(self):
        McFoodInfo.objects.create(name='product1', description="description")
        McFoodInfo.objects.create(name='product2', description="description")

    def test_get_object_exact_match(self):
        response = self.client.get('/api/products/product1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'product1')

    def test_get_object_not_exact_match(self):
        response = self.client.get('/api/products/uct1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'product1')

    def test_get_object_no_match(self):
        response = self.client.get('/api/products/long_product_name/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_object_field(self):
        response = self.client.get('/api/products/product1/description/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "description")

    def test_get_field_no_match(self):
        response = self.client.get('/api/products/product1/wrong_field/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
