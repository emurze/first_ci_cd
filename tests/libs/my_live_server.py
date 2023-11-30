import os
import socket as sock

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MyLiveServerTestCase(StaticLiveServerTestCase):
    # host = os.getenv('STAGING_SERVER', sock.gethostbyname(sock.gethostname()))
    host = 'localhost'
    port = 8081
