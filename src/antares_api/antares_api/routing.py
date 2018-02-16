from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from django.urls import path
from websockets import consumers

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    "websocket": SessionMiddlewareStack(
        URLRouter([
            path("users/", consumers.NoticeConsumer)
        ])
    )
})
