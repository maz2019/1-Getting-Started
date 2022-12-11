from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from leads.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='home-page'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/',  include('agents.urls', namespace="agents")),
    path('products/', include('products.urls', namespace='products')),
    path('accounts/', include('allauth.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
