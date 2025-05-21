from selenium.webdriver.common.by import By
import allure


class MainPage:

    def __init__(self, driver):
        """
        Конструктор главной страницы интернет-магазина
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Выбор товара")
    def select(self):
        """
        Находим на странице кнопки выбора товаров labs-backpack,
        labs-bolt-t-shirt и labs-onesie и нажимаем на них
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        ).click()

    @allure.step("Переход в корзину")
    def cart_link(self):
        """
        Нажимаем на значок корзины и переходим в нее
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()
