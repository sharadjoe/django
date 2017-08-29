from __future__ import unicode_literals

from django.db import models

class album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=600)
    genre = models.CharField(max_length=200)
    album_logo = models.CharField( max_length=100)

    def __unicode__(self): 
        return self.artist


class song(models.Model):
    album = models.ForeignKey(album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)


    def __unicode__(self): 
        return self.song_title
    

    
