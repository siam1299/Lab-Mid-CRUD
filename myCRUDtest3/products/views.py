from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django .shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('Success!')
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'form.html', {'form': form})

def update_product(request, p_id):
    p = Product.objects.get(pk = p_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm(instance=p)
    return render(request, 'form.html', {'form' : form})

def delete_product(request, p_id):
    Product.objects.get(pk=p_id).delete()
    #return render(request,'home.html')
    return redirect('/')
