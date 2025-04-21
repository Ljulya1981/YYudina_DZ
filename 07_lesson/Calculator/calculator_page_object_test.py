import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from MainPage import MainPage
from InputDelay import InputDelay
from ButtonCalc import ButtonCalc
from ResultCalc import ResultCalc


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    main_page = MainPage(driver)
    main_page.get_calc()

    input = InputDelay(driver)
    input.input_delay('45')

    click = ButtonCalc(driver)
    click.click_button()

    result = ResultCalc(driver)
    result_txt = result.get_result(driver)

    assert result_txt == "15"
