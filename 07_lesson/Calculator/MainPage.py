class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_calc(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
