from selenium.webdriver.support import expected_conditions as EC #
from selenium.webdriver.common.by import By # no idea -> research online -> ask teacher
from selenium.webdriver.support.wait import WebDriverWait # no idea -> research online -> ask teacher



class Actions: # creating a class Actions
    def __init__(self,driver): # initializes certain attributes when creating a class object
        """
        instantiate a driver for the class to be used in its functionality
        :param driver:
        """
        self.driver = driver

    def current_url(self):
        return self.driver.current_url

    def get_menu_items(self):
        """

        :return:
        """
        menu_items = self.driver.find_elementS(By.ID, 'menu-navigation').find_elements(By.XPATH, './/li')
        menu_list = []

        for item in menu_items:
            menu_id = item.get_attribute('id')
            menu_class = item.get_attribute('class')
            menu_list.append({'id': menu_id, 'class': menu_class})

        return menu_list

    def click_element(self,locator,value):
        locator_type = getattr(By, locator) # returns
        elemnt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
        elemnt.click()

