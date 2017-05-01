# third party imports
from rest_framework import serializers

from bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializing bookmarks
    """
    class Meta:
        model = Bookmark
        fields = '__all__'
