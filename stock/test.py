from django.test import TestCase
from .models import Products,Order


class ProductTestClass(TestCase):

  def setUp(self):
      self.nbx214563= Products(ref_no = 'NBX214563', desc = 'Supa loaf brown bread', unit_price = '45', quantity = '25', unit_measure = 'pcs', reorder_level = '12')

      def test_instance(self):
        self.assertTrue(isinstance(self.bread,Products))

      def test_save_method(self):
        self.nbx214563.save_prod()
        products = Products.objects.all()
        self.assertTrue(len(products) > 0)



class OrderTestClass(TestCase):

  def setUp(self):
      self.nbx214563= Order(ref_no = 'NBX214563', desc = 'Supa loaf brown bread', quantity = '25', unit_measure = 'pcs', date = '12th July 2019')

      def test_instance(self):
        self.assertTrue(isinstance(self.nbx214563,Order))

      def test_save_method(self):
        self.nbx214563.save_prod()
        order = Order.objects.all()
        self.assertTrue(len(order) > 0)