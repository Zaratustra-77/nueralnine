import unittest

from selenium.webdriver.common.by import By

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
        print('Test setup')
        super().setUp()
        self.driver.get(self.URL)
        self.home_page = Home_page(self.driver)
        self.Actions = Actions(self.driver)

    def test_1_book_page_loads_from_home_page(self):
        self.home_page.click_books()
        current_url = self.Actions.current_url()
        assert current_url == 'https://www.neuralnine.com/books/'

    # how to configure more names for unittest

    def test_logo(self):
        # Locate the logo element by its ID or any other attribute
        logo_link = self.Actions.find_element('CLASS_NAME','clr')
        logo_element = self.Actions.find_element('ID', 'site-logo-inner')  # Replace 'logo-id' with actual ID or attribute
        logo_location = logo_element.location # is a dict
        print(logo_location)
        # Assert visibility
        self.assertTrue(logo_element.is_displayed())
        home_element = self.Actions.find_element('ID', 'menu-item-97')
        home_location = home_element.location
        print(home_location)
        self.assertTrue(home_location['x'] > logo_location['x'])
        # self.assertEqual(self.driver.current_url,'https://www.neuralnine.com/')


        # href = logo_link.get_attribute('href')
        # self.assertEqual(href, 'https://www.neuralnine.com/')  # Replace with the expected href
        # className = logo_element.get_attribute('className')
        # self.assertEqual(className,"custom-logo")


        # Assert clickability by actually clicking
        # logo_element.click()

if __name__ == '__main__':
        unittest.main()
