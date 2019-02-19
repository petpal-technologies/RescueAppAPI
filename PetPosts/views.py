from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from PetPosts.models import PetPost
from PetPosts.serializers import PostSerializer

from django.shortcuts import get_object_or_404



# Create your views here.
class PostView(APIView):
    def get(self, request):
        posts = PetPost.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')

        return Response({"post": post})

        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            saved_post = serializer.save()
            return Response({"success": "Post '{}' created successfully".format(saved_post.title)})
        else:
            return Response({"failure": "Post failed"})

    def delete(self, request, pk):
        # Get object with this pk
        post = get_object_or_404(PetPost.objects.all(), pk=pk)
        post.delete()
        return Response({"message": "Post with id `{}` has been deleted.".format(pk)}, status=204)


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = PetPost.objects.all()
#     serializer_class = PostSerializer
