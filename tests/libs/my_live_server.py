import os
import socket

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MyLiveServerTestCase(StaticLiveServerTestCase):
    host = os.getenv(
        'STAGE_SERVER',
        socket.gethostbyname(socket.gethostname())
    )
    port = 8081
