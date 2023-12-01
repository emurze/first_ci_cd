from tests.libs import MyLiveServerTestCase, get_driver


class BaseTest(MyLiveServerTestCase):
    def setUp(self) -> None:
        self.driver = get_driver()

    def test_title(self) -> None:
        self.driver.get('https://github.com')

        self.driver.get('http://0.0.0.0:80')

        self.assertIn('Django', self.driver.title)
