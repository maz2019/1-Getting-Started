from .models import Product, Category
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import OrganizorAndLoginRequiredMixin


class ProductListView(OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = "products/productlist.html"
    context_object_name = "products"
    queryset = Product.objects.all()

class ProductDetailView(OrganizorAndLoginRequiredMixin, generic.DetailView):
    template_name = "products/product_detail.html"
    context_object_name = "product"
    queryset = Product.objects.all()


class ProductUpdateView(generic.UpdateView):
    template_name = "products/product_update.html"
    queryset = Product.objects.all()

class ProductDeleteView(generic.DeleteView):
    template_name = "products/product_delete.html"
    queryset = Product.objects.all()

class CategoryListView(OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = "products/categoty_list.html"
    context_object_name = "category"
    queryset = Category.objects.all()