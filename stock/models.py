from django.db import models


class Profile(models.Model):
   '''
   Holds user's profile data.
   '''

   name = models.CharField(max_length = 250)
   profile_photo = models.ImageField(upload_to = "images/")
   bio = models.TextField()
   

   def save_profile(self):
    self.save()
  
   def delete(self):
    Profile.objects.get(id = self.id).delete()
  
   def update(self,field,val):
    Profile.objects.get(id=self.id).update(field=val)
    

   def __str__(self):
      return self.name





class Products(models.Model):
  '''
  Holds the product info.
  '''

  ref_no = models.CharField(max_length = 250)
  desc = models.TextField(max_length=400)
  unit_price = models.PositiveIntegerField(default = 0)
  quantity = models.PositiveIntegerField(default = 0)
  unit_measure = models.CharField(max_length = 250)
  reorder_level = models.PositiveIntegerField(default = 0 )
  


  def save_prod(self):
    self.save()
  
  def delete_prod(self):
    Products.objects.get(id = self.id).delete()

  def edit_prod(self,new_prod):
     prod = Products.objects.get(id = self.id)
     prod.Products = new_prod
     prod.save()

  def __str__(self):
      return self.ref_no

class Order(models.Model):

  ref_no = models.CharField(max_length = 250)
  desc = models.TextField(max_length = 400)
  quantity = models.PositiveIntegerField(default = 0)
  date = models.CharField(max_length = 250 )


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




