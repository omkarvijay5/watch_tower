# define the urls related to bookmark app
# The complete url may look like /api/bookmark_url

# django imports
from django.conf.urls import url

# third party imports
from bookmark.api import BookmarkApi


urlpatterns = [
    # url(r'^(?P<url>(.*))/$', BookmarkApi.as_view(), name='bookmark_api')
    url(r'^bookmarks/$', BookmarkApi.as_view(), name='bookmark_api')
]
