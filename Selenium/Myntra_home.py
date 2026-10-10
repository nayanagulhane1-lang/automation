#Install the latest version of ChromeDriver and set up Selenium WebDriver in your preferred language (Java, Python, or JavaScript) so that you can automate Chrome browser actions.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.myntra.com/")
time.sleep(3)

driver.quit()


