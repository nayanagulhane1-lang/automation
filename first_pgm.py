import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(5)
print(driver.current_url)
print(driver.title)
# driver.close()
driver.quit()