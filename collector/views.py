from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import COVID, News,  Map

class MapListView(ListView):
    model = Map
    template_name = 'index.html'
    context_object_name = 'maps'
    paginate_by = 10 # display 10 results on a single page

class MapDetailView(DetailView):
    model = Map

class MapResultsView(ListView):
    model = Map
    template_name = 'collector/map_results.html'
    paginate_by = 10 # display 10 results on a single page

    def get_queryset(self):
        query = self.request.GET.get('map')
        object_list = Map.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return object_list

class MapCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Map
    fields = ['name', 'description', 'embed_type', 'link', 'category']
    success_message = "The map has been successfully added to the portal."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class COVIDListView(ListView):
    model = COVID
    template_name = 'covid/home.html'
    context_object_name = 'covid'
    paginate_by = 10

class COVIDResultsView(ListView):
    model = COVID
    template_name = 'collector/covid_results.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('covid_resource')
        object_list = COVID.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return object_list

class COVIDDetailView(DetailView):
    model = COVID

class NewsListView(ListView):
    model = News
    context_object_name = 'news'
    paginate_by = 10

class NewsDetailView(DetailView):
    model = News


"""

**** for PostgreSQL****

def provinces(request):
    province = serialize('geojson', Provinces.objects.all())
    return HttpResponse(province, content_type='json')

def incidents(request):
    incident = serialize('geojson', Incidents.objects.all())
    return HttpResponse(incident, content_type='json')

"""
