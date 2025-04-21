from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def send(self, driver):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys("Юлия")

        last_name = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys("Юдина")

        postal_code = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code.send_keys("456200")

    def cont(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def result(self):
        total = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return total

    def close(self):
        self.driver.find_element(By.CSS_SELECTOR, "#finish").click()
