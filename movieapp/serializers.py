from rest_framework import serializers
from .models import Movie, Comment

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	data = serializers.SerializerMethodField('clean_data')
	comments = serializers.StringRelatedField(many=True)

	class Meta:
		model = Movie
		fields = ('id', 'url', 'title', 'data', 'comments')

	def clean_data(self, obj):
		return obj.data

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'url', 'body', 'movie')