from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):

    products = Product.objects.all()
    context = { 
        'page_title' : "This is the page title",
        'another_content' : "This is the another content",
        'products' : products
    }
    return render(request,'index.html',context)

def detail(request,product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(f"<h1>This is the page of {product.name} </h1>")