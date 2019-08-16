from django import forms
from .models import Products,Order
from django.forms import modelform_factory




ProductForm = modelform_factory(Products, fields=("ref_no", "desc","unit_price","quantity","unit_measure","reorder_level"))

OrderForm = modelform_factory(Order, fields=("ref_no", "desc","quantity","date"))

# class OrderForm(forms.ModelForm):
#    '''
#    To add an order
#    '''

#    STATUS = (
#       ('', 'Status'),
#       ('Unprocessed','Unprocessed'),
#       ('Processed','Processed'),
#       ('Pending','Pending'),
#    )

#    ref_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ref no'}))
#    desc =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Shortly Describe the product'}))
#    quantity = forms.IntegerField(widget = forms.IntegerField(attrs={'placeholder':'quantity'}))
#    date = forms.CharField(widget=forms.CharField(attrs={'placeholder':'date'}))
#    status = forms.ChoiceField(choices=STATUS,widget=forms.Select())

#    class Meta:
#       model = Post
#       fields = ['ref_no','desc','quantity','date','status']