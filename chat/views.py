from django.shortcuts import render, redirect
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
    if not room_id:
        room_id = Room.objects.all()[0:1].get().id
    room = Room.objects.get(id=room_id)
    posts = Post.objects.filter(room=room).order_by('-created')[:50]
    context['room'] = room
    context['posts'] = posts
    return render(request, "chat.html", context)


@login_required
def post_message(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        room_id = request.POST['room_id']
        message = request.POST['message']
        room = Room.objects.get(pk=room_id)
        post = Post.objects.create(room=room, message=message, author=request.user)
        post.save()
        return redirect('index_room', room_id=room_id)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
