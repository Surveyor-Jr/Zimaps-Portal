# Generated by Django 3.1.6 on 2021-02-23 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('prefer_not_to_say', 'Prefer Not To Say')], max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, help_text='in the format: YYYY-MM-DD', null=True)),
                ('bio', models.TextField(default='Just a freelancer looking to earn some extra money by offering services', help_text='Help people get to know you better. Remember a good bio attracts me clients!')),
                ('phone_number', models.IntegerField(blank=True, help_text='Enter your phone number. E.g 776887606', null=True)),
                ('twitter', models.CharField(blank=True, help_text="Enter your Twitter username without including the '@' character. E.g surveyor_jr", max_length=20, null=True)),
                ('facebook', models.URLField(blank=True, help_text='Paste in your Facebook profile URL here. Navigate to your profile and copy the URL displayed', null=True)),
                ('linkedin', models.URLField(blank=True, help_text='Paste in your LinkedIn Profile URL. Navigate to your profile and copy the URL displayed', null=True)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
