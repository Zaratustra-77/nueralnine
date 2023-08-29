from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.common.actions import Actions


class Home_page:

    def __init__(self, driver):
        """
        instantiate a driver for the class to be used in its functionality
        :param driver:
        """
        self.driver = driver



    def click_books(self) -> None:
        """
        click on th eBooks button
        :return:
        """
        # element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, 'menu-item-715')))
        Actions(self.driver).click_element('ID', 'menu-item-715')
        # element.click()

