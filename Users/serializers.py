from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()

from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='hash_id', read_only=True)
    user_type = serializers.CharField()
    user_name = serializers.CharField()
    fb_user   = serializers.BooleanField()

    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'user_type', 'user_name', 'fb_user')
