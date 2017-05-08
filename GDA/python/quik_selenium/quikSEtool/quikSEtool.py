import imp
from Tkinter import *
from ScrolledText import *
#from selenium import webdriver


import time

class uistate():
    find_element_id=-1
    find_element_txt=""
    action_id=-1

#todo:
# perhaps improve formatting of UI using frame containers in the grid
# Needs refactored into class
def selenium_search_option():
    n=v1.get()
    en=inputstxt[n-1]
    en=en[1]
    inputstate.find_element_id = v1.get()
    inputstate.find_element_txt = en.get()

    print "selenium_search_option: %d - %s" % (v1.get(), en.get())

def invoke_find_element():
    global scrolltxt
    print "invoke_find_element: %d" % v2.get()  # Invoke selenium search
    inputstate.find_element_id=v2.get()
    try:
        _call = selenium_search_option_list[inputstate.find_element_id-1]
        _fn = getattr(driver,_call)
        rc = _fn(inputstate.find_element_txt)
        ss= "\nLocation: %s" % str(rc.location)
        ss+="\nSize: %s" % str(rc.size)
        ss+="\nTag Name: %s" % str(rc.tag_name)

        ss += "\nText: %s\n" % str(rc.text)
        print ss

        scrolltxt.insert('1.0',ss)
    except Exception as err:
        ss = "ERROR: %s" % err
        ss += "\nelement not found\n"
        print ss
        scrolltxt.insert('1.0',ss)

def find_element():
    print "selected find_element: %d" % v2.get() #Invoke selenium search
    inputstate

def selenium_action_option():
    print "selenium_action_option: %d" % v3.get()
    inputstate.action_id = v3.get()

def invoke_selenium_action_option():
    print "invoke_selenium_action_option: %d" % v3.get()

def input_element():
    n=v2.get()

selenium_search_option_list = [
    "find_element_by_class_name",
    "find_element_by_css_selector",
    "find_element_by_tag_name",
    "find_element_by_name",
    "find_element_by_xpath",
    "find_elements_by_link_text"
]

selenium_action_list = [
    "get text",
    "get attributes",
    "Click",
    "action4",
    "action5",
    "action6"
]


def start_selenium(*args):
    global driver
    if driver:
        b3txt.set("START Quik Selenium")
        driver.quit()
    else:
        b3txt.set("STOP Quik Selenium")
        Selenium = imp.load_module("SeleniumDriver",
                                   "/Automation/gopro-tests-desktop/GDA/python/quik_selenium/pydriver/SeleniumDriver.py")
        Selenium.init()
        driver=Selenium.driver
        # chrome_app_path = "/Applications/GoPro Quik.app/Contents/MacOS/GoPro Quik"
        # chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.binary_location = chrome_app_path
        # driver = webdriver.Chrome(chrome_options=chromeOptions)


def initUI(root):
    global scrolltxt
    root.wm_title("GoPro Quik Selenium Tester Tool")

    Label(root, text="Set selenium search method", justify=LEFT, padx=20).grid(row=0, column=0)
    Label(root, text="find_element Reference", justify=LEFT, padx=20).grid(row=0, column=1)
    Label(root, text="find_element Action", justify=LEFT, padx=20).grid(row=0, column=2)
    for i in range(len(selenium_search_option_list)):

        Radiobutton(root, text=selenium_search_option_list[i], justify=LEFT, indicatoron=0, width=20, padx=20,
                    variable=v1, command=selenium_search_option, value=i+1).grid(row=(i+1), column=0)

        inputstxt.append((selenium_search_option_list[i], Entry(root, width=20)))
        en=inputstxt[i]
        en=en[1]
        en.grid(row=(i + 1), column=1)
        if i<len(selenium_action_list):
            Radiobutton(root, text=selenium_action_list[i], justify=LEFT, indicatoron=0, width=10, padx=20,
                        variable=v3, command=selenium_action_option, value=i + 1).grid(row=(i + 1), column=2)

    r1=len(selenium_search_option_list)+2
    b1=Button(root,text="find_element", command=invoke_find_element)
    b1.grid(row=r1,column=0)

    b2=Button(root, text="Invoke Action", command=invoke_selenium_action_option)
    b2.grid(row=r1, column=1)
    b3=Button(root,text="Start Quik Selenium",textvariable=b3txt, command=start_selenium)
    b3.grid(row=r1, column=2)
    b3txt.set("START Quik Selenium")
    scrolltxt = ScrolledText(root, width=80,height=10, border=5)
    scrolltxt.insert('1.0', "Element result info")
    scrolltxt.grid(row=(r1+1),column=0,columnspan=40)

b1=None
b2=None
b3=None
scrolltxt=None
driver = None
result_txt = None
root = Tk()

inputstxt=[]

v1 = IntVar()
v1.set(1)
v2 = IntVar()
v2.set(1)
v3 = IntVar()
v3.set(1)

result_txt = StringVar()
b3txt = StringVar()


inputstate = uistate()
initUI(root)

root.mainloop()

