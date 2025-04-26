import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from PageAuth import PageAuth
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.implicitly_wait(10)
    driver.quit()


def test_full_purchase_flow(driver):
    auth = PageAuth(driver)
    auth.get_shop()
    auth.user_name(driver)
    auth.password(driver)
    auth.click(driver)

    main_page = MainPage(driver)
    main_page.set_cookie()
    main_page.select()
    main_page.cart_link()

    cart_page = CartPage(driver)
    counter = cart_page.check(driver)
    assert counter == 3

    cart_page.get_checkout()

    order_page = OrderPage(driver)
    order_page.send(driver)
    order_page.cont()
    order_page.result()
    total_result = order_page.result()
    assert total_result == "Total: $58.29"

    order_page.close()
