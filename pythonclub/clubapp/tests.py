from django.test import TestCase
from django.urls import reverse
from .models import ProductType, Product, Review
from django.contrib.auth.models import User


#test for models

class ProductTypeTest(TestCase):
    def test_string(self):
        type=ProductType(productename='laptop')
        self.assertEqual(str(type),type.productname)
    
    def test_table(self):
        self.assertEqual(str(ProductType._meta.db_table),'producttype')

class ProductTypeTest(TestCase):
    def setUp(self):
        self.type=ProductType(productname='tablet')
        self.prod=Product(productname='Ipad',producttype=self.type, productprice=800.00)
    
    def test_string(self):
        self.assertEqual(str(self.prod),self.prod.productname)
    
    def test_type(self):
        self.assertEqual(str(self.prod.producttype),'tablet')

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(),40.00)
        
#tests for views

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=ProductType.objects.create(productname='laptop')
        self.prod=Product.objects.create(productname='product1', producttype=self.type, user=self.u, 
        productprice=500.00,productentrydate='2019-04-02', productdescription="some kind of laptop")
    
    def test_product_detail_success(self):
        response=self.client.get(reverse('productdetails', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)

     