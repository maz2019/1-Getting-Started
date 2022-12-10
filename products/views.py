from django.shortcuts import render
from .models import Product

def ProductList(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'products/productlist.html', context)
