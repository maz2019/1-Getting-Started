from django.contrib import admin
from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryListView,
)

app_name = "products"

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/',ProductDeleteView.as_view(), name='product-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),

]
