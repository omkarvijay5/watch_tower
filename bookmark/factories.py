# python imports
from __future__ import unicode_literals
from string import ascii_letters

# Third-party imports.
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from factory import LazyAttribute

from bookmark.models import Bookmark


class BookmarkFactory(DjangoModelFactory):

    name = FuzzyText(length=10, chars=ascii_letters)
    url = LazyAttribute(lambda o: 'https://%s.com' % o.name)

    class Meta:
        model = Bookmark
