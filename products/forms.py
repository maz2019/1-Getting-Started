from django import forms
from .models import Product, Category


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'category',
            'stock',
        )


class PCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
            'image',
            'parent',
        )