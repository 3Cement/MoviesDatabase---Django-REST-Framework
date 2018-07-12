from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', views.MovieView)
router.register('comments', views.CommentView)

urlpatterns = [
	path('api/', include(router.urls)),
    url(r'^$', views.homepage),
    url(r'^search/', views.results),
    url(r'^movies/', views.MovieList.as_view()),
]
'''
urlpatterns = [
    url(r'^movies/', views.MovieList.as_view()),
]
'''