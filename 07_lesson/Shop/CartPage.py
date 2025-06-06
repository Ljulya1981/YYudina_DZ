from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def check(self, driver):
        products = self.driver.find_elements(By.CSS_SELECTOR, "div.cart_quantity")
        return len(products)

    def get_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
