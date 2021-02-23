from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render
from django.db.models import Q 
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Services, FAQ
from users.models import Profile

class ServiceListView(ListView):
    model = Services
    template_name = 'careers/freelancers_home.html'
    context_object_name = 'services'
    paginate_by = 20

class ServiceDetailView(DetailView):
    model = Services

    def get_context_data(self, *args, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(*args, **kwargs)
        context['faq'] = FAQ.objects.all() # to fix-->Need to only show FAQ of that service 
        return context 

class ServiceCreateView(CreateView):
    model = Services
    fields = ['name', 'category', 'intro', 'pricing', 'detail', 'image']
    success_message = "Your services have been successfully added to the platform."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ServiceUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Services
    fields = ['name', 'category', 'intro', 'pricing', 'detail', 'image']
    success_message = "Your services have been updated successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        service = self.get_object()
        if self.request.user == service.author:
            return True
        return False

class ServiceDeleteView(UserPassesTestMixin, DeleteView):
    model = Services
    success_url = '/' #find a more convinient url to redirect to

    def test_func(self):
        service = self.get_object()
        if self.request.user == service.author:
            return True
        return False

class ServiceResultsView(ListView):
    model = Services
    template_name = 'careers/service_results.html'
    paginate_by = 20
    ordering = '-name'

    def get_queryset(self):
        query = self.request.GET.get('service')
        object_list = Services.objects.filter(Q(name__icontains=query) | Q(intro__icontains=query))
        return object_list

class UserServices(ListView):
    model = Services
    template_name = 'careers/user_services.html'
    context_object_name = 'services'
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Services.objects.filter(author=user).order_by('-name')
        


    