from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AgentAndOrgnizerAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated. and is Agent"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_agent or not request.user.is_organizor:
            return redirect('home-page')
        return super().dispatch(request, *args, **kwargs)

class OrganizorAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated. and is organizor"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizor:
            return redirect('home-page')
        return super().dispatch(request, *args, **kwargs)