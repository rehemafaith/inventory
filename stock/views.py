from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Brand,Category,Store,Products,Order
from .forms import BrandForm,StoreForm,CategoryForm,ProductForm,OrderForm


def home(request):


    return render(request,'home.html')

def brand(request):
    brand = Brand.objects.all()

    if request.method == 'POST':
      form = BrandForm(request.POST,request.FILES)
      if form.is_valid():
        brand = form.save(commit=False)
        form.save()
        return redirect('brand')
    else:
      form = BrandForm()


    context = {
      'form':form,
      'brand':brand,
    }

    return render(request,'brand.html',context)



def categories(request):

    category = Category.objects.all()

    if request.method == 'POST':
      form = CategoryForm(request.POST,request.FILES)
      if form.is_valid():
        category = form.save(commit=False)
        form.save()
        return redirect('categories')
    else:
      form = CategoryForm()

    context ={
      'form':form,
      'category':category,
    }
    return render(request,'category.html',context)  



def stores(request):

    store = Store.objects.all()

    if request.method == 'POST':
      form = StoreForm(request.POST,request.FILES)
      if form.is_valid():
        store = form.save(commit=False)
        form.save()
        return redirect('stores')
    else:
      form = StoreForm()

    context ={
      'form':form,
      'store':store,
    }
    return render(request,'store.html',context)
    
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