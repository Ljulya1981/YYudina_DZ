from selenium.webdriver.common.by import By


class InputName:

    def __init__(self, driver):
        self.driver = driver

    def send(self, driver):
        firstname = self.driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
        firstname.send_keys("Иван")

        lastname = self.driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
        lastname.send_keys("Петров")

        address = self.driver.find_element(By.CSS_SELECTOR, "[name='address']")
        address.send_keys("Ленина, 55-3")

        email = self.driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
        email.send_keys("test@skypro.com")

        phonenumber = self.driver.find_element(By.CSS_SELECTOR, "[name='phone']")
        phonenumber.send_keys("+7985899998787")

        city = self.driver.find_element(By.CSS_SELECTOR, "[name='city']")
        city.send_keys("Москва")

        country = self.driver.find_element(By.CSS_SELECTOR, "[name='country']")
        country.send_keys("Россия")

        jobposition = self.driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
        jobposition.send_keys("QA")

        company = self.driver.find_element(By.CSS_SELECTOR, "[name='company']")
        company.send_keys("SkyPro")
