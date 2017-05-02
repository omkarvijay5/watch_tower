# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django imports
from django.contrib import admin

# third party imports
from bookmark.models import Bookmark
# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
	"""
	bookmark admin page to add or modify from admin
	"""
    pass
