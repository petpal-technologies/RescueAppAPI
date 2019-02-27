from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import mixins, generics

from PetPosts.models import PetPost
from PetPosts.serializers import PostSerializer

from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class PostView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = PostSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    queryset = PetPost.objects.all()

    def get(self, request):
        posts = PetPost.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        # post = request.data.get('post')
        # serializer = PostSerializer(data=post)
        # if serializer.is_valid(raise_exception=True):
        #     saved_post = serializer.save()
        #     return Response({"success": "Post '{}' created successfully".format(saved_post.title)})
        # else:
        #     return Response({"failure": "Post failed"})

    def delete(self, request, pk):
        # Get object with this pk
        post = get_object_or_404(PetPost.objects.all(), pk=pk)
        post.delete()
        return Response({"message": "Post with id `{}` has been deleted.".format(pk)}, status=204)


def single_post_view(request, post_id):
    try:
        post = get_object_or_404(PetPost, id=post_id)
    except ValueError:
        raise Http404

    return render_to_response('single_post.html', {'post': post})
