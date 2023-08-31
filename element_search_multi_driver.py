import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Functions to interact with elements
def click_element(driver, locator, value):
    locator_type = getattr(By, locator)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
    element.click()


def get_url(driver, url_link):
    driver.get(url_link)


def click_books(driver):
    click_element(driver, 'ID', 'menu-item-715')


# Driver setup for Chrome
def chrome_driver_setup():

    options = Options()
    service = Service(ChromeDriverManager().install())
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# Driver setup for Firefox
def firefox_driver_setup():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.set_preference("extensions.disabled", True)
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)
    return driver


# Driver setup for Edge

def edge_driver_setup():

    edge_options = webdriver.EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("--disable-extensions")
    service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=edge_options)
    return driver


# Modify this line to use the driver you want
my_chrome_driver = chrome_driver_setup()  # Replace with firefox_driver_setup() or edge_driver_setup() based on your needs
my_firefox_driver = firefox_driver_setup()
my_edge_driver = edge_driver_setup()


get_url(my_chrome_driver, 'https://www.neuralnine.com')
get_url(my_firefox_driver, 'https://www.neuralnine.com')
get_url(my_edge_driver, 'https://www.neuralnine.com')


# Perform actions using Chrome driver
get_url(my_chrome_driver, 'https://www.google.com')
# element = my_chrome_driver.find_element(By.ID, "menu-item-715").click()

time.sleep(10)
my_chrome_driver.close()
my_chrome_driver.quit()


# Perform actions using Firefox driver
# get_url(my_firefox_driver, 'https://www.neuralnine.com')
# click_books(my_firefox_driver)
# time.sleep(3)
# my_firefox_driver.close()
# my_firefox_driver.quit()

# Perform actions using Edge driver
# get_url(my_edge_driver, 'https://www.neuralnine.com')
# click_books(my_edge_driver)
# time.sleep(3)
# my_edge_driver.close()
# my_edge_driver.quit()
