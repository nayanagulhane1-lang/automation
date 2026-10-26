from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://seleniumbase.github.io/demo_page/") 

inputs=driver.find_elements(By.TAG_NAME,"input")
print("Total input element:",len(inputs))

for element in inputs:
    print("Input type:", element.get_attribute("type"))


time.sleep(2)

driver.quit()