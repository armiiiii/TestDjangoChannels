import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatBuild.settings')

application = get_asgi_application()


import chat.routing


app = ProtocolTypeRouter({
    "http": application,
    "websocket": URLRouter(chat.routing.websocket_urlpatterns)
})
