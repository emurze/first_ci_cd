from tests.libs import MyLiveServerTestCase, get_driver


class BaseTest(MyLiveServerTestCase):
    def setUp(self) -> None:
        self.driver = get_driver()

    def test_title(self) -> None:
        print(self.live_server_url)

        self.driver.get(self.live_server_url)

        self.assertIn('Django', self.driver.title)
