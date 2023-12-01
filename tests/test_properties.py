from tests.libs import MyLiveServerTestCase, get_driver


class BaseTest(MyLiveServerTestCase):
    def setUp(self) -> None:
        self.driver = get_driver()

    def test_title(self) -> None:
        print(self.live_server_url)

        print()

        self.driver.get('http://0.0.0.0:8088')

        self.assertIn('Django', self.driver.title)
