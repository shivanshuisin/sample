from django.db import models

from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=20)
    album_title = models.CharField(max_length=70)
    genre = models.CharField(max_length=30)
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title+'-'+self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=5)
    song_title = models.CharField(max_length=50)
    is_favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.song_title

