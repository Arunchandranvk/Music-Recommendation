# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EmotionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def emotion_message(self, event):
        emotion = event['emotion']
        await self.send(text_data=json.dumps({
            'emotion': emotion
        }))
