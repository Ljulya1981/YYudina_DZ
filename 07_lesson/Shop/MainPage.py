from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def set_cookie(self):
        my_cookies = {
             'name': 'session-username',
             'value': 'standard_user',
             'secure': False,
             'httpOnly': False,
             'path': '/',
             'samSite': 'Lax'
         }
        self.driver.add_cookie(my_cookies)

    def select(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def cart_link(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
