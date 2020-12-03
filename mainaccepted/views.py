from django.shortcuts import render
from .models import Events
from django.shortcuts import HttpResponse


def index(request):
    return render(request, 'accepted/index.html')

def successs(request):
    return render(request, 'accepted/stories.html')

def places(request):
    return render(request, 'accepted/places.html')

def events(request):
    events = Events.objects.all()
    context = {
        'events': events
    }
    return render(request, 'accepted/events.html', context)

def about(request):
    return render(request, 'accepted/about.html')