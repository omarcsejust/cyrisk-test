"""
ASGI config for cyrisk project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import cyrisk.dj_channels_demo.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyrisk.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        cyrisk.dj_channels_demo.routing.websocket_urlpatterns
    ),
})

