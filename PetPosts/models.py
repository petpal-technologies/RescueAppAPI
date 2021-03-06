from django.db import models
from django.contrib.auth.models import User

from Rescue_App_API_ import settings
import uuid

# Create your models here.


def get_upload_to(instance, filename):
    instance.uuid = uuid.uuid4().hex
    return '%s/%s' % (instance.uuid, filename)


class PetPost(models.Model):

    user                 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title                = models.CharField(max_length=255)
    lat                  = models.FloatField()
    long                 = models.FloatField()
    image                = models.ImageField(upload_to=get_upload_to, null=True, blank=True)
    location_description = models.TextField()
    created              = models.DateTimeField(auto_now=True)
    modified             = models.DateTimeField(auto_now_add=True)
    id                   = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    description          = models.TextField(default="description")
    views                = models.IntegerField(default=0)
    status               = models.CharField(default="looking", max_length=30)

    def __str__(self):
        return self.title




    # for future, implement a Replies class
