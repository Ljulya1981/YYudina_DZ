from selenium.webdriver.common.by import By
import allure


class PageAuth:

    def __init__(self, driver):
        """
        Конструктор страницы авторизации
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Открытие страницы интернет-магазина")
    def get_shop(self):
        """
        Открывает страницу авторизации интернет-магазина
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Введение имени пользователя на странице авторизации")
    def user_name(self):
        """
        Находит поле "Username" и вводит имя пользователя
        """
        username = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        username.send_keys("standard_user")

    @allure.step("Введение пароля на странице авторизации")
    def password(self):
        """
        Находит поле "Password" и вводит пароль
        """
        password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")

    @allure.step("Нажатие кнопки 'Login'")
    def click(self):
        """
        Находит кнопку "Login" и нажимает на нее
        """
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
