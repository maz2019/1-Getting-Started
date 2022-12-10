from django.shortcuts import render, reverse
from django.views import generic
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    template_name = "account/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse('account:login')
