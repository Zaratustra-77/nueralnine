from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


chromedriver_path = "C:/Webdrivers/chromedriver.exe"
options = webdriver.ChromeOptions()
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.neuralnine.com')
title = driver.title
url = driver.current_url
# username_input_field = driver.find_element(By.ID,'username').send_keys('student')
time.sleep(4)
print(title,url)
driver.close()
# assert title == 'Test Login | Practice Test Automation', 'wrong title'