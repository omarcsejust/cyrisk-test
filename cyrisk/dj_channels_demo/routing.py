from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/connect/test-socket/routing', consumers.MySyncConsumer.as_asgi()),
]
