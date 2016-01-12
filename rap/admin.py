from django.contrib import admin
from rap.models import Song
# Register your models here.

class SongAdmin(admin.ModelAdmin):
	fields = ['song_name', 'url']

admin.site.register(Song, SongAdmin)

admin.site.site_header = 'Rappz administration'

admin.site.site_title = 'Rappz admin site'