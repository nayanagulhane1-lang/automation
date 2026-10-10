#Update your script to launch Microsoft Edge with Selenium, and explain the difference between driver.close() and driver.quit() by adding comments in your code where each is used.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.zomato.com")
time.sleep(3)
print(driver.title)
driver.quit() #close all tabs
#driver.close() #closes current tab
