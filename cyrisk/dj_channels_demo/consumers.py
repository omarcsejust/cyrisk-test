from channels.consumer import SyncConsumer, AsyncConsumer
from channels.generic.websocket import WebsocketConsumer


class MySyncConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket connected: ")

    def receive(self, text_data):
        print("Message received: ")

    def disconnect(self, close_code):
        print("Websocket disconnected: ", close_code)


