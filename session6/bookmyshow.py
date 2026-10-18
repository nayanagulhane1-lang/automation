#On the BookMyShow sign-up page, use find_element(By.NAME) to locate the mobile number
# input field and enter a sample phone number. Then, use find_element(By.TAG_NAME) to
# find the first 'button' element and print its text.

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://in.bookmyshow.com/login")
time.sleep(2)
driver.find_element(By.ID,"userMobileNumber").send_keys("9865434567")
time.sleep(2)
# Find the first button and print its text
button = driver.find_element(By.TAG_NAME, "button")
print("Button text:", button.text)
driver.quit()
