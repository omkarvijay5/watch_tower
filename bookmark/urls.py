# define the urls related to bookmark app
# The complete url may look like /api/bookmark_url

# django imports
from django.conf.urls import url

# third party imports
from bookmark.api import BookmarkApi, BookmarkCreateListApi


urlpatterns = [
    # url(r'^(?P<url>(.*))/$', BookmarkApi.as_view(), name='bookmark_api')
    url(r'^bookmarks/$', BookmarkCreateListApi.as_view(), name='bookmark_list_create_api'),
    url(r'^bookmarks/(?P<pk>[0-9]+)/$', BookmarkApi.as_view(), name='bookmark_detail_api')
]
