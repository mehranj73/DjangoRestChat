from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = "group"

    async def receive_json(self, content, **kwargs):
        print(content)
        command = content['command']

        if command == 'echo':
            await self.send_json(
                {
                    "type": "message",
                },
            )

    async def connect(self):
        await self.channel_layer.group_add(
            "room.group_name",
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, code):
        pass
