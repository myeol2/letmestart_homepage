from django.contrib import admin

from .models import Play
from .models import PlayImage
# Register your models here.

class PlayImageInline(admin.TabularInline):
    model = PlayImage
    extra = 6

class PlayAdmin(admin.ModelAdmin):
    inlines = [PlayImageInline,]

admin.site.register(Play, PlayAdmin)

































