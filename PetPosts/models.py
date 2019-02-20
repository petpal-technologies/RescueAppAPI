from django.db import models
from django.contrib.auth.models import User

from Rescue_App_API_ import settings

# Create your models here.

class PetPost(models.Model):
    user                 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title                = models.CharField(max_length=255)
    post_id              = models.CharField(max_length=255, blank=True)
    lat                  = models.FloatField()
    long                 = models.FloatField()
    image_link           = models.TextField()
    description          = models.TextField()
    location_description = models.TextField()
    created              = models.DateTimeField(auto_now=True)
    modified             = models.DateTimeField(auto_now_add=True)
    user_id              = models.TextField()

    def __str__(self):
        return self.title







    # for future, implement a replies class
