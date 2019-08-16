from django.shortcuts import render
from django.http  import HttpResponse
from .models import Brand,Category,Store,Products,Order
from .forms import BrandForm,StoreForm,CategoryForm


def home(request):


    return render(request,'home.html')

def brand(request):

    if request.method == 'POST':
      form = BrandForm(request.POST,request.FILES)
      if form.is_valid():
        brand = form.save(commit=False)
        form.save()
        return redirect('home')
    else:
      form = BrandForm()


    return render(request,'brand.html',{'form':form})