from channels.generic.websocket import WebsocketConsumer

# calling aync functions from synchronus code requires this...
from asgiref.sync import async_to_sync

class NoticeConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('users', self.channel_name)
        self.accept()
        self.send(text_data="accepted")

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            "users",
            {
                "type": "user.message",
                "text": 'Broadcasting: {}'.format(text_data),
            },
        )

    def user_message(self, event):
        self.send(text_data=event['text'])

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)('users', self.channel_name)


    '''
    async def connect(self):
        print("DBG: Connection made .....")
        await self.accept()

    async def recieve_json(self, content):
        command = content.get("command", None)
        print("DBG: {}".format(content.toString()))
        self.send_json({'YouWant': hello})

    async def disconnect(self, code):
        self.send_json({"message": "bye"})
    '''
