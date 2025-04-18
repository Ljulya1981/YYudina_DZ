from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )
driver.implicitly_wait(10)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images")

award = driver.find_element(By.CSS_SELECTOR, "img#award")

print(award.get_attribute("src"))

driver.quit()
