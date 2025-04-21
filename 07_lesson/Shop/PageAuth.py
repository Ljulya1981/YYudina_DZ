from selenium.webdriver.common.by import By


class PageAuth:

    def __init__(self, driver):
        self.driver = driver

    def get_shop(self):
        self.driver.get("https://www.saucedemo.com/")

    def user_name(self, driver):
        username = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        username.send_keys("standard_user")

    def password(self, driver):
        password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")

    def click(self, driver):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
