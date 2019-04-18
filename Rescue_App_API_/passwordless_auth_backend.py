from django.contrib.auth.backends import ModelBackend
from Users import models

class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, username=None):
        # whelp this is VERY INSECURE
        try:
            return models.CustomUser.objects.get(username=username)
        except models.CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return models.CustomUser.objects.get(pk=user_id)
        except models.CustomUser.DoesNotExist:
            return None