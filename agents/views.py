import random
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizorAndLoginRequiredMixin

class AgentListView(OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    

    def get_queryset(self):
        company = self.request.user.userprofile
        user = self.request.user.is_agent
        queryset = Agent.objects.filter(company=company)
        queryset = queryset.filter(user__is_agent=True)
        return queryset


class AgentCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizor = False
        user.set_password(f"{random.randint(0,1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            company= self.request.user.userprofile
        )
        send_mail(
            subject="Your are invited to be and agent",
            message="Your were added as and Agent",
            from_email="admin@gmail.com",
            recipient_list=[user.email],
        )
        
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganizorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)


class AgentUpdateView(OrganizorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)


class AgentDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)