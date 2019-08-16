from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
from .models import Products,Order
from .forms import ProductForm,OrderForm
from django.contrib import messages


def home(request):


    return render(request,'home.html')


    
def product(request):

  product = Products.objects.all()

  if request.method == 'POST':
    form = ProductForm(request.POST,request.FILES)
    if form.is_valid():
      product = form.save(commit=False)
      form.save()
      return redirect('product')
  else:
    form = ProductForm()

  context ={
    'form':form,
    'product':product,
  }

  return render(request,'product.html',context)
  
def order(request):

  order = Order.objects.all()
  product = Products.objects.all()

  if request.method == 'POST':
    form = OrderForm(request.POST,request.FILES)
    if form.is_valid():
      order = form.save(commit=False)
      form.save()
      return redirect('order')
  else:
    form = OrderForm()

  context ={
    'form':form,
    'product':product,
    'order':order,
  }

  

  return render(request,'order.html',context)


def delete_product(request, id=None):

    product= get_object_or_404(Products, id=id)

    

    if request.method == "POST": 
        product.delete()
        messages.success(request, "Post successfully deleted!")
        return redirect("product")
    
    context= {'product': product,
              
              }
    
    return render(request, 'delete_product.html', context)

  