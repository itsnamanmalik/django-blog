from django.shortcuts import render
from video.models import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def videos(request):
    allvideo = Video.objects.all()
    video_dict = {"allvideo":allvideo}
    return render(request, 'video_app/videos.html', video_dict)

def single_video(request ,slug):

    isvideo = Video.objects.filter(slug=slug)

    count = 0
    for c in isvideo:
        count = count + 1

    if (count > 0):
        isvideo = isvideo.first()
        video_dict = {"slug":slug, "video":isvideo}
        return render(request,'video_app/video_single.html',video_dict)
    else:
        return HttpResponse("404")

