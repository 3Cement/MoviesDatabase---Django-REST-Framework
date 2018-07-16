import unittest
from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, APIClient, RequestsClient

from movieapp.models import Movie, Comment
from movieapp.serializers import MovieSerializer, CommentSerializer

# Testing the Comment Model
class CommentTestCase(TestCase):
    def setUp(self):
    	firstMovie = Movie.objects.create(title='FirstMovie')
    	secondMovie = Movie.objects.create(title='SecondMovie')
    	Comment.objects.create(body="Amazing movie!", movie=firstMovie)
    	Comment.objects.create(body="The worst movie ever!", movie=secondMovie)

    def test_genres_exist(self):
        first = Comment.objects.get(body="Amazing movie!")
        second = Comment.objects.get(body="The worst movie ever!")
        self.assertEqual(first.body, 'Amazing movie!')
        self.assertEqual(first.movie.title, 'FirstMovie')
        self.assertEqual(second.body, 'The worst movie ever!')
        self.assertEqual(second.movie.title, 'SecondMovie')

# Testing the Movie Model
class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="Movie1")
        Movie.objects.create(title="Movie2")

    def test_movies_exist(self):
        m1 = Movie.objects.get(title="Movie1")
        self.assertEqual(m1.title, "Movie1")
        m2 = Movie.objects.get(title="Movie2")
        self.assertEqual(m2.title, "Movie2")

# Testing JSON output
class JSONTests(TestCase):

    def test_get_comments(self):
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, 200)
        #self.assertJSONEqual(str(response.content, encoding='utf8'),{'id': 0, 'url': None, 'body': None, 'movie': None})