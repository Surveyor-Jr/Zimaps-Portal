from django.urls import path
from . import views
from .views import  COVIDDetailView, COVIDListView, COVIDResultsView, MapCreateView, MapDetailView, MapListView, MapResultsView, NewsDetailView, NewsListView

urlpatterns = [
    path('', MapListView.as_view(), name='home'),
    path('map/<slug:slug>/', MapDetailView.as_view(), name='map-detail'),
    path('search/', MapResultsView.as_view(), name='map-results'),
    path('add-map/', MapCreateView.as_view(), name='add-map'),
    path('covid-19/', COVIDListView.as_view(), name='covid-home'),
    path('covid-19/resource/<slug:slug>/', COVIDDetailView.as_view(), name='covid-resource-detail'),
    path('covid-19/search/', COVIDResultsView.as_view(), name='covid-results'),
    path('covid-19/news/', NewsListView.as_view(), name='news-home'),
    path('covid-19/news/<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),
    # path('provinces/', views.provinces, name='province'),
    # path('incidents/', views.incidents, name='incidents'),
    # path('collector/',)
]
