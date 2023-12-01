import socket as sock

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MyLiveServerTestCase(StaticLiveServerTestCase):
    host = sock.gethostbyname(sock.gethostname())
    port = 8088
