from django.db import models
from django.utils import timezone

# Create your models here.
class Interest(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Conversation(models.Model):
    scenario = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    conversation = models.TextField()
    time_generated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.scenario



