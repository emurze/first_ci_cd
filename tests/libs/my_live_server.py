import os
import socket as sock

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MyLiveServerTestCase(StaticLiveServerTestCase):
    if os.getenv('STAGING_SERVER'):
        host = '0.0.0.0'
    else:
        host = sock.gethostbyname(sock.gethostname())
    port = 8088
