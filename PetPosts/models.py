from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PetPost(models.Model):
    title                = models.CharField(max_length=255)
    post_id              = models.CharField(max_length=255, blank=True)
    user                 = models.ForeignKey(User, on_delete=models.CASCADE)
    lat                  = models.FloatField()
    long                 = models.FloatField()
    image_link           = models.TextField()
    description          = models.TextField()
    location_description = models.TextField()
    created              = models.DateTimeField(auto_now=True)
    modified             = models.DateTimeField(auto_now_add=True)

# for future, implement a replies class