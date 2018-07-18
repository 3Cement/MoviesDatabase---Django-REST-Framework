import unittest
from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, APIClient, RequestsClient, APITestCase

from .views import *
from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer


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

    def test_movie_data(self):
        m = Movie.objects.create(title="Movie1", data={"Year": "2000", "Country": "UK, USA"})
        self.assertEqual(m.data, {"Year": "2000", "Country": "UK, USA"})

# Testing the Comment Model
class CommentTestCase(TestCase):
    def setUp(self):
    	firstMovie = Movie.objects.create(title='FirstMovie')
    	secondMovie = Movie.objects.create(title='SecondMovie')
    	Comment.objects.create(body="Amazing movie!", movie=firstMovie)
    	Comment.objects.create(body="The worst movie ever!", movie=secondMovie)

    def test_comments_exist(self):
        first = Comment.objects.get(body="Amazing movie!")
        second = Comment.objects.get(body="The worst movie ever!")
        self.assertEqual(first.body, 'Amazing movie!')
        self.assertEqual(first.movie.title, 'FirstMovie')
        self.assertEqual(second.body, 'The worst movie ever!')
        self.assertEqual(second.movie.title, 'SecondMovie')


# Testing the views
class ViewsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    #Movies Views
    def test_movies_list(self):
        response = self.client.get('/allmovies/')
        self.assertEqual(response.status_code, 200)

    def test_movie_detail_with_no_content(self):
        response = self.client.get('/movie/2')
        self.assertEqual(response.status_code, 404)

    def test_movie_detail_with_content(self):
        Movie.objects.create(title='Movie1')
        response = self.client.get('/movie/1')
        self.assertEqual(response.status_code, 200)

    #Comments Views
    def test_comments_list(self):
        response = self.client.get('/allcomments/')
        self.assertEqual(response.status_code, 200)

    def test_add_comment_template(self):
        response = self.client.get('/comment/')
        self.assertEqual(response.status_code, 200)

# Testing JSON output
class JSONTestsNoData(TestCase):

    #Movies
    def test_get_movies_empty_list(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),[])        

    def test_get_movie_movie2_and_movies_list_without_comments(self):
        Movie.objects.create(title="Movie1")
        response1 = self.client.get('/api/movies/1/')

        self.assertEqual(response1.status_code, 200)
        self.assertJSONEqual(str(response1.content, encoding='utf8'),
            {'id': 1, 'url': 'http://testserver/api/movies/1/', 'title': 'Movie1', 'data': None, 'comments': []})

        Movie.objects.create(title="Movie2")
        response2 = self.client.get('/api/movies/2/')

        self.assertEqual(response1.status_code, 200)
        self.assertJSONEqual(str(response2.content, encoding='utf8'),
            {'id': 2, 'url': 'http://testserver/api/movies/2/', 'title': 'Movie2', 'data': None, 'comments': []})

        response3 = self.client.get('/api/movies/')

        self.assertEqual(response1.status_code, 200)
        self.assertJSONEqual(str(response3.content, encoding='utf8'),[
            {'id': 1, 'url': 'http://testserver/api/movies/1/', 'title': 'Movie1', 'data': None, 'comments': []},
            {'id': 2, 'url': 'http://testserver/api/movies/2/', 'title': 'Movie2', 'data': None, 'comments': []}
            ])

    #Comments
    def test_get_comments_empty_list(self):
        response4 = self.client.get('/api/comments/')
        self.assertEqual(response4.status_code, 200)
        self.assertJSONEqual(str(response4.content, encoding='utf8'),[])

    def test_get_comment_with_no_movie(self):
        Comment.objects.create(body="Example comment")
        response5 = self.client.get('/api/comments/1/')
        self.assertEqual(response5.status_code, 200)
        self.assertJSONEqual(str(response5.content, encoding='utf8'),
            {'id': 1, 'url': 'http://testserver/api/comments/1/', 'body': 'Example comment', 'movie': None})

class JSONTestsWithData(TestCase):
    def setUp(self):
        self.someMovie = Movie.objects.create(title='SomeMovie')
        comment1 = Comment.objects.create(body="Comment1", movie=self.someMovie)
        self.nextMovie = Movie.objects.create(title='NextMovie')
        comment2 = Comment.objects.create(body="Comment2", movie=self.nextMovie)
'''
    #Movies
    def test_get_movies_list(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
            [
            {'id': 1, 'url': 'http://testserver/api/movies/1/', 'title': 'SomeMovie', 'data': None, 'comments': ['Comment1']}, 
            {'id': 2, 'url': 'http://testserver/api/movies/2/', 'title': 'NextMovie', 'data': None, 'comments': ['Comment2']}
            ]
            )
'''
'''
    def test_get_movie_with_data(self):
        Movie.objects.create(title="Movie1")

        response1 = self.client.get('/api/movies/1/')

        self.assertEqual(response1.status_code, 200)
        self.assertJSONEqual(str(response1.content, encoding='utf8'),
            {'id': 1, 'url': 'http://testserver/api/movies/1/', 'title': 'Movie1', 'data': None, 'comments': []})

    #Comments
    def test_get_comments_empty_list(self):
        response4 = self.client.get('/api/comments/')
        self.assertEqual(response4.status_code, 200)
        self.assertJSONEqual(str(response4.content, encoding='utf8'),[])

    def test_get_comment_with_movie(self):
        response = self.client.get('/api/comments/1/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
            {'id': 1, 'url': 'http://testserver/api/comments/1/',
            'body': 'Example comment!', 'movie': 'http://testserver/api/movies/1/'})
'''
class TestMoviesJSON_RequestFactory(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = MovieView.as_view({'get': 'list'})
        self.uri = '/api/movies/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                        'Expected Response Code 200, received {0} instead.'
                        .format(response.status_code))


    def test_get_movie_with_data(self):
        Movie.objects.create(title="Movie2")

        response2 = self.client.get('/api/movies/1/')

        self.client = APIClient()
        self.client.post('/api/movies/1', {'id': 1, 'url': 'http://testserver/api/movies/1/', 'title': 'Movie2', 
            'data': 'Something about movie!', 'comments': ['something about movie']}, format='json')
        self.assertEqual(response2.status_code, 200)
        self.assertJSONEqual(str(response2.content, encoding='utf8'),
            {'id': 1, 'url': 'http://testserver/api/movies/1/', 'title': 'Movie2', 'data': None, 'comments': []})

'''
class TestMoviesJSON_Client(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.view = MovieView.as_view({'get': 'list'})
        self.uri = '/api/movies/'

    def test_list2(self):
        response = self.client.get(self.uri)        
        self.assertEqual(response.status_code, 200,
                        'Expected Response Code 200, received {0} instead.'
                        .format(response.status_code))

    def test_create(self):
        params = {'id': 1, 'url': 'http://testserver/api/movies/1/', 'title': 'Movie1',
                 'data': 'Some data about movie', 'comments': []}
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                        'Expected Response Code 201, received {0} instead.'
                        .format(response.status_code))
'''