from django.contrib import admin
from .models import FAQ, Services, Project, Category

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    '''Admin View for Service'''

    list_display = ('name', 'intro')
    list_filter = ('author', 'category') 
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    '''Admin View for Project'''

    list_display = ('name',)
    list_filter = ('author',)   
    search_fields = ('name', 'portfolio')
    ordering = ('name',)

admin.site.register(Category)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    '''Admin view for FAQ's'''

    list_display = ('question', 'answer')
