from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reading(models.Model):
    level = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    chinese_characters = models.CharField(max_length=255)
    audio_clip = models.FileField(upload_to='readings/audio_clips', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Listening(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='listening/images')
    phrase = models.CharField(max_length=100)
    hanzi = models.CharField(max_length=100)
    yingzi = models.CharField(max_length=100)
    audio_clip = models.FileField(upload_to='listening/audio_clips', blank=True, null=True)

    def __str__(self):
        return self.phrase


class VideoLesson(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='video_lessons')
    posted = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
