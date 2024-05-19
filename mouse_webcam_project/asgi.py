import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path

from mouse_webcam_project.main import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mouse_webcam_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/mouse/$', consumers.MouseWebcamConsumer.as_asgi()),
        ])
    ),
})
