from django.shortcuts import render
from .models import Reading, Listening, VideoLesson

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def courses_home(request):
    return render(request, 'lectures/courses_home.html')


def reading_lessons(request):
    readings = Reading.objects.all()
    context = {"readings": readings}
    return render(request, 'lectures/reading_lessons.html', context)


def listening_lessons(request):
    l_lessons = Listening.objects.all()
    context = {"l_lessons": l_lessons}
    return render(request, 'lectures/listening_lessons.html', context)


def writing(request):
    return render(request, 'lectures/writing_practice.html')


def video_lessons(request):
    vid_lessons = VideoLesson.objects.all()
    context = {"vid_lessons": vid_lessons}
    return render(request, 'lectures/video_lessons.html', context)
