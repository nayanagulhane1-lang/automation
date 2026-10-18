#2.Write a Selenium script to find all elements with the class name 'btn' on the Flipkart homepage 
# using find_elements(By.CLASS_NAME), and print the text of each button found.<br><br><em><strong>Hint:</strong> Look for buttons like 'Login', 'Signup', or 'Cart'.</em>


from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.find_element(By.CLASS_NAME,"v1zwn28")
print("Login")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"v1zwn24")
print("Signup")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"v1zwn28")
print("Cart")
time.sleep(2)


driver.quit()