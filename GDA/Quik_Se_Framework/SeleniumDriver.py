from selenium import webdriver

import platform


class Selenium:
    win_path = "C:\\Program Files\\GoPro\\GpPro Quik.exe"
    # mac_path is default path and platform
    mac_path = "/Applications/GoPro Quik.app/Contents/MacOS/GoPro Quik"
    aut = mac_path
    driver = webdriver.Chrome
    host = "mac"
    ready = False
    chromedebug = False
    capabilities = None
    # webelement = webdriver.Chrome.find_element_by_name("").clear()
    # webelement = webdriver.Chrome.find_element_by_name("").click()
    # webelement = webdriver.Chrome.find_element_by_name("").get_attribute(name)
    # webelement = webdriver.Chrome.find_element_by_name("").get_property(name)
    # webelement = webdriver.Chrome.find_element_by_name("").id
    # webelement = webdriver.Chrome.find_element_by_name("").is_displayed()
    # webelement = webdriver.Chrome.find_element_by_name("").is_enabled()
    # webelement = webdriver.Chrome.find_element_by_name("").is_selected()
    # webelement = webdriver.Chrome.find_element_by_name("").send_keys()
    # webelement = webdriver.Chrome.find_element_by_name("").submit()
    # webelement = webdriver.Chrome.find_element_by_name("").text
    # webelement = webdriver.Chrome.find_element_by_name("").tag_name






    def __init__(self, app_path=None):
        Selenium.init(app_path)

    @staticmethod
    def init(app_path=None):
        Selenium.host = platform.system()
        if app_path:  #overide default AUT path
            Selenium.aut = app_path
        elif Selenium.host == "Windows":  #detect & switch to windows default path
            Selenium.aut = Selenium.win_path
        try:  # Invoke the Quik App
            chromeOptions = webdriver.ChromeOptions()
            if Selenium.chromedebug:
                chromeOptions.add_argument("-webdebug")
            chromeOptions.binary_location = Selenium.aut
            Selenium.driver = webdriver.Chrome(chrome_options=chromeOptions)
            if Selenium.driver:  # need to add validation
                Selenium.capabilities = Selenium.driver.capabilities
                if Selenium.capabilities:
                    Selenium.ready = True
                    print str(Selenium.capabilities)
        except Exception as err:
            print str(err)


# import time
# def test_selenium_class():
#     Selenium()
#     print str(Selenium)
#     time.sleep(10)
#     for i in range(10):
#         Selenium.driver.find_element_by_class_name("button-play-pause").click()
#         time.sleep(5)
#
#         txt = Selenium.driver.find_element_by_class_name("GoProUIHlsTimecode").text
#
#         print txt
#         Selenium.driver.find_element_by_class_name("button-play-pause").click()
#     time.sleep(2)
#     Selenium.driver.quit()
#
# test_selenium_class()
#
