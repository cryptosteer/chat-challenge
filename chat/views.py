from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Room, Post
from .serializers import RoomSerializer, PostSerializer
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "chat.html", {})


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer