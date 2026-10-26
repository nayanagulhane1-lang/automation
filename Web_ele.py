from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
#driver.get("https://demo.guru99.com/test/radio.html") #radio and checkox selection
#driver.get("https://the-internet.herokuapp.com/multiple_dropdown")#multidrodown site
#driver.get("https://testautomationcentral.com/demo/multi_select_dropdown.html") 
#driver.get("https://the-internet.herokuapp.com/add_remove_elements/") #add remove cta
#driver.get("https://demo.guru99.com/test/newtours/register.php") #single dropdown option select
#driver.get("https://the-internet.herokuapp.com/upload") #file 
driver.get("https://the-internet.herokuapp.com/radio_buttons") #radio selected



time.sleep(2)
# radio=driver.find_element(By.ID,"vfb-7-1")
# print(radio.is_selected())
# radio.click()
# print(radio.is_enabled())
# time.sleep(2)

#checkbox selection
# checkbox=driver.find_element(By.ID,"vfb-6-0")
# print(checkbox.is_selected())
# checkbox.click()
# print(checkbox.is_selected())
# time.sleep(2)

#2nd example
#id=checkbox=driver.find_element(By.ID,"dropdown-toggle").click()
# print(checkbox.is_selected())
# checkbox.click()
# print(checkbox.is_selected())

#below checkbox not selected 
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@value='Apple']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@value='Cherry']").click()
# time.sleep(2)
###not works below
# checkbox.select_by_value("Apple")
# checkbox.select_by_index("3")
# checkbox.select_by_visible_text("Cherry")
time.sleep(2)

#multiple dropdown select site now open
# dropdown=Select(driver.find_element(By.ID,"multiple-dropdown"))
# time.sleep(2)
# dropdown.select_by_index(0)
# time.sleep(5)
# dropdown.select_by_value("2")
# time.sleep(2)
# dropdown.select_by_visible_text("Option 3")
# time.sleep(2)

# webele=Select(driver.find_element(By.NAME,"country"))
# time.sleep(5)
# webele.select_by_index(3)
# time.sleep(5)
# webele.select_by_value("AUSTRALIA")
# time.sleep(2)
# webele.select_by_visible_text("VIETNAM")
# time.sleep(2)


#add remove cta
# driver.find_element(By.XPATH,"//*[@id='content']/div/button").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='elements']/button").click()
# time.sleep(2)

#file upload
#driver.find_element(By.XPATH,"//*[@id='file-submit']").click()

#radio button select
driver.find_element(By.ID,"red").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='blue']").click()
time.sleep(2)
driver.find_element(By.NAME,"sport").click()

time.sleep(2)
driver.quit()
