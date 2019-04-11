from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from Rescue_App_API_ import helper

class CustomUser(AbstractUser):
    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)
    user_type = models.CharField(default="Good Citizen", max_length=25)
    user_name = models.CharField(max_length=20)
    fb_user   = models.BooleanField(default=False)