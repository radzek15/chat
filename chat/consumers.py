import datetime
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = str(self.scope['user'])
        now_time = datetime.datetime.now().strftime(settings.DATETIME_FORMAT)

        if not message:
            return
        if not self.scope['user'].is_authenticated:
            return

        Message.objects.create(user=self.scope['user'], message=message, group_name=self.room_group_name)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
                'now_time': now_time
            }
        )

    async def chat_message(self, event):
        message = event['message']
        now_time = event['now_time']
        user = event['user']

        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'now_time': now_time,
        }))
