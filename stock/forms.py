from django import forms
from .models import Brand,Category,Store,Products,Order
from django.forms import modelform_factory

class BrandForm(forms.ModelForm):
  '''
  New brand creation form
  '''

  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Brand Name'}))

  class Meta:
    model = Brand
    fields = ['name']


class CategoryForm(forms.ModelForm):
  '''
  New category creation form
  '''

  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Category Name'}))

  class Meta:
    model = Category
    fields = ['name']

class StoreForm(forms.ModelForm):
  '''
  New brand creation form
  '''

  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Store Name'}))

  class Meta:
    model = Store
    fields = ['name']


ProductForm = modelform_factory(Products, fields=("name", "price","quantity","brand","category"))

OrderForm = modelform_factory(Order, fields=("name", "address","phone","product"))