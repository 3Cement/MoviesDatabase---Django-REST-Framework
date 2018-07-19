from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Comment
from .forms import CommentForm
from .serializers import MovieSerializer, CommentSerializer
import json


class MovieView(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class CommentView(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movie_detail.html'

    def get_context_data(self, **kwargs):
    	context = super(MovieDetailView, self).get_context_data(**kwargs)
    	context['comments_list'] = Comment.objects.all()
    	return context


def homepage(request):
	return render(request, 'home.html')

def allmovies(request):
	movie_list = Movie.objects.all()
	return render(request, 'movie_list.html', {'movie_list': movie_list})

def allcomments(request):
	comment_list = Comment.objects.all()
	return render(request, 'comment_list.html', {'comment_list': comment_list})

def comments_by_book_id(request, pk):
	movie=get_object_or_404(Movie, pk = pk)
	comment_list = Comment.objects.filter(movie=movie).all()
	return render(request, 'comment_list_by_id.html', {'comment_list': comment_list, 'movie': movie})

def add_comment(request):
	if request.method == 'POST':
		form = CommentForm(request.POST or None)
		if form.is_valid():
			form.save()
			#messages.success(request, ('Comment has been added!'))
			return redirect('home.html')
		else:
			form = CommentForm()
			#messages.success(request, ('You CommentFOrm is invalid'))
			return redirect('home.html')
	else:
		form = CommentForm()
	return render(request, 'comment_form.html', { 'form': form, },)

def results(request):
	print('Looking for results')
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
