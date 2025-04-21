from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultCalc:

    def __init__(self, driver):
        self.driver = driver

    def get_result(self, driver, result=None):
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result
