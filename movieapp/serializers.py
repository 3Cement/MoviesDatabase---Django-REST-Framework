from rest_framework import serializers
from .models import Movie, Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'url', 'body', 'movie')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	data = serializers.SerializerMethodField('clean_data')
	comments = CommentSerializer(many=True, read_only=True)

	class Meta:
		model = Movie
		fields = ('id', 'url', 'title', 'data', 'comments')

	def clean_data(self, obj):
		return obj.data
