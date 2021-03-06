from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to=True)
    website_url = models.CharField(max_length=50, null=True, blank=True)
    facebook_url = models.CharField(max_length=50, null=True, blank=True)
    twitter_url = models.CharField(max_length=50, null=True, blank=True)
    instagram_url = models.CharField(max_length=50, null=True, blank=True)
    youtube_url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)