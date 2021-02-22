from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import default, slugify 
from PIL import Image
from users.models import Profile
from django_summernote.fields import SummernoteTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Service Categories'
        ordering = ('name',)


class Services(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False, max_length=130)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    intro = models.CharField(max_length=100, unique=True)
    pricing = models.IntegerField()
    detail = SummernoteTextField()
    image = models.ImageField(default='default.png', upload_to='services')
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE) # use self.request.user.id == to get id of current logged in user
    author  = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Services on Offer'
        ordering = ('name',)

    def save(self, *args, **kwargs):
        value = self.intro
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.slug})


class Project(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField(help_text="What was the project all about? Explain in detail")
    image = models.ImageField(default='default.png', upload_to='projects')
    url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = 'Previous Projects'