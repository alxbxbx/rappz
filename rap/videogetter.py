
from django.db import models
from models import Song
import urllib2, json

class pullSongs():
    def getSongs():
        apiKey = "AIzaSyCWDfJdQfcOeDGjvL4Rs0sNnaTY0CcBMRY"


        getChannelID = "https://www.googleapis.com/youtube/v3/channels?key=AIzaSyCWDfJdQfcOeDGjvL4Rs0sNnaTY0CcBMRY&forUsername=allrapnation&part=id"
        channelRequest = urllib2.urlopen(getChannelID)

        channel = channelRequest.read()
        channelJson = json.loads(channel)
        channelID =  channelJson['items'][0]['id']

        getPlaylistID = "https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId=" + channelID + "&key=AIzaSyCWDfJdQfcOeDGjvL4Rs0sNnaTY0CcBMRY"

        playlistRequest = urllib2.urlopen(getPlaylistID)
        playlist = playlistRequest.read()
        playlistJson = json.loads(playlist)

        for item in playlistJson['items']:
            getVideosID = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=" + str(item['id']) +"&maxResults=50&key=AIzaSyCWDfJdQfcOeDGjvL4Rs0sNnaTY0CcBMRY"
            videosRequest = urllib2.urlopen(getVideosID)
            videos = videosRequest.read()
            videosJson = json.loads(videos)
            for songItem in videosJson['items']:
                print songItem['snippet']['title']
                song = Song()
                song.song_name = songItem['snippet']['title']
                song.url = songItem['snippet']['resourceId']['videoId']
                Song.save(song)