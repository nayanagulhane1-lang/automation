from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://seleniumbase.github.io/demo_page/") 

driver.find_element(By.XPATH,"//button[@id='myButton']").click()
time.sleep(2)

driver.quit()