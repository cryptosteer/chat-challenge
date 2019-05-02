from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Room, Post
from .serializers import RoomSerializer, PostSerializer
from django.contrib.auth.decorators import login_required

@login_required
def index(request, room_id=None):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    if room_id:
        room = Room.objects.get(id=room_id)
        posts = Post.objects.filter(room=room).order_by('-created')[:50]
        context['room'] = room
        context['posts'] = posts
    return render(request, "chat.html", context)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
