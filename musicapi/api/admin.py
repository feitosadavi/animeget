from django.contrib import admin

from .models import Music, Album, Band, Member

admin.site.register(Music)
admin.site.register(Album)
admin.site.register(Band)
admin.site.register(Member)

# Register your models here.
