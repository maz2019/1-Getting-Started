from django.contrib import admin
from django.urls import path
from .views import ProductList

app_name = "products"

urlpatterns = [
    path('', ProductList, name='product-list'),
]
