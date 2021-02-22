from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

GENDER_CHOICES = (
   ('female', 'Female'),
   ('male', 'Male'),
   ('prefer_not_to_say', 'Prefer Not To Say')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, help_text="in the format: YYYY-MM-DD")
    bio = models.TextField(default="Just a freelancer looking to earn some extra money by offering services", help_text="Help people get to know you better. Remember a good bio attracts me clients!")
    phone_number = models.IntegerField(help_text="Enter your phone number. E.g 776887606", null=True, blank=True)
    twitter = models.CharField(max_length=20, help_text="Enter your Twitter username without including the '@' character. E.g surveyor_jr", null=True, blank=True)
    facebook = models.URLField(help_text="Paste in your Facebook profile URL here. Navigate to your profile and copy the URL displayed", null=True, blank=True)
    linkedin = models.URLField(help_text="Paste in your LinkedIn Profile URL. Navigate to your profile and copy the URL displayed", null=True, blank=True)
    # age = models.IntegerField(editable=False, null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)   
   

"""
    def calculate_age(self):
        import datetime 
        calculated_age = datetime.date.today() - self.date_of_birth 
        self.age = calculated_age
                                                                       |==> Find a function that automatically calculates Age
    def save(self, *args, **kwargs):
        self.calculate_age()
        super(Profile, self).save(*args, **kwargs)

"""

