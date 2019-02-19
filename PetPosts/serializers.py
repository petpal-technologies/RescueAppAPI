from rest_framework import serializers

from PetPosts.models import PetPost
from Rescue_App_API_ import settings


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    post_id = serializers.CharField(max_length=255)
    lat = serializers.FloatField()
    long = serializers.FloatField()
    image_link = serializers.CharField()
    description = serializers.CharField()
    location_description = serializers.CharField()
    created = serializers.DateTimeField(auto_now=True)
    modified = serializers.DateTimeField(auto_now_add=True)
    author_id = serializers.CharField()

    def create(self, validated_data):
        return PetPost.objects.create(**validated_data)

    # class Meta:
    #     model = PetPost
    #     fields = ('title', 'post_id', 'user', 'lat', 'long','image_link','description','location_description','created','modified')