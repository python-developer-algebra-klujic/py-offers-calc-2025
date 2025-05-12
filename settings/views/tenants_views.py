from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  UpdateView)
from ..models import Tenant


class TenantListView(LoginRequiredMixin, ListView):
    model = Tenant
    paginate_by = 10


class TenantDetailView(LoginRequiredMixin, DetailView):
    model = Tenant


class TenantUpdateView(LoginRequiredMixin, UpdateView):
    model = Tenant
    fields = '__all__'
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('settings:tenants')
