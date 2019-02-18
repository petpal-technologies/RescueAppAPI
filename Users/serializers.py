from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()

from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='hash_id', read_only=True)

    class Meta:
        model = models.CustomUser
        fields = ('id', 'username')
