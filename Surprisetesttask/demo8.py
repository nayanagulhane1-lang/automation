from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
driver.get("https://seleniumbase.github.io/demo_page/") 
time.sleep(2)

checkboxes=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
print("Total checkboxes:", len(checkboxes))

for checkbox in checkboxes:
    if checkbox.is_enabled():
        if not checkbox.is_selected():
            checkbox.click()

        print("Checkbox selected:", checkbox.is_selected())

time.sleep(2)

driver.quit()