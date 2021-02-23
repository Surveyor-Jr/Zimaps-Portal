from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
# from django.db.models import Manager as GeoManager
from django.urls import reverse 
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 

"""
class Incidents(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4396)
    objects = GeoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Incidences'

class Provinces(models.Model):
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    type_1 = models.CharField(max_length=50, null=True)
    engtype_1 = models.CharField(max_length=50, null=True)
    nl_name_1 = models.CharField(max_length=50, null=True)
    varname_1 = models.CharField(max_length=150, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name_1

    class Meta:
        verbose_name_plural = 'Provinces'

class Districts(models.Model):
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    id_2 = models.BigIntegerField()
    name_2 = models.CharField(max_length=75, null=True)
    type_2 = models.CharField(max_length=50, null=True)
    engtype_2 = models.CharField(max_length=50, null=True)
    nl_name_2 = models.CharField(max_length=75, null=True)
    varname_2 = models.CharField(max_length=150, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name_2

    class Meta:
        verbose_name_plural = 'Districts'

"""

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'

EMBED_CHOICES = (
   ('arcgis', 'ArcGIS'),
   ('google', 'Google'),
   ('openstreet', 'OpenStreet'),
   ('image', 'Image')
)

# a collection of maps 
class Map(models.Model):
    name = models.CharField(max_length=30, help_text="Place the map title here", unique=True)
    slug = models.SlugField(null=True, blank=True, editable=False, help_text="The name of the page you want displayed in the URL e.g https://zimaps.co.zw/map/[the-url-here]")
    description = models.TextField(help_text="Provide a brief description about your map, how it helps and what is being displayed")
    embed_type = models.CharField(choices=EMBED_CHOICES, max_length=50, null=True, blank=True)
    link = models.TextField(help_text="Paste the embedding code depending on the platform on which the map is hosted on.", verbose_name="URL", max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Maps'

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('map-detail', kwargs={'slug': self.slug})

class Bucketlist(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(help_text="Provide a detailed explanation about the map in order for the mappers to get a clear understanding of what you are looking for")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="To which category does this map belong to?")
    reference = models.URLField(null=True, help_text="Have you seen such a map elsewhere? If yes please provide a link to the source as this will also help the mappers visualize easily")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Maps BucketList'

RESOURCES_CHOICES = (
   ('dashboard', 'dashboard'),
   ('webapp', 'webapp'),
   ('webmap', 'webmap'),
   ('survey123', 'survey123'),
   ('repository', 'repository')
)

class COVID(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True, editable=False)
    description = models.TextField(help_text="The detailed description of the tool")
    embed_type = models.CharField(choices=RESOURCES_CHOICES, max_length=50, null=True, blank=True)
    link = models.TextField(max_length=1000)
    external_resource = models.URLField(null=True, blank=True, help_text="Specify the original link of the resource that you have just added to the list")

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = 'COVID-19 Resources'

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('covid-resource-detail', kwargs={'slug': self.slug})

class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, editable=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    source = models.CharField(max_length=100)
    source_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name_plural = 'COVID-19 News Feed'

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})