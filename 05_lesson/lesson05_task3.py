from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

div_exampl = driver.find_element(By.CSS_SELECTOR, 'input')
div_exampl.send_keys("Sky")

sleep(5)

div_exampl.clear()

sleep(5)

div_exampl.send_keys("Pro")

sleep(5)

driver.quit()
