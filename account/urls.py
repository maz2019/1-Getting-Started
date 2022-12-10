from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
            LoginView,
            LogoutView,
            PasswordResetView,
            PasswordResetDoneView,
            PasswordResetConfirmView,
            PasswordResetCompleteView,
            )

from django.urls import path, include
from .views import SignUpView

app_name = "account"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('reset-pw/', PasswordResetView.as_view(), name='reset-pw'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),



    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
