from django.db import models



class Brand(models.Model):
  '''
  Holds the name of the brand
  '''

  name = models.CharField(max_length = 250)

  def save_brand(self):
    self.save()
  
  def delete_brand(self):
    Brand.objects.get(id = self.id).delete()

  def edit_brand(self,new_brand):
     bran = Brand.objects.get(id = self.id)
     bran.brand = new_brand
     bran.save() 


class Category(models.Model):
  '''
  Holds the name of the category
  '''

  name = models.CharField(max_length = 250)

  def save_cat(self):
    self.save()
  
  def delete_cat(self):
    Category.objects.get(id = self.id).delete()

  def edit_cat(self,new_category):
     cat = Category.objects.get(id = self.id)
     cat.category = new_category
     cat.save() 


class Store(models.Model):
  '''
  Holds the name of the store
  '''

  name = models.CharField(max_length = 250)

  def save_store(self):
    self.save()
  
  def delete_store(self):
    Store.objects.get(id = self.id).delete()

  def edit_store(self,new_store):
     sto = Store.objects.get(id = self.id)
     sto.store = new_store
     sto.save() 

class Products(models.Model):
  '''
  Holds the product info.
  '''

  name = models.CharField(max_length = 250)
  price = models.PositiveIntegerField(default = 0)
  quantity = models.PositiveIntegerField(default = 0)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  


  def save_prod(self):
    self.save()
  
  def delete_prod(self):
    Products.objects.get(id = self.id).delete()

  def edit_prod(self,new_prod):
     prod = Products.objects.get(id = self.id)
     prod.Products = new_prod
     prod.save()

  def __str__(self):
      return self.name

class Order(models.Model):

  name = models.CharField(max_length = 250)
  address = models.CharField(max_length = 250)
  phone = models.PositiveIntegerField(default = 0)
  product = models. ForeignKey( Products, on_delete=models.CASCADE)


  def save_order(self):
    self.save()
  
  def delete_order(self):
    Order.objects.get(id = self.id).delete()

  def edit_order(self,new_order):
     oda = Order.objects.get(id = self.id)
     oda.Order = new_order
     oda.save()

  def __str__(self):
      return self.name


