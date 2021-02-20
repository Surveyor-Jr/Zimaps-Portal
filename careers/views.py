from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Services

class ServiceListView(ListView):
    model = Services
    template_name = 'careers/freelancers_home.html'
    context_object_name = 'services'
    paginate_by = 20

class ServiceDetailView(DetailView):
    model = Services