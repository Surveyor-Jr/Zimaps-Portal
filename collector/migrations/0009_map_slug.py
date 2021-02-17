# Generated by Django 3.1.6 on 2021-02-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0008_auto_20210213_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='slug',
            field=models.SlugField(blank=True, help_text='The name of the page you want displayed in the URL e.g https://zimaps.co.zw/map/[the-url-here]', null=True),
        ),
    ]