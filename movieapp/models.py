from django.db import models
import urllib.request
import urllib, sys, requests, json
from urllib.parse import quote
from jsonfield import JSONField
from collections import OrderedDict

class Movie(models.Model):
	title = models.CharField(max_length=50)
	data = JSONField(null=True)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

	def getOMDBdata(self, title):
		title = urllib.parse.quote(title)
		API_KEY = '44c18575'
		try:
			request = urllib.request.Request("https://www.omdbapi.com/?t=%s&apikey=44c18575" % title)
			print('Request data successfull')
		except Exception:
			print('Error: Request data unsuccessfull')
			sys.exit(1)
	
		response = urllib.request.urlopen(request)
		json_string = response.read().decode('utf-8')
		
		self.moviedict = json.loads(json_string, object_pairs_hook=OrderedDict)
		if(self.moviedict['Response'] == 'True'):
			if Movie.objects.filter(title=self.moviedict['Title']).exists():
				existing_movie = Movie.objects.get(title=self.moviedict['Title'])
				print('There is already that movie in the database')
				return existing_movie.data
			else:
				new_movie = Movie.objects.create(title=self.moviedict['Title'], data=self.moviedict)
				print('Movie added to the OUR database')
				return new_movie.data

class Comment(models.Model):
	body = models.TextField(max_length=200)
	movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.body