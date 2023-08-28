import unittest
from utils.driver_setup import DriverSetUp
from src.common.actions import Actions
from src.pages.home_page import Home_page


class TestHP(DriverSetUp):
    """
    after import i can access DriverSetUp and TestCase
    """
    # which url am is under test
    URL = 'https://www.neuralnine.com'

    def setUp(self) -> None:
        print('setup')
        super().setUp()
        self.driver.get(self.URL)
        self.home_page = Home_page(self.driver)
        self.Actions = Actions(self.driver)

    def test_book_page_loads_from_home_page(self):
        self.home_page.click_books()
        current_url = self.Actions.current_url()
        assert current_url == 'https://www.neuralnine.com/books/'

    def test_2(self):
        pass
if __name__ == '__main__':
    unittest.main()
