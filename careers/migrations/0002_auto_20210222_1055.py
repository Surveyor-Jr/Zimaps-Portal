# Generated by Django 3.1.6 on 2021-02-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='slug',
            field=models.SlugField(editable=False, max_length=130),
        ),
    ]