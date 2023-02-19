from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_year = models.PositiveSmallIntegerField()
    album_art = models.URLField()
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.artist}"