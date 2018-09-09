from django.contrib import admin

from .models import Play
from .models import PlayCasting
from .models import PlayImage
from .models import PlayMember
from .models import PlayRelImage
from .models import PlayVideo

from .models import Gala
from .models import GalaSetlist
from .models import GalaPhoto

from .models import PlayMember
from .models import PlayTeamPhoto
# Register your models here.


class PlayCastingInline(admin.TabularInline):
    model = PlayCasting
    extra = 3


class PlayImageInline(admin.TabularInline):
    model = PlayImage
    extra = 3

class PlayRelImageInline(admin.TabularInline):
    model = PlayRelImage
    extra = 6

class PlayVideoInline(admin.TabularInline):
    model = PlayVideo
    extra = 3

class PlayMemberInline(admin.TabularInline):
    model = PlayMember
    extra = 3

class PlayTeamPhotoInline(admin.TabularInline):
    model = PlayTeamPhoto
    extra = 3


class PlayAdmin(admin.ModelAdmin):
    inlines = [PlayMemberInline, PlayTeamPhotoInline, PlayCastingInline, PlayImageInline,  
            PlayRelImageInline, PlayVideoInline,]

admin.site.register(Play, PlayAdmin)

class GalaSetlistInline(admin.TabularInline):
    model = GalaSetlist
    extra = 3

class GalaPhotoInline(admin.TabularInline):
    model = GalaPhoto
    extra = 4

class GalaAdmin(admin.ModelAdmin):
    inlines = [GalaSetlistInline, GalaPhotoInline,]

admin.site.register(Gala, GalaAdmin)


""" DB 구조랑 등등 한번다시생각해보자.
class PlayMemberAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
            'admission_order_letme',
            'team',
            'position',
            'name',
            'major',
            'admission_year',
            )
    list_filter = ('admission_order_letme',)

admin.site.register(PlayMember, PlayMemberAdmin)
"""


























