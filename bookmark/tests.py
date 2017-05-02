# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

# django imports
from django.test import TestCase, Client

# third party imports
from bookmark.factories import BookmarkFactory
from bookmark.models import Bookmark


class BookmarkCreateTestCase(TestCase):
    """
    Test bookmark create successful
    """

    def setUp(self):
        self.client = Client()

    def test_create_bookmark_with_no_data(self):
        """when input name and url are blank. should not create a bookmark"""
        response = self.client.post('/api/bookmarks/', {})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Bookmark.objects.count(), 0)

    def test_create_bookmark_with_invalid_url(self):
        """
        when input url is not of the for url format(https://example.com) then should not create a bookmark
        """
        response = self.client.post('/api/bookmarks/', {'url': 'invalid_url'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Bookmark.objects.count(), 0)

    def test_create_bookmark_with_invalid_url(self):
        """
        happy path. when name is not blank and url is in proper format bookmark is created
        """
        response = self.client.post('/api/bookmarks/', {'url': 'https://example.com/', 'name': 'example bookmark'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Bookmark.objects.count(), 1)


class BookmarkListTestCase(TestCase):
    """
    test Bookmark list api
    """

    def setUp(self):
        self.client = Client()

    def test_list_page_returns_all_bookmarks(self):
        """bookmark list api returns all the bookmarks with order name"""
        BookmarkFactory.create(name='stackoverflow', url='https://stackoverflow.com')
        BookmarkFactory.create(name='facebook', url='https://facebook.com')
        response = self.client.get('/api/bookmarks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Bookmark.objects.count(), 2)
        bookmarks = response.data

        # assert data
        self.assertEqual(bookmarks[0]['name'], 'facebook')
        self.assertEqual(bookmarks[0]['url'], 'https://facebook.com')

        # assert data
        self.assertEqual(bookmarks[1]['name'], 'stackoverflow')
        self.assertEqual(bookmarks[1]['url'], 'https://stackoverflow.com')


class BookmarkUpdateTestCase(TestCase):
    """
    Test  bookmark update
    """

    def setUp(self):
        self.client = Client()
        self.bookmark = BookmarkFactory.create(name='xyz', url='http://xyz.com')

    def test_update_bookmark(self):
        """updating a bookmark is successful"""
        payload = json.dumps({"name": "django", "url": "https://django.com"})
        response = self.client.put('/api/bookmarks/' + str(self.bookmark.id) + '/', payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Bookmark.objects.count(), 1)
        bookmark = Bookmark.objects.get(name="django")

        self.assertEqual(bookmark.url, 'https://django.com')


class BookmarkDeleteTestCase(TestCase):
    """
    Test bookmark delete
    """

    def setUp(self):
        self.client = Client()
        self.bookmark = BookmarkFactory.create()

    def test_update_bookmark(self):
        """updating a bookmark is successful"""
        self.assertEqual(Bookmark.objects.count(), 1)
        response = self.client.delete('/api/bookmarks/' + str(self.bookmark.id) + '/', {}, content_type='application/json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Bookmark.objects.count(), 0)
