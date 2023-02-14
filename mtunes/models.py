from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    '''
    This class defines the properties and attributes of a song
    param: song_id : the id of the song
    param: name : the name of the song
    param: singer : describes the artist's name
    param: tags : song category
    param: song : actual song file
    param: movie : genre of the song
    '''
    song_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 2000)
    singer = models.CharField(max_length= 2000)
    tags = models.CharField(max_length= 100)
    image = models.ImageField(upload_to = 'docs')
    song = models.FileField(upload_to= 'docs')
    movie = models.CharField(max_length = 150, default = "None")

    def __str__(self):
        return self.name
    
class Watchlater(models.Model):
    '''
    This class describes the attributes of songs to be watched later
    param: watch_id : the song watch id
    param: user : the user watching the song to be watched later
    param: video_id : the id of the songs being played
    '''
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=10000000, default="")

class History(models.Model):
    '''
    This class describes the attributes of song history
    param: hist_id : the history id of the song
    param: user : describes the foreign key which is the user
    param: music_id : describes the music_id for the song in the history
    '''
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")
