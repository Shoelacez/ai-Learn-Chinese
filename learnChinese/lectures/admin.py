from django.contrib import admin
from .models import  Reading, Listening, VideoLesson


class ReadingAdmin(admin.ModelAdmin):
    list_display = ("title", "chinese_characters", "audio_clip",)


class ListeningAdmin(admin.ModelAdmin):
    list_display = ("phrase", "hanzi", "yingzi", "audio_clip")


class VideoLessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video')


# Register your models here.
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Listening, ListeningAdmin)
admin.site.register(VideoLesson, VideoLessonAdmin)
