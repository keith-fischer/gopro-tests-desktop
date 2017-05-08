
from selenium import webdriver


class WebDriver():
    def __init__(self, autpath):
        self.aut_path=autpath
        self.driver=self.driverinit()
        if self.driver:

    def driverinit(self):
        try:
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.binary_location = self.aut_path
            return webdriver.Chrome(chrome_options=chromeOptions)
        except Exception:
            print Exception.message
            print Exception.args
            print Exception

    def getTitle(self):
        self.driver.title