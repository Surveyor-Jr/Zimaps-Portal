# Generated by Django 3.1.6 on 2021-02-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0012_auto_20210214_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='link',
            field=models.TextField(help_text='Paste the embedding code depending on the platform on which the map is hosted on.', max_length=1000, verbose_name='URL'),
        ),
    ]