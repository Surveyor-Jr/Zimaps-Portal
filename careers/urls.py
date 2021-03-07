from django.urls import path
from . import views
from .views import  CategoryServices, ServiceCreateView, ServiceDeleteView, ServiceDetailView, ServiceListView, ServiceResultsView, ServiceUpdateView, UserServices

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    path('services/<slug:slug>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('services/<slug:slug>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('service/create-new/', ServiceCreateView.as_view(), name='add-service'),
    path('search/', ServiceResultsView.as_view(), name='service-results'),
    path('services-by/<str:username>', UserServices.as_view(), name='user-services'),
    path('service-category/<str:name>', CategoryServices.as_view(), name='category-services'),
]
