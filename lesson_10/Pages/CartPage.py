from selenium.webdriver.common.by import By
import allure


class CartPage:

    def __init__(self, driver):
        """
        Конструктор страницы "Корзина"
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Подсчет количества товаров в корзине")
    def check(self):
        """
        Подсчитываем количество товаров в корзине
        :return: int
        """
        products = self.driver.find_elements(
            By.CSS_SELECTOR, "div.cart_quantity"
        )
        return len(products)

    @allure.step("Нажатие на кнопку 'Checkout'")
    def get_checkout(self):
        """
        Находим кнопку "Checkout" и нажимаем на нее
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
