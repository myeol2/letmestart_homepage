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

    class Meta:
        verbose_name_plural = "등장 인물(정기공연 페이지)"

    play = models.ForeignKey(Play, related_name='castings', on_delete=models.CASCADE)
    casting = models.ImageField(
            upload_to=play_media_path,
            verbose_name='배역 이미지',
            )

class PlayImage(models.Model):

    class Meta:
        verbose_name_plural = "실황 사진(정기공연 페이지: 무대가 잘 나온 사진, 배우 표정이 잘 드러난 사진 등)"

    play = models.ForeignKey(Play, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
            upload_to=play_media_path,
            verbose_name='실황 사진'
            )

class PlayRelImage(models.Model):

    class Meta:
        verbose_name_plural = "과정들(정기공연 페이지: 무대 제작, 공연 당일 준비과정, 무대 설치, 연습 과정 등 생동감있는 사진 위주)"


    play = models.ForeignKey(Play, related_name='rel_images', on_delete=models.CASCADE)
    photo = models.ImageField(
            upload_to=play_media_path,
            verbose_name='과정들'
            )

class PlayVideo(models.Model):

    class Meta:
        verbose_name_plural = "관련 영상(정기공연 페이지| 링크는 facebook video 게시글의 id를 입력하면 됨. ex:1947738842192551)"


    play = models.ForeignKey(Play, related_name='video_urls', on_delete=models.CASCADE)
    category = models.CharField(
            verbose_name='영상 이름',
            max_length=10
            )
    video_url = models.CharField(
            verbose_name='공연 관련 링크(극 공개, 인터뷰, 티저순으로 입력)',
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

    class Meta:
        verbose_name_plural="팀별사진(사람들 페이지. 정기공연별로 프로필을 촬영하므로 이 위치에 삽입)"

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
        verbose_name_plural = "함께한 사람들(정기공연 페이지, 사람들 페이지, 공동대표 인사말 페이지에 모두 사용됨)"

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

class Etc(models.Model):
    idx = models.IntegerField(
                verbose_name=u'기수',
                validators=[validators.MinValueValidator(0), validators.MaxValueValidator(99)],
            )


class EtcChief(models.Model):

    class Meta:
        verbose_name_plural = "대표 정보(홈페이지 하단)"


    etc = models.ForeignKey(Etc, related_name="chiefs", on_delete=models.CASCADE)
    POSITION_CHOICES = (
            (u'공동대표', u'공동대표'),
            (u'회장', u'회장'),
            (u'부회장', u'부회장'),
            )
    position = models.CharField(
                verbose_name=u'직책',
                max_length=5,
                choices = POSITION_CHOICES,
            )
    name = models.CharField(
                verbose_name=u'이름',
                max_length=6,
            )
    phone_number = models.CharField(
                verbose_name=u'연락처',
                max_length=13,
            )

