# Generated by Django 3.1.6 on 2021-02-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, help_text='Paste in your Facebook profile URL here. Navigate to your profile and copy the URL displayed', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('prefer_not_to_say', 'Prefer Not To Say')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, help_text='Paste in your LinkedIn Profile URL. Navigate to your profile and copy the URL displayed', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, help_text='Enter your phone number. E.g 776887606', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, help_text="Enter your Twitter username without including the '@' character. E.g surveyor_jr", max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
