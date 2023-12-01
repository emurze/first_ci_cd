import os
import socket as sock

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MyLiveServerTestCase(StaticLiveServerTestCase):
    # if os.getenv('STAGING_SERVER'):
    #     host = 'localhost'
    # else:
    host = sock.gethostbyname(sock.gethostname())
    port = 8088
