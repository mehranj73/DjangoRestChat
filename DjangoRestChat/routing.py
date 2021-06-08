from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path
from .auth import JWTAuthMiddlewareStack
from django.core.asgi import get_asgi_application

from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    #  "http": get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        JWTAuthMiddlewareStack(
            URLRouter([
                path('chat/<room_id>/', ChatConsumer.as_asgi()),
            ])
        )
    ),
})
