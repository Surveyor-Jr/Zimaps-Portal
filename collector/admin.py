from django.contrib import admin
from .models import Incidents, Provinces, Districts, Category, Map, COVID, News
from django_summernote.admin import SummernoteModelAdmin
from leaflet.admin import LeafletGeoAdmin

class IncidentsAdmin(LeafletGeoAdmin):
    list_display = ['name', 'location']

class ProvincesAdmin(LeafletGeoAdmin):
    list_display = ['name_1', 'varname_1']

class DistrictsAdmin(LeafletGeoAdmin):
    list_display = ['name_2', 'varname_2']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class MapAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name', 'category']
    search_fields = ['name', 'category', 'link']
    radio_fields = {'embed_type': admin.VERTICAL}

class COVIDAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'embed_type']
    list_filter = ['name', 'embed_type']

class NewsAdmin(SummernoteModelAdmin):
    list_display = ['title', 'content']
    list_filter = ['source', 'source_url']
    search_fields = ['title', 'source']
    summernote_fields = ('content', )


admin.site.register(Incidents, IncidentsAdmin)
admin.site.register(Provinces, ProvincesAdmin)
admin.site.register(Districts, DistrictsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(COVID, COVIDAdmin)
admin.site.register(News, NewsAdmin)