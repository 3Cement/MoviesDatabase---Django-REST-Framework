from rest_framework import serializers
from .models import Movie, Comment, Comment2

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Movie
		fields = ('id', 'url', 'title', 'comment',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'url', 'body')

class Comment2Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment2
		fields = ('id', 'url', 'body', 'movie')