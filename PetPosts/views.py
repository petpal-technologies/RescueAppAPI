from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

# from PetPosts.models import PetPost
from PetPosts.serializers import PostSerializer
# Create your views here.

class SayHiBasic(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


# class AddPetPost(APIView):
#     def add(self, data):
#         return Response({"title": "blah"})


#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = PetPost.objects.all()
#     serializer_class = PostSerializer
