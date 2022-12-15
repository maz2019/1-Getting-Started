from django.core.mail import send_mail
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import AgentAndOrgnizerAndLoginRequiredMixin, OrganizorAndLoginRequiredMixin, AgentAndLoginRequiredMixin
from django.views import generic
from .models import Lead, Category
from .forms import (
    LeadModelForm,
    AssignAgentForm,
    LeadCategoryUpdateForm,
    CategoryModelForm,
)


class LandingPageView(generic.TemplateView):
    template_name = "home.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizor:
            queryset = Lead.objects.filter(
                company=user.userprofile,
                agent__isnull=False
            )
        else:
            queryset = Lead.objects.filter(
                company=user.agent.company,
                agent__isnull=False
            )
            #filter for the agent is logged
            queryset = queryset.filter(agent__user=user)
        return queryset
        
    # def get_context_data(self, **kwargs):
    #     context = super(LeadListView, self).get_context_data(**kwargs)
    #     user = self.request.user
    #     if user.is_organizor:
    #         queryset = Lead.objects.filter(
    #             company=user.userprofile,
    #             agent__isnull=True
    #         )
    #     context.update({
    #         "unassigned_leads": queryset
    #     })
    #     return context

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizor:
            queryset = Lead.objects.filter(company=user.userprofile)
        else:
            queryset = Lead.objects.filter(company=user.agent.company)
            #filter for the agent is logged
            queryset = queryset.filter(agent__user=user)
        return queryset

class LeadCreateView(AgentAndOrgnizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self,form):
        lead = form.save(commit=False)
        lead.company = self.request.user.userprofile
        lead.save()
        send_mail(
            subject="A Lead has been created",
            message="Go to the Site",
            from_email="test&test.com",
            recipient_list=["test2&test.com"],
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(company=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(company=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")


class AssignAgentView(OrganizorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs
        
    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organizor:
            queryset = Lead.objects.filter(
                company=user.userprofile
            )
        else:
            queryset = Lead.objects.filter(
                company=user.agent.company
            )

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()
        })
        return context
    
    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organizor:
            queryset = Category.objects.filter(
                company=user.userprofile
            )
        else:
            queryset = Category.objects.filter(
                company=user.agent.company
            )
        return queryset

class CategoryCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/category_create.html"
    form_class = CategoryModelForm
    
    def get_success_url(self):
        return reverse("leads:category-list")
    
    def form_valid(self, form):
        category = form.save(commit=False)
        category.company = self.request.user.userprofile
        category.save()
        return super(CategoryCreateView, self).form_valid(form)

    
class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/category_detail.html"
    context_object_name = "category"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organizor:
            queryset = Category.objects.filter(
                company=user.userprofile
            )
        else:
            queryset = Category.objects.filter(
                company=user.agent.company
            )
        return queryset

class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_category_update.html"
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_success_url(self):
        return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})