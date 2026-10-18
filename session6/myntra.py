from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.myntra.com/login/password")
driver.find_element(By.ID,"mobileNumberPass").send_keys("henrytesting1@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("1234")
time.sleep(2)



driver.quit()