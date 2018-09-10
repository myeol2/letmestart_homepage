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
            unique=True,
            )
    title = models.CharField(
            verbose_name='공연 제목',
            max_length=50
            )
    poster = models.ImageField(
            verbose_name='포스터 이미지',
            upload_to=play_poster_path,
            )
    synopsis = models.TextField(
            verbose_name='시놉시스',
            )
    num_of_audience = models.PositiveIntegerField(
            verbose_name='관객 수',
            default=1,
            )
    group_photo = models.ImageField(
            verbose_name='단체사진',
            upload_to=play_poster_path,
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
            verbose_name='공연 사진'
            )

class PlayRelImage(models.Model):
    play = models.ForeignKey(Play, related_name='rel_images', on_delete=models.CASCADE)
    photo = models.ImageField(
            upload_to=play_media_path,
            verbose_name='공연 관련 사진'
            )

class PlayVideo(models.Model):
    play = models.ForeignKey(Play, related_name='video_urls', on_delete=models.CASCADE)
    category = models.CharField(
            verbose_name='영상 이름',
            max_length=10
            )
    video_url = models.CharField(
            verbose_name='공연 관련 링크(facebook viedo id, (극 공개, 티저, 인터뷰순으로 입력))',
            max_length=200)

class Gala(models.Model):

    idx = models.PositiveIntegerField(
            verbose_name='갈라쇼 회차',
            validators=[validators.MaxValueValidator(100), validators.MinValueValidator(1)],            
            unique=True,
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


class PlayTeamPhoto(models.Model):
    play = models.ForeignKey(Play, related_name='teamphotos', on_delete=models.CASCADE)
    group_photo = models.ImageField(
                upload_to=play_media_path,
                verbose_name='팀별사진'
            )
    
    PLANNING = u"기획"
    STAGE = u"무대"
    ACT = u"배우"
    DIRECT = u"연출"
    MUSIC = u"음악"
    DANCE = u"안무"
    PRESIDENTS = u"대표"
    LEADERS = u"임원"
    

    TEAM_CHOICES = (
            (LEADERS, u'회장단/대표단'),
            (PLANNING, u'기획'),
            (STAGE, u'무대'),
            (ACT, u'배우'),
            (DIRECT, u'연출'),
            (MUSIC, u'음악'),
            (DANCE, u'안무(9기 이전)'),
            (PRESIDENTS, u'대표'),
            (LEADERS, u'임원'),
            )

    team = models.CharField(
            verbose_name=u'팀',
            max_length=2,
            choices = TEAM_CHOICES,
            )


class PlayMember(models.Model):
    play = models.ForeignKey(Play, related_name="members", on_delete=models.CASCADE)
   
    class Meta:
        ordering = ['admission_order_letme', 'name']
        verbose_name = "함께한 사람들"

    PLANNING = u"기획"
    STAGE = u"무대"
    ACT = u"배우"
    DIRECT = u"연출"
    MUSIC = u"음악"
    DANCE = u"안무"
    
    LEADER = u'공동대표'
    PRESIDENT = u'회장'
    VICE_PRESIDENT = u'부회장'
    TEAM_LEADER = u'팀장'
    TEAM_MEMBER = u'팀원'

    TEAM_CHOICES=(
            (PLANNING, u'기획'),
            (STAGE, u'무대'),
            (ACT, u'배우'),
            (DIRECT, u'연출'),
            (MUSIC, u'음악'),
            (DANCE, u'안무(9기 이전)'),
            )

    POSITION_CHOICES=(
            (LEADER, u'공동대표'),
            (PRESIDENT, u'회장'),
            (VICE_PRESIDENT, u'부회장'),
            (TEAM_LEADER, u'팀장'),
            (TEAM_MEMBER, u'팀원'),
          )


    admission_order_letme = models.IntegerField(
                verbose_name=u'기수',
                validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)]
                )
    team = models.CharField(
            verbose_name=u'팀',
            max_length=6,
            choices = TEAM_CHOICES,
            )

    
    position = models.CharField(
            choices = POSITION_CHOICES,
            max_length=6,
            default = TEAM_MEMBER 
            )

    name = models.CharField(
                verbose_name=u'이름',
                max_length=10, 
            )
    admission_year = models.IntegerField(
                verbose_name=u"학번",
                validators=[validators.MinValueValidator(0), validators.MaxValueValidator(99)]
                
                )

    major = models.CharField(
                verbose_name=u"학과",
                max_length=10,
            )
    
    def __str__(self):
        return "{0}기 {1} {2} {3}".format(self.admission_order_letme, self.team, self.position, self.name)


















