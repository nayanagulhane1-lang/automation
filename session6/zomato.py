#Navigate to the Zomato homepage and use find_element(By.LINK_TEXT) 
# to locate the 'Add restaurant' link, then click it using Selenium WebDriver.

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.zomato.com/surat/collections")

main_w=driver.current_window_handle
print(main_w)

driver.find_element(By.PARTIAL_LINK_TEXT,"Fan").click()
time.sleep(2)
all_w=driver.window_handles
print(all_w)
time.sleep(2)

for child_w in all_w:
    if child_w!=main_w:
        driver.switch_to.window(child_w)
        time.sleep(2)
        print("child window:"+child_w)
        driver.find_element(By.CLASS_NAME,"sc-bCQtTp idzkjU")
        time.sleep(5)
        driver.close()
        time.sleep(2)
driver.switch_to.window(main_w)
current_w=driver.current_window_handle
print("current window :"+current_w)
time.sleep(2)

driver.quit()