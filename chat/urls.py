from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chat'),
    path('chat<str:room_name>_<uid4>', views.room, name='room'),
]
