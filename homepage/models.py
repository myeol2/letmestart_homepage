from django.db import models

# Create your models here.

class Play(models.Model):
    title = models.CharField(max_length=50)
    poster = models.ImageField(upload_to="homepage/static/img")
    synopsis = models.TextField()


class PlayImage(models.Model):
    play = models.ForeignKey(Play, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()






























