import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class DataConsumer(WebsocketConsumer):

    def connect(self):
        self.id_device = self.scope['url_route']['kwargs']['id_device']
        self.group_name = self.id_device

        # Join sheet group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave sheet group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send sheet_name to sheet group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'send_confirmation',
                'message': text_data_json['message'],
                'code': text_data_json['code'],
                'data': text_data_json['data'],
            }
        )
        print("enviado consumer")

    # Receive message from sheet group
    def send_confirmation(self, event):
        # Send sheet_name to WebSocket
        self.send(text_data=json.dumps({
            'message': event['message'],
            'code': event['code'],
            'data': event['data'],
        }))

