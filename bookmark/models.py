# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator



class Bookmark(models.Model):
    """
    Boommark is a model which is used to bookmark(save) an url which you like
    """

    # name is used to provide a name to the bookmark. It can also be used as an alias for the url
    name = models.CharField(max_length=50)

    # The url to be bookmarked
    url = models.TextField(validators=[URLValidator()])

    def __unicode__(self):
        return self.url
