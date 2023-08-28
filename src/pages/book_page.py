from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.home_page_locators import home_page_locators as hpl

class Book_page:
    def __init__(self,driver):
        """
        instantiate a driver for the class to be used in its functionality
        :param driver:
        """
        self.driver = driver
