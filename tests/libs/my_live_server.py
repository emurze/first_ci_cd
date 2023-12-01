import os
import socket as sock

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MyLiveServerTestCase(StaticLiveServerTestCase):
    if not os.getenv('STAGING_SERVER'):
        host = sock.gethostbyname(sock.gethostname())

    port = 8088
