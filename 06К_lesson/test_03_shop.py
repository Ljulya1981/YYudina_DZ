from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")

user = driver.find_element(By.CSS_SELECTOR, "#user-name")
user.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")

driver.find_element(By.CSS_SELECTOR, "#login-button").click()

my_cookies = {
     'name': 'session-username',
     'value': 'standard_user',
     'secure': False,
     'httpOnly': False,
     'path': '/',
     'samSite': 'Lax'
}
driver.add_cookie(my_cookies)

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()


driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

driver.find_element(By.CSS_SELECTOR, "#checkout").click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Юлия")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Юдина")

postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
postal_code.send_keys("456200")

driver.find_element(By.CSS_SELECTOR, "#continue").click()

total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
print(total)

driver.find_element(By.CSS_SELECTOR, "#finish").click()

assert total == "Total: $58.29"
