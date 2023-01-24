from django.shortcuts import render
from app.models import *
# Create your tests here.

def topic(request):
    t=Topic.objects.all()
    d={'topics':t}
    return render(request,'topic.html',d)


def webpage(request):
    w=Webpage.objects.all()
    d={'webpages':w}
    return render(request,'webpage.html',d)


def access(request):
    a=Accessrecord.objects.all()
    d={'access':a}
    return render(request,'access.html',d)