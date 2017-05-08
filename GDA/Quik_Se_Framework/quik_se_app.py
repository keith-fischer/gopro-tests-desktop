import quik_se_signin
import quik_se_createacct
import quik_se_media
import quik_se_appnav
import SeleniumDriver

class QuikSeApp():
    def __init__(self):
        self.driver = SeleniumDriver.Selenium.init()