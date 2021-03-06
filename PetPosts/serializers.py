from rest_framework import serializers

from PetPosts.models import PetPost
from Rescue_App_API_ import settings


class PostSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    # post_id = serializers.CharField(max_length=255)
    # lat = serializers.FloatField()
    # long = serializers.FloatField()
    # image = serializers.ImageField()
    # description = serializers.CharField()
    # location_description = serializers.CharField()
    # created = serializers.DateTimeField()
    # modified = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return PetPost.objects.create(**validated_data)

    class Meta:
        model = PetPost
        fields = ('user','title', 'lat', 'long','image','location_description','created','modified','id','description','views','status')