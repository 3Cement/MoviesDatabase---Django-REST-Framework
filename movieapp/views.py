from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from movieapp.models import *
from .serializers import MovieSerializer, CommentSerializer, Comment2Serializer

class MovieView(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class CommentView(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class Comment2View(viewsets.ModelViewSet):
	queryset = Comment2.objects.all()
	serializer_class = Comment2Serializer

def homepage(request):
	return render(request, 'home.html')

def results(request):
	m = Movie()
	if request.GET.get('q') is not None:
		searchname = request.GET.get('q')
		if Movie.objects.filter(title=searchname).exists():
			print('Wczytuję film z naszej bazy danych!')
			our_movie = Movie.objects.get(title=searchname)
			print('Wczytuję film z naszej bazy danych2!')
			movieData = our_movie.data
			return render(request, 'home.html', {'movieData': movieData, 'search': True})
		else:
			movieData = m.getMovieData(searchname)
			return render(request, 'home.html', {'movieData': movieData, 'search': True})
	else:
		return render(request, 'home.html')
	print (searchname)

#Request response should include full movie object, along with all data fetched from external API.
import json

def get_movie(request, title):
	if request.method =='GET':
		try:
			movie = Movie.objects.get(title=title)
			response = json.dumps([{ 'Movie': movie.title, 'MovieData': movie.movieData }])
		except:
			response = json.dumps([{ 'Error': 'No movie with that title' }])
	return HttpResponse(response, content_type='text/json')
'''
def add_movie(request, title):
	if request.method =='POST':

		movieData = m.getMovieData(searchname)'''

# List all movies or create a new one
class MovieList(APIView):

	def get(self, request):
		movies = Movie.objects.all()
		serializer = MovieSerializer(movies, many=True)
		return Response(serializer.data)

	def post(self):
		pass
