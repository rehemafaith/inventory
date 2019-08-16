from django import forms
from .models import Products,Order
from django.forms import modelform_factory




ProductForm = modelform_factory(Products, fields=("ref_no", "desc","unit_price","quantity","unit_measure","reorder_level"))

OrderForm = modelform_factory(Order, fields=("ref_no", "desc","quantity","date"))