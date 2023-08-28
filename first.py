from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.driver_setup import DriverSetUp,By

# to get an address
my_driver = DriverSetUp().setup('https://www.neuralnine.com') # returns a webdriver object
# my_driver.get('https://www.neuralnine.com')
# my_driver.maximize_window()

links = my_driver.find_elements(By.XPATH,"//a[@href]")
print(links)
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        href_value = link.get_attribute("href")
        # Wait for the link to be clickable
        WebDriverWait(my_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@href='{href_value}']"))
        )

        # Re-find the link and click on it
        my_driver.find_element(By.XPATH, f"//a[@href='{href_value}']").click()
        break  # Exit the loop once the link is found and clicked
