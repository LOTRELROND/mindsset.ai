from . serializer import PostSerializer
from rest_framework.generics import GenericAPIView
from core.models import Post
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics
from rest_framework.generics import get_object_or_404

############ POST ###########
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 