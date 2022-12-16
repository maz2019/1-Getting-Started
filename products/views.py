from .models import Product, Category
from django.shortcuts import reverse 
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductModelForm, PCategoryModelForm
from core.mixins import OrganizorAndLoginRequiredMixin
from itertools import chain
from operator import attrgetter

class ProductListView(OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = "products/productlist.html"
    context_object_name = 'lists'

    def get_queryset(self):
        user = self.request.user
        queryset = {'products': Product.objects.all(), 
                    'category': Category.objects.all(),
        }
        return queryset


class ProductCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse ("products:product-list")


class ProductDetailView(OrganizorAndLoginRequiredMixin, generic.DetailView):
    template_name = "products/product_detail.html"
    context_object_name = "product"
    queryset = Product.objects.all()

class ProductUpdateView(OrganizorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "products/product_update.html"
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse ("products:product-list")


class ProductDeleteView(OrganizorAndLoginRequiredMixin,generic.DeleteView):
    template_name = "products/product_delete.html"
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse ("products:product-list")

class CategoryListView(OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = "products/categoty_list.html"
    context_object_name = "category"
    queryset = Category.objects.all()