# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator



class Bookmark(models.Model):

	name = models.CharField(max_length=50)

	url = models.TextField(validators=[URLValidator()])