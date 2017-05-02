# third party imports
from rest_framework import serializers

from bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializing bookmark objects to json
    """
    class Meta:
        model = Bookmark
        fields = '__all__'
