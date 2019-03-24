from django.shortcuts import render

# Create your views here.
from Comments.serializer import CommentSerializer
from Comments.models import Comment
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from PetPosts.models import PetPost
from django.views.generic import View


class LoginView(View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(PetPost, id=request.POST.get("post_id"))
        Comment.objects.create(post=post, text=request.POST.get("text"), author_id=request.POST.get("author_id"))

    def get(self, request):
        post = get_object_or_404(PetPost, id=request.GET['post_id'])
        return Response({"post_id": post.id})
        comments = post.comments.all()
        serialized = CommentSerializer(comments, many=True)
        return Response({"comments": serialized.data})