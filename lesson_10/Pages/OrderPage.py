from selenium.webdriver.common.by import By
import allure


class OrderPage:

    def __init__(self, driver):
        """
        Конструктор страницы оформления покупки
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Введение имени, фамилии покупателя и его почтового индекса")
    def send(self):
        """
        Вводим данные покупателя "First Name", "Last Name", "Postal Code"
        """
        first_name = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys("Юлия")

        last_name = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys("Юдина")

        postal_code = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code.send_keys("456200")

    @allure.step("Нажатие на кнопку 'Continue'")
    def cont(self):
        """
        Находим кнопку "Continue" и нажимаем на нее
        """
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Нахождение на странице итоговой суммы покупки")
    def result(self):
        """
        Находим итоговую сумму (итоговая стоимость покупки)
        :return: str
        """
        total = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label"
        ).text
        return total

    @allure.step("Нажатие на кнопку 'Finish'")
    def close(self):
        """
        Находим кнопку "Finish" и нажимаем на нее
        """
        self.driver.find_element(By.CSS_SELECTOR, "#finish").click()
