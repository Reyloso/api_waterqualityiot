from api_waquanet.consumers import (DataConsumer)
from django.urls import path, re_path, include

from django.conf.urls import url

websocket_urlpatterns = [
    path('measurement/send/<id_device>', DataConsumer.as_asgi()),
]