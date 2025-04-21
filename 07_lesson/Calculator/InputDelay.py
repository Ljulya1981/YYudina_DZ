from selenium.webdriver.common.by import By


class InputDelay:

    def __init__(self, driver):
        self.driver = driver

    def input_delay(self, time):
        input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        input.clear()
        input.send_keys(time)
