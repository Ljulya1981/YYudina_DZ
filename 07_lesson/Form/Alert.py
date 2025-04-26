from selenium.webdriver.common.by import By


class Alert:

    def __init__(self, driver):
        self.driver = driver

    def alert_danger(self):
        zip_code_field = self.driver.find_element(By.CSS_SELECTOR, "#zip-code")
        return "alert-danger" in zip_code_field.get_attribute("class")

    def alert_success(self, class_attribut_success=None):
        first_name_field = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        return "alert-success" in first_name_field.get_attribute("class")

        last_name_field = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        return "alert-success" in last_name_field.get_attribute("class")

        address_field = self.driver.find_element(By.CSS_SELECTOR, "#address")
        return "alert-success" in address_field.get_attribute("class")

        email_field = self.driver.find_element(By.CSS_SELECTOR, "#e-mail")
        return "alert-success" in email_field.get_attribute("class")

        phone_number_field = self.driver.find_element(By.CSS_SELECTOR, "#phone")
        return "alert-success" in phone_number_field.get_attribute("class")

        city_field = self.driver.find_element(By.CSS_SELECTOR, "#city")
        return "alert-success" in city_field.get_attribute("class")

        country_field = self.driver.find_element(By.CSS_SELECTOR, "#country")
        return "alert-success" in country_field.get_attribute("class")

        job_position_field = self.driver.find_element(By.CSS_SELECTOR, "#job-position")
        return "alert-success" in job_position_field.get_attribute("class")

        company_field = self.driver.find_element(By.CSS_SELECTOR, "#company")
        return "alert-success" in company_field.get_attribute("class")
