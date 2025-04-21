class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def get(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
