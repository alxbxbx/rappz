from django.conf.urls import patterns, url
from rap import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^songs/(?P<song_url>\w+\S+)', views.oneSong, name='oneSong'),
    url(r'^results/(?P<song_name>\w{0,50})', views.search, name='search'),
)