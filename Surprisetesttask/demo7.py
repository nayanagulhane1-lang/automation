from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
driver.get("https://seleniumbase.github.io/demo_page/") 
time.sleep(2)


checkbox=driver.find_element(By.CSS_SELECTOR,"#checkBox2")
print(checkbox.is_selected())



time.sleep(2)

driver.quit()