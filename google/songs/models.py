from django.db import models

# Create your models here.

class Songs(models.Model):
    input_link = models.CharField(max_length=200)
    output_link = models.CharField(max_length=200)
    ranking = models.IntegerField(default=0)
    user_played = models.BooleanField()
    time_stamp = models.CharField(max_length=200, default='test')

class SongsFixed(models.Model):
    songs_path = models.CharField(max_length=200)