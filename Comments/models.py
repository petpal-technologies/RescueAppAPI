from django.db import models
from PetPosts.models import PetPost
from Rescue_App_API_ import settings

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(PetPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text