import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.implicitly_wait(10)
    driver.quit()

def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    firstname = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    firstname.send_keys("Иван")

    lastname = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    lastname.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email.send_keys("test@skypro.com")

    phonenumber = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phonenumber.send_keys("+7985899998787")

    city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country.send_keys("Россия")

    jobposition = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
    jobposition.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company.send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type=submit").click()

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    first_name_field = driver.find_element(By.CSS_SELECTOR, "#first-name")
    assert "alert-success" in first_name_field.get_attribute("class")

    last_name_field = driver.find_element(By.CSS_SELECTOR, "#last-name")
    assert "alert-success" in last_name_field.get_attribute("class")

    address_field = driver.find_element(By.CSS_SELECTOR, "#address")
    assert "alert-success" in address_field.get_attribute("class")

    email_field = driver.find_element(By.CSS_SELECTOR, "#e-mail")
    assert "alert-success" in email_field.get_attribute("class")

    phone_number_field = driver.find_element(By.CSS_SELECTOR, "#phone")
    assert "alert-success" in phone_number_field.get_attribute("class")

    city_field = driver.find_element(By.CSS_SELECTOR, "#city")
    assert "alert-success" in city_field.get_attribute("class")

    country_field = driver.find_element(By.CSS_SELECTOR, "#country")
    assert "alert-success" in country_field.get_attribute("class")

    job_position_field = driver.find_element(By.CSS_SELECTOR, "#job-position")
    assert "alert-success" in job_position_field.get_attribute("class")

    company_field = driver.find_element(By.CSS_SELECTOR, "#company")
    assert "alert-success" in company_field.get_attribute("class")
