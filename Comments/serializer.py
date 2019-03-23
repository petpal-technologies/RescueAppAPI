from rest_framework import serializers
from Comments.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('author','text', 'post')