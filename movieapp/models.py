from django.db import models
import urllib.request
import urllib, sys, requests, json
from urllib.parse import quote

class Comment(models.Model):
	body = models.TextField(max_length=200)

	def __str__(self):
		return self.body

class Movie(models.Model):
	title = models.CharField(max_length=50)
	comment = models.ManyToManyField(Comment, blank=True)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

	def getMovieData(self, title):
		from tabulate import tabulate
		#jsonData = urllib.request.urlopen("http://omdbapi.com/?t=%s&y=&tomatoes=true&plot=short&r=json" % title)
		#request = urllib.request.Request("http://omdbapi.com/?t=%s&y=&tomatoes=true&plot=short&r=json" % title)
		#response = urllib.request.urlopen(request)
		title = urllib.parse.quote(title)
		API_KEY = '44c18575'
		try:
			request = urllib.request.Request("https://www.omdbapi.com/?t=%s&apikey=44c18575" % title)
			print('Movie title exist in database.')
		except Exception:
			print('Błąd pobrania danych z ompdbapi')
			sys.exit(1)
	
		response = urllib.request.urlopen(request)
		json_string = response.read().decode('utf-8')
		
		moviedict = json.loads(json_string)
		self.movieData = moviedict

		headers = ['Key', 'Value']
		data = sorted([(str(k),str(v)) for k,v in moviedict.items()]) # flip the code and name and sort
		print(tabulate(data, headers=headers))

		print('Ratings:')
		for i in moviedict['Ratings']:
			data = sorted([(str(k),str(v)) for k,v in i.items()]) # flip the code and name and sort
			print(tabulate(data))

		return self.movieData

'''
	def get_values(self, title):
		title = self.title
		sys.stdout.write(u'Pobieram dane... ')
		sys.stdout.flush()
		try:
			page = requests.get("https://www.omdbapi.com/?t=%s&apikey=44c18575" % title)
		except Exception:
			print(u'Błąd pobrania danych z API NBP')
			sys.exit(1)

		page.raise_for_status
		currencies = json.loads(page.text)
		#currencies_list = currencies[0]['rates'] 
		print(currencies) 
'''

class Comment2(models.Model):
	body = models.TextField(max_length=200)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.body

#Movie().getMovieData('Guardians of the Galaxy Vol. 2')
#Movie().getMovieData('Game of Thrones')
#Movie().get_values('Guardians of the Galaxy Vol. 2')