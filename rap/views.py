from django.shortcuts import render, get_object_or_404
from django.db import connection
from rap.models import Song
import urllib2, json
from helper import format_number
# Create your views here.

def index(request):
	#get last song to show
	play_song = Song.objects.latest('id')

	#get last 15 songs for latest list
	all_songs = Song.objects.all()
	be_shown = all_songs[len(all_songs)-15:]
	last10 = []
	for song in be_shown:
		last10.append(song)
	last10.reverse()

	#get number of views for last song
	api_key = "AIzaSyCWDfJdQfcOeDGjvL4Rs0sNnaTY0CcBMRY"
	url_for_details = "https://www.googleapis.com/youtube/v3/videos?id=" + play_song.url + "&key=" + api_key + "&fields=items(id,snippet(channelId,title,categoryId,description),statistics)&part=snippet,statistics"
	response = urllib2.urlopen(url_for_details)
	html = response.read()
	json_file = json.loads(html)
	views = json_file['items'][0]['statistics']['viewCount']
	formatted_views = format_number(views)
	
	context = {'last10': last10, 'playSong': play_song, 'viewCount': formatted_views}
	return render(request, 'rap/index.html', context)

def oneSong(request, song_url):

	#taking url for check if there is "/" at the end
	url = str(song_url)
	if("/" in url):
		url = url[:len(url)-1]
	play_song = Song.objects.get(url=url)

	#get last 15 songs for latest songs
	all_songs = Song.objects.all()
	be_shown = all_songs[len(all_songs)-15:]
	last10 = []
	for song in be_shown:
		last10.append(song)
	last10.reverse()

	#get number of views for certain song
	api_key = "AIzaSyCWDfJdQfcOeDGjvL4Rs0sNnaTY0CcBMRY"
	url_for_details = "https://www.googleapis.com/youtube/v3/videos?id="+ play_song.url + "&key=" + api_key + "&fields=items(id,snippet(channelId,title,categoryId,description),statistics)&part=snippet,statistics"
	response = urllib2.urlopen(url_for_details)
	html = response.read()
	json_file = json.loads(html)
	views = json_file['items'][0]['statistics']['viewCount']
	formatted_views = format_number(views)

	context = {'last10': last10, 'playSong': play_song, 'viewCount': formatted_views}
	return render(request, 'rap/index.html', context)

def search(request, song_name):
	#parse request
	name = str(request)
	names = name.split('=')
	name = names[1][:-2]

	songs = []
	if name != '':
		#create custom cursor to find all songs that contains song parameters user typed
		cursor = connection.cursor()
		query = 'Select * From rap_song Where song_name LIKE "%' + name + '%"'
		cursor.execute(query)

		#iterate through cursor and make list of songs
		for s in cursor.fetchall():
			song = Song()
			song.song_name = s[1]
			song.url = s[2]
			song.pic_url = s[4]
			songs.append(song)

	empty = False
	if len(songs) == 0:
		empty = True

	context = {'songs': songs, 'empty': empty, 'search': name}
	return render(request, 'rap/results.html', context)