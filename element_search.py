import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# functions to interact with elements

def click_element(driver, locator, value):
    locator_type = getattr(By, locator)
    # returns
    elemnt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
    elemnt.click()


def get_url(driver, url_link):
    driver.get(url_link)


def click_books(driver) -> None:
    """
    click on th eBooks button
    :return:
    """

    click_element(driver, 'ID', 'menu-item-715')


def current_url(driver):
    return driver.current_url


# driver setup
def driver_setup():
    options = Options()
    service = Service(ChromeDriverManager().install())
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# driver actions:
options = Options()
service = Service(ChromeDriverManager().install())
options.add_experimental_option("detach", True)
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=service, options=options)

my_driver = driver_setup()
get_url(my_driver, 'https://www.neuralnine.com')
cu = my_driver.current_url
print(cu)
click_element(my_driver, 'ID', 'menu-item-715')
time.sleep(3)
my_driver.quit()
