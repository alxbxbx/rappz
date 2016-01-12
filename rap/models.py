from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Song(models.Model):
	song_name = models.CharField(max_length = 100)
	url = models.CharField(max_length = 200)
	date_created = models.DateTimeField(auto_now = False, auto_now_add = True)
	pic_url = models.CharField(max_length = 100)

	def save(self, *args, **kwargs):
		if("youtube.com" in self.url):
			self.url = self.url[32:]
		self.pic_url = "http://img.youtube.com/vi/" + self.url + "/0.jpg"
		try:
			Song.objects.get(url = self.url)
		except ObjectDoesNotExist:
			super(Song, self).save(*args, **kwargs)
			
	def __str__(self):
		return self.song_name

class RapUser(models.Model):
	name = models.CharField(max_length= 30)
	last_name = models.CharField(max_length= 30)
	username = models.CharField(max_length= 30)
	password = models.CharField(max_length= 200)
	email = models.CharField(max_length= 50)
	fb_id = models.CharField(max_length= 50)

class Comment(models.Model):
	song = models.ForeignKey(Song)
	rap_user = models.ForeignKey(RapUser)
	comment_text = models.CharField(max_length = 1000)
	likes = models.IntegerField()
	dislikes = models.IntegerField()



