from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', views.MovieView)
router.register(r'comments', views.CommentView)

urlpatterns = [
	path('api/', include(router.urls)),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^allmovies/', views.allmovies, name='movie_list'),
    url(r'^allcomments/', views.allcomments, name='comment_list'),
    path('comments/<int:pk>/', views.comments_by_movie_id, name='comment_list_by_id'),
    path('movie/<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),
    url(r'^comment/', views.add_comment, name='comment_form'),
    url(r'^search/', views.results),
]