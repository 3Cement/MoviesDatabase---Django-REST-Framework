from django import forms
from django.forms import ModelForm
from .models import Movie, Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'movie']
        labels = { 'body': 'Comment', 'movie': 'Movie',}
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)