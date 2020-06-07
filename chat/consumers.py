import json
import random
import string

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser

x = ''.join(random.choice(string.digits) for _ in range(5))


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Receive message from websocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        status = 'OK'
        try:
            user = self.user.username
        except:
            # Error to handle anonymous user
            user = x

        try:
            message = text_data_json["message"]
        except KeyError:
            message = 'Typo in message !!!'
            status = "ERROR"

        # Send message from websocket
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message",
                "message": message,
                "status": status,
                "user": user
            }
        )

        # Receive message from room group

    async def chat_message(self, event):
        message = event["message"]
        status = event["status"]
        user = event["user"]
        # Send message to websocket
        await self.send(text_data=json.dumps({"message": message, "user": user}))
