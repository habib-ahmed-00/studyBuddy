from django.shortcuts import render
from .models import *



def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    rooms = Room.objects.get(id=pk)
    context = {
        'room': rooms
    }
    return render(request, 'base/room.html', context)