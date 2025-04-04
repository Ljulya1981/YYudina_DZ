from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

div_label = driver.find_element(By.CSS_SELECTOR, 'input#username')
div_label.send_keys("tomsmith")

div_label = driver.find_element(By.CSS_SELECTOR, 'input#password')
div_label.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CSS_SELECTOR, 'i')
button.click()

div_messages = driver.find_element(By.CSS_SELECTOR, 'div#flash.flash.success').text
print(div_messages)

driver.quit()
