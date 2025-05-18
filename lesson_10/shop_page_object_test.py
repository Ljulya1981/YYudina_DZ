import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Pages.PageAuth import PageAuth
from Pages.MainPage import MainPage
from Pages.CartPage import CartPage
from Pages.OrderPage import OrderPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершении работы драйвера
    """
    driver = webdriver.Firefox(
        service=FirefoxService(
            GeckoDriverManager().install()))
    yield driver
    driver.implicitly_wait(10)
    driver.quit()


@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет работоспособность интернет-магазина")
@allure.feature("Интернет-магазин")
@allure.severity("allure.severity_level.CRITICAL")
def test_full_purchase_flow(driver):
    """
    Тест проверяет работоспособность интернет-магазина
    (авторизация,
    выбор товара,
    проверка количества выбранных товаров в корзине,
    подсчет итоговой суммы покупки,
    введение данных покупателя и др.)
    :param driver: WebDriver — объект драйвера Selenium
    """
    auth = PageAuth(driver)

    with allure.step("Открытие страницы интеренет-магазина"):
        auth.get_shop()

    with allure.step("Введение имени пользователя на странице авторизации"):
        auth.user_name(driver)

    with allure.step("Введение пароля на странице авторизации"):
        auth.password(driver)

    with allure.step("Нажатие кнопки 'Login'"):
        auth.click(driver)

    main_page = MainPage(driver)

    with allure.step("Выбор товара"):
        main_page.select()

    with allure.step("Переход в корзину"):
        main_page.cart_link()

    cart_page = CartPage(driver)

    with allure.step(
            "Подсчет количества товаров в корзине + проверка на соответствие"
    ):
        counter = cart_page.check(driver)
        assert counter == 3

    with allure.step("Нажатие на кнопку 'Checkout'"):
        cart_page.get_checkout()

    order_page = OrderPage(driver)

    with allure.step(
            "Введение имени, фамилии покупателя и его почтового индекса"
    ):
        order_page.send(driver)

    with allure.step("Нажатие на кнопку 'Continue'"):
        order_page.cont()

    with allure.step(
            "Нахождение на странице итоговой суммы покупки "
            "+ проверка на соответствие"
    ):
        total_result = order_page.result()
        assert total_result == "Total: $58.29"

    with allure.step("Нажатие на кнопку 'Finish'"):
        order_page.close()
