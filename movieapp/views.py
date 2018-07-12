from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import MovieSerializer, CommentSerializer
import json

class MovieView(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class CommentView(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

def homepage(request):
	return render(request, 'home.html')

def results(request):
	movie = Movie()
	if request.GET.get('searchTitle') is not None:
		searchname = request.GET.get('searchTitle')
		movieData = movie.getOMDBdata(searchname)
		return render(request, 'home.html', {'movieData': movieData, 'search': True})
	else:
		return render(request, 'home.html')
'''
def get_movie(request, title):
	if request.method =='GET':
		try:
			movie = Movie.objects.get(title=title)
			response = json.dumps([{ 'Movie': movie.title, 'MovieData': movie.movieData }])
		except:
			response = json.dumps([{ 'Error': 'No movie with that title' }])
	return HttpResponse(response, content_type='text/json')
'''
class MovieList(APIView):

	def get(self, request):
		movies = Movie.objects.all()
		serializer = MovieSerializer(movies, many=True)
		return Response(serializer.data)
