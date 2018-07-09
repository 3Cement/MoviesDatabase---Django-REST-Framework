from django.shortcuts import render
from rest_framework import viewsets
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
		movieData = m.getMovieData(searchname)
		return render(request, 'home.html', {'movieData': movieData, 'search': True})
	else:
		return render(request, 'home.html')
	print (searchname)