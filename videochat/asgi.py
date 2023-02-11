import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from video.consumers import VideoChat
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VideoChat.settings')

application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
        URLRouter([
            path('ws/',VideoChat)
        ])
    )
})