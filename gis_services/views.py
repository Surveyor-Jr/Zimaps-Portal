from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    template_name = "gis_services/home.html"
