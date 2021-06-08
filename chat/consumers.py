from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = "group"

    async def receive_json(self, content, **kwargs):
        print(f"receive_json: {content}")
        command = content['command']

        if command == 'echo':
            await self.send_json(
                {
                    "type": "message",
                },
            )

    async def connect(self):
        print("connected")
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )
        await self.accept()

        await self.send_json({
            "join": "yes"
        })

    async def disconnect(self, code):
        print("disconnected")
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "leave",
                "message": "message"
            }
        )

    async def leave(self, event):
        print(event)
        await self.send_json({
            "leave": "yes"
        })




