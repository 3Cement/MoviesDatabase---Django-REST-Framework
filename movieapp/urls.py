from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', views.MovieView)
router.register('comments', views.CommentView)
router.register('comments2', views.Comment2View)

urlpatterns = [
	path('api/', include(router.urls)),
    url(r'^$', views.homepage),
    url(r'^search/', views.results),
]
'''
urlpatterns = [
    url(r'^movies/', views.MovieList.as_view()),
]
'''