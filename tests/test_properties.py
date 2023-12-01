import os

from tests.libs import MyLiveServerTestCase, get_driver


class BaseTest(MyLiveServerTestCase):
    def setUp(self) -> None:
        self.driver = get_driver()

    def test_title(self) -> None:
        print(f'\n\n{"-" * 200}\n')
        print(self.live_server_url)
        print(os.system('netstat -tulpn | grep LISTEN'))
        print(f'\n{"-" * 200}\n\n')

        self.driver.get(self.live_server_url)

        self.assertIn('Django', self.driver.title)
