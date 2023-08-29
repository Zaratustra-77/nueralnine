# unittest related imports
import unittest
from unittest import TestCase
# selenium related imports:
from selenium import webdriver  # will be used to to create an object that navigates ws.
from selenium.webdriver.chrome.service import Service  # creates a Service object (instance) wo points to the driver
# the webdriver.exe location.
from selenium.webdriver.chrome.options import Options  # creates a Options object (instance) that deals
# with different interact behavioural actions

from webdriver_manager.chrome import ChromeDriverManager  # to instantiate a new driver.exe or cached for the session


class DriverSetUp(TestCase):

    def setUp(self) -> None:
        options = Options()
        service = Service(ChromeDriverManager().install())
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(service=service, options=options)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
