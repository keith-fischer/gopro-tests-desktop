
import os
import time
# import base64
# import httplib
# from selenium.webdriver.remote.command import Command
# from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.proxy import Proxy

from selenium import webdriver

def doclick(classname):
    print "doclick: %s" % classname
    time.sleep(1)
    btn = driver.find_element_by_class_name(classname)
    if btn:
        btn.click()
        print "PASSED Click: %s" % classname
        return True
    else:
        print "ERROR: Not found:%s" % classname
        exit(-1)
        return False

def intToTimeFormat(secs):
    n1=secs%60
    n2=secs/60
    return "%01d:%02d" % (n2,n1)

def uiTimeToSec(strtime):
    items=strtime.split(":")
    n1=int(items[0])*60
    n2=n1+int(items[1])
    return n2
def calctime(numint_secs):
    mins= numint_secs/60


def checktimecodeplayer():
    dur = driver.find_element_by_class_name("GoProUIHlsDuration").text
    max = uiTimeToSec(dur)
    secs = uiTimeToSec(driver.find_element_by_class_name("GoProUIHlsTimecode").text)
    half=max/2
    elapsed = 0
    while secs < max:
        secs = uiTimeToSec(driver.find_element_by_class_name("GoProUIHlsTimecode").text)
        if secs>half:
            print "Half way %.2f" % half
            doclick("button-play-pause")
            time.sleep(5)
            doclick("button-play-pause")
            half=max
        start = time.time()

        if elapsed > 3:
            print "Test: %s|%s - %s - %.2f" % (secs, dur, "FAILED", elapsed)
        else:
            print "Test: %s|%s - %s - %.2f" % (secs, dur, "PASSED", elapsed)

        if secs == max:
            break
        while(uiTimeToSec(driver.find_element_by_class_name("GoProUIHlsTimecode").text)<=secs):
            time.sleep(0.1)
        elapsed = float(time.time() - start)


def checktimecodeplayer2():
    tc = driver.find_element_by_class_name("GoProUIHlsTimecode")
    vt = driver.find_element_by_class_name("GoProUIHlsDuration")
    print vt.text
    print tc.text
    t1 = ""
    elapsed = ""
    vlen = uiTimeToSec(vt.text)
    print "Test Time Counter: %d" % vlen
    for i in range(0,(vlen+1),1):
        start = time.time()

        ttime=intToTimeFormat(i)
        rc = "FAILED"
        dur = driver.find_element_by_class_name("GoProUIHlsDuration").text
        txt = driver.find_element_by_class_name("GoProUIHlsTimecode").text
        n1=uiTimeToSec(txt)
        if i==n1:
            if dur == vt.text:
                rc = "PASSED"

        t1 = txt
        print "Test: %d %s|%s - %s - %s" % (i, txt, dur, rc, elapsed)
        count=5
        c = "FAILED"

        #dynamic wait
        while (True):

            tx=driver.find_element_by_class_name("GoProUIHlsTimecode").text
            if tx!=txt:
                end = time.time()
                elapsed = str(end - start)
                break
            #print "===%s : %s" % (txt, tx)
            count=(count-1)
            time.sleep(0.5)
            if count<1:
                end = time.time()
                elapsed=str(end-start)

                print "Long Time Delay %s seconds" % elapsed
                break


print "start"
#dr = os.path.dirname(__file__)
#chrome_driver_path = dr + "/chromedriver"  # win "\chromedriver.exe"
#chrome_app_path = "/Automation/Qt/qtwebengine/examples/webengine/build-quicknanobrowser-Desktop_Qt_5_8_0_clang_64bit-Debug/quicknanobrowser.app/Contents/MacOS/quicknanobrowser" # --remote-debugging-port=9999"
chrome_app_path = "/Applications/GoPro Quik.app/Contents/MacOS/GoPro Quik"
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location=chrome_app_path
driver = webdriver.Chrome(chrome_options=chromeOptions)



print "Nav to HLS Player ...10sec"
time.sleep(10)
print str(driver)
print str(driver.title)
print str(driver.capabilities)
print str(driver.name)

print str(driver.window_handles)
#print str(driver.page_source)
time.sleep(5)
doclick("button-play-pause")
#time.sleep(3)
#doclick("button-play-pause")

checktimecodeplayer()

doclick("button-play-pause")
# driver.get("http://www.gopro.com")
# time.sleep(3)
# doclick("homepage-video-cta-container")
# doclick("gpl-main-logo")
# doclick("shop-now-anchor")
driver.quit()

print "Done"