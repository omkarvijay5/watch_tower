# python imports

# django imports
from rest_framework import generics
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.views import APIView

# third party imports
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer


class BookmarkApi(generics.RetrieveUpdateDestroyAPIView):
    model = Bookmark
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class BookmarkCreateListApi(generics.ListCreateAPIView):
    model = Bookmark
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
