from django.contrib import admin

from .models import Play
from .models import PlayImage
from .models import PlayCasting
from .models import PlayVideo
# Register your models here.

class PlayCastingInline(admin.TabularInline):
    model = PlayCasting
    extra = 3

class PlayImageInline(admin.TabularInline):
    model = PlayImage
    extra = 6

class PlayVideoInline(admin.TabularInline):
    model = PlayVideo
    extra = 3

class PlayAdmin(admin.ModelAdmin):
    inlines = [PlayCastingInline, PlayImageInline, PlayVideoInline,]

admin.site.register(Play, PlayAdmin)

































