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
# Register your models here.


class PlayCastingInline(admin.TabularInline):
    model = PlayCasting
    extra = 3


class PlayImageInline(admin.TabularInline):
    model = PlayImage
    extra = 3

class PlayMemberInline(admin.TabularInline):
    model = PlayMember
    extra = 15

class PlayRelImageInline(admin.TabularInline):
    model = PlayRelImage
    extra = 6

class PlayVideoInline(admin.TabularInline):
    model = PlayVideo
    extra = 3

class PlayAdmin(admin.ModelAdmin):
    inlines = [PlayCastingInline, PlayImageInline, PlayMemberInline, 
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
































