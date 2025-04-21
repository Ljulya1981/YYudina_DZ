from selenium.webdriver.common.by import By


class Submit:

    def __init__(self, driver):
        self.driver = driver

    def click(self, driver):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit").click()
