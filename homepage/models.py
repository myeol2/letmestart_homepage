from django.db import models
from django.core import validators

# Create your models here.

def play_poster_path(instance, filename):
    return 'plays/{0}/{1}'.format(instance.idx, filename)
    
def play_media_path(instance, filename):
    return 'plays/{0}/{1}'.format(instance.play.idx, filename)

def gala_poster_path(instance, filename):
    return 'galas/{0}/{1}'.format(instance.idx, filename)

def gala_media_path(instance, filename):
    return 'galas/{0}/{1}'.format(instance.gala.idx, filename)

class Play(models.Model):
    idx = models.PositiveIntegerField(
            verbose_name='정기공연 회차',
            default=1,
            validators=[validators.MaxValueValidator(100), validators.MinValueValidator(1)],
            )
    title = models.CharField(
            verbose_name='공연 제목',
            max_length=50
            )
    poster = models.ImageField(
            verbose_name='포스터 이미지',
            upload_to=play_poster_path,)
    synopsis = models.TextField(
            verbose_name='시놉시스',
            )
    num_of_audience = models.PositiveIntegerField(
            verbose_name='관객 수',
            default=1,
            )

    def __str__(self):
        return ('제 %d회 정기공연 : %s' % (self.idx, self.title))


class PlayCasting(models.Model):
    play = models.ForeignKey(Play, related_name='castings', on_delete=models.CASCADE)
    casting = models.ImageField(
            upload_to=play_media_path,
            verbose_name='배역 이미지',
            )

class PlayImage(models.Model):
    play = models.ForeignKey(Play, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
            upload_to=play_media_path,
            verbose_name='공연 관련 사진'
            )

class PlayVideo(models.Model):
    play = models.ForeignKey(Play, related_name='video_urls', on_delete=models.CASCADE)
    video_url = models.CharField(
            verbose_name='공연 관련 링크(극 공개, 티저, 인터뷰순)',
            max_length=200)

class Gala(models.Model):

    idx = models.PositiveIntegerField(
            verbose_name='갈라쇼 회차',
            validators=[validators.MaxValueValidator(100), validators.MinValueValidator(1)],            
            )

    poster = models.ImageField(
            upload_to=gala_poster_path,
            verbose_name='갈라쇼 포스터',
            )

    def __str__(self):
        return ("제 %d회 갈라쇼" % (self.idx))

class GalaSetlist(models.Model):
    gala = models.ForeignKey(Gala, related_name='setlists', on_delete=models.CASCADE)
    setlist = models.ImageField(
            upload_to=gala_media_path,
            verbose_name='셋리스트'
            )

class GalaPhoto(models.Model):
    gala = models.ForeignKey(Gala, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(
            upload_to=gala_media_path,
            verbose_name='공연사진'
            )

























