from django.db import models
from django.core import validators

# Create your models here.

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
            upload_to="homepage/static/img")
    synopsis = models.TextField(
            verbose_name='시놉시스',
            )
    num_of_audience = models.PositiveIntegerField(
            verbose_name='관객 수',
            default=1,
            )

class PlayCasting(models.Model):
    play = models.ForeignKey(Play, related_name='castings', on_delete=models.CASCADE)
    casting = models.ImageField(
            verbose_name='배역 이미지',
            )

class PlayImage(models.Model):
    play = models.ForeignKey(Play, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
            verbose_name='공연 관련 사진'
            )

class PlayVideo(models.Model):
    play = models.ForeignKey(Play, related_name='video_urls', on_delete=models.CASCADE)
    video_url = models.CharField(
            verbose_name='공연 관련 링크(극 공개, 티저, 인터뷰순)',
            max_length=200)






























