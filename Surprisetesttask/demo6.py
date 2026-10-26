from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
driver.get("https://seleniumbase.github.io/demo_page/") 

time.sleep(2)

radio = driver.find_element(By.CSS_SELECTOR, "input[type='radio']")
print(radio.is_selected())

time.sleep(2)

driver.quit()