# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
	"""
	landing page for the bookmarks
	"""
    return render_to_response('index.html', {})
