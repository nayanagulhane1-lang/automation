from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://seleniumbase.github.io/demo_page/") 
time.sleep(2)

driver.find_element(By.ID,"myTextInput").send_keys("selebium Practice")

time.sleep(2)

driver.quit()
