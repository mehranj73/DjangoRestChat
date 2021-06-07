from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def receive_json(self, content, **kwargs):
        return await super().receive_json(content, **kwargs)

    async def send_json(self, content, close=False):
        return await super().send_json(content, close)

    async def connect(self):
        return await super().connect()