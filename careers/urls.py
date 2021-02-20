from django.urls import path
from . import views
from .views import  ServiceDetailView, ServiceListView

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
]
