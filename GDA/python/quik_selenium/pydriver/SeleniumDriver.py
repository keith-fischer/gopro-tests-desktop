from selenium import webdriver
import os
import platform
import time
class Selenium():
    win_path=""
    mac_path = "/Applications/GoPro Quik.app/Contents/MacOS/GoPro Quik"
    aut=mac_path
    driver = None
    host = "mac"

    @staticmethod
    def init(app_path=None):
        host=platform.system()
        if app_path:
            Selenium.aut=app_path
        elif host == "Windows":
            Selenium.aut = win_path
        try:
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.binary_location = Selenium.aut
            Selenium.driver = webdriver.Chrome(chrome_options=chromeOptions)
        except Exception as err:
            print str(err)



def test_selenium_class():
    Selenium.init()
    print str(Selenium)

    time.sleep(10)

    txt=Selenium.driver.find_element_by_class_name("GoProUIHlsTimecode").text

    print txt
    Selenium.driver.quit()

#test_selenium_class()