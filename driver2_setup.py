import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_element(driver, locator, value):
    locator_type = getattr(By, locator)  # returns
    elemnt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
    elemnt.click()

def click_books(driver) -> None:
    """
    click on th eBooks button
    :return:
    """
    # element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, 'menu-item-715')))
    click_element(driver, 'ID', 'menu-item-715')
    # element.click()

def current_url():
    return driver.current_url

options = Options()
service = Service(ChromeDriverManager().install())
options.add_experimental_option("detach", True)
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.neuralnine.com')
cu = driver.current_url
print(cu)
click_books(driver)

time.sleep(3)
driver.quit()


