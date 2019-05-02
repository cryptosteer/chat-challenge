from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'rooms', views.RoomViewSet)
router.register(r'posts', views.PostViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>', views.index, name='index_room'),
    path('api/', include(router.urls)),
]
