import os
import socket as sock

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MyLiveServerTestCase(StaticLiveServerTestCase):
    host = os.getenv('STAGE_SERVER', sock.gethostbyname(sock.gethostname()))
    port = 8081
