import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from MainPage import MainPage
from InputName import InputName
from Submit import Submit
from Alert import Alert


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.implicitly_wait(10)
    driver.quit()


def test_form_submission(driver):
    main_page = MainPage(driver)
    main_page.get()

    input = InputName(driver)
    input.send(driver)

    click_button = Submit(driver)
    click_button.click(driver)

    alert = Alert(driver)
    class_attribut_danger = alert.alert_danger()
    class_attribut_success = alert.alert_success()

    assert class_attribut_danger == True
    assert class_attribut_success == True
