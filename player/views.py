from django.shortcuts import render, get_object_or_404

from .models import Room


def index(request):
    return render(request, 'player/index.html')


def room(request, room_id):
    room = get_object_or_404(Room.objects.all(), pk=room_id)
    return render(request, 'player/room.html', {
        room_id: room.id
    })