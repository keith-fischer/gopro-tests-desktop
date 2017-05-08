

from Tkinter import *
from Tkinter import Tk
from ScrolledText import *
import SeleniumDriver

#from Demopanels import MsgPanel, SeeDismissPanel

class uistate():
    find_element_id = -1
    find_element_txt = ""
    action_id = -1
    action_input_txt = ""

class GoProQuikSeleniumTool(Tk):
    root = None
    b1 = None
    b2 = None
    b3 = None
    b4 = None
    scrolltxt = None
    driver = None
    result_txt = StringVar
    inputstxt = []
    inputsactiontxt = []
    v1 = IntVar
    v2 = IntVar
    v3 = IntVar
    v4 = IntVar
    b3txt = StringVar
    b4txt = StringVar
    en1 = None
    inputstate = uistate()
    quik_path = None
    selenium_search_option_list = [
        "find_element_by_class_name",
        "find_element_by_css_selector",
        "find_element_by_tag_name",
        "find_element_by_name",
        "find_element_by_xpath",
        "find_elements_by_link_text"
    ]

    selenium_action_list = [
        "Get Text",
        "Put Text",
        "Left Mouse Click",
        "Right Mouse Click",
        "Get Attribute",
        "Get Property"

    ]
    selenium_action_list_input = [
        False,
        True,
        False,
       False,
        True,
        True
    ]


    def __init__(self,quik_path = None):
        GoProQuikSeleniumTool.root = Tk()
        if quik_path:
            GoProQuikSeleniumTool.quik_path = quik_path
        GoProQuikSeleniumTool.initUI()

    #todo:
    # perhaps improve formatting of UI using frame containers in the grid
    # Needs refactored into class
    @staticmethod
    def selenium_search_option():
        n=GoProQuikSeleniumTool.v1.get()
        en=GoProQuikSeleniumTool.inputstxt[n-1]
        en=en[1]
        GoProQuikSeleniumTool.inputstate.find_element_id = GoProQuikSeleniumTool.v1.get()
        GoProQuikSeleniumTool.inputstate.find_element_txt = en.get()

        print "%s: %d - %s" % (GoProQuikSeleniumTool.selenium_search_option_list[GoProQuikSeleniumTool.inputstate.find_element_id-1],
                               GoProQuikSeleniumTool.inputstate.find_element_id,
                               GoProQuikSeleniumTool.inputstate.find_element_txt)

    @staticmethod
    def getelement():
        rc=None
        GoProQuikSeleniumTool.selenium_search_option()

        try:
            _call = GoProQuikSeleniumTool.selenium_search_option_list[GoProQuikSeleniumTool.inputstate.find_element_id-1]
            _fn = getattr(GoProQuikSeleniumTool.driver, _call)
            rc = _fn(GoProQuikSeleniumTool.inputstate.find_element_txt)

            if rc:
                GoProQuikSeleniumTool.scrolltxt.insert(END, str(rc))
            else:
                GoProQuikSeleniumTool.scrolltxt.insert(END, "\nelement not found\n")
        except Exception as err:
            ss = "ERROR: %s" % err
            ss += "\nelement not found\n"
            print ss
            GoProQuikSeleniumTool.scrolltxt.insert(END, ss)
        return rc

    @staticmethod
    def invoke_find_element():
        rc = GoProQuikSeleniumTool.getelement()
        try:
            if rc:
                ss= "\nLocation: %s" % str(rc.location)
                ss+="\nSize: %s" % str(rc.size)
                ss+="\nTag Name: %s" % str(rc.tag_name)
                ss+="\nID: %s" % str(rc.id)
                ss+="\nis_displayed: %s" % str(rc.is_displayed())
                ss+="\nis_enabled: %s" % str(rc.is_enabled())
                ss+="\nis_selected: %s" % str(rc.is_selected)
                ss += "\nText: %s\n" % str(rc.text)

                print ss

                GoProQuikSeleniumTool.scrolltxt.insert(END, ss)

        except Exception as err:
            ss = "ERROR: %s" % err
            ss += "\nelement not found\n"
            print ss
            GoProQuikSeleniumTool.scrolltxt.insert(END,ss)

    @staticmethod
    def find_element():
        print "selected find_element: %d" % GoProQuikSeleniumTool.v2.get() #Invoke selenium search

    @staticmethod
    def selenium_action_option():
        print "selenium_action_option: %d" % GoProQuikSeleniumTool.v3.get()
        GoProQuikSeleniumTool.inputstate.action_id = GoProQuikSeleniumTool.v3.get()
        n=GoProQuikSeleniumTool.inputstate.action_id-1
        GoProQuikSeleniumTool.inputstate.action_input_txt = ""
        if n<len(GoProQuikSeleniumTool.inputsactiontxt):
            en1=GoProQuikSeleniumTool.inputsactiontxt[n]
            if en1:
                s = en1[1].get()
                print str(s)
                GoProQuikSeleniumTool.inputstate.action_input_txt=s
        else:
            GoProQuikSeleniumTool.inputstate.action_input_txt = ""



    @staticmethod
    def invoke_selenium_action_option():
        try:
            print "invoke_selenium_action_option: %d" % GoProQuikSeleniumTool.v3.get()
            uistate.action_id = GoProQuikSeleniumTool.v3.get()
            GoProQuikSeleniumTool.selenium_search_option()
            SeElement = GoProQuikSeleniumTool.getelement()
            if SeElement:
                if uistate.action_id == 1:
                    s = SeElement.text
                    ss = "Get text:\n%s" % s
                    print ss
                    GoProQuikSeleniumTool.scrolltxt.insert(END, ss)
                elif uistate.action_id == 2:
                    s = str(Tk.clipboard_get())
                    SeElement.send_keys(s)
                    ss = "put text, from clipboard: %s" % s
                    print ss
                    GoProQuikSeleniumTool.scrolltxt.insert(END, ss)


                elif uistate.action_id == 3:
                    SeElement.click()
                    ss = "Left Click"
                    print ss
                    GoProQuikSeleniumTool.scrolltxt.insert(END, ss)
                elif uistate.action_id == 4:#Right Mouse Click
                    action= SeleniumDriver.webdriver.ActionChains(SeleniumDriver.Selenium.driver)
                    action.context_click(SeElement)
                    ss = "context_click"

                    print ss
                    GoProQuikSeleniumTool.scrolltxt.insert(END, ss)

                elif uistate.action_id == 5:
                    ss = "Mouse Down"
                    print ss
                    GoProQuikSeleniumTool.scrolltxt.insert(END, ss)
                elif uistate.action_id == 6:
                    ss = "Mouse Up"
                    print ss
                    GoProQuikSeleniumTool.scrolltxt.insert(END, ss)
                else:
                    ss= "Invalid %d" % uistate.action_id
                    print ss
                    GoProQuikSeleniumTool.scrolltxt.insert(END, ss)
            else:
                ss= "Invalid %d" % uistate.action_id
                print ss
                GoProQuikSeleniumTool.scrolltxt.insert(END, ss)
        except Exception as err:
            ss = "ERROR: %s" % err
            ss += "\nelement not found\n"
            print ss
            GoProQuikSeleniumTool.scrolltxt.insert(END, ss)

    @staticmethod
    def input_element():
        n=GoProQuikSeleniumTool.v2.get()

    @staticmethod
    def start_selenium():
        if SeleniumDriver.Selenium.ready:
            GoProQuikSeleniumTool.b3txt.set("START Quik Selenium")
            SeleniumDriver.Selenium.driver.quit()
        else:
            #Selenium = imp.load_module("SeleniumDriver",
            #                           "/Automation/gopro-tests-desktop/GDA/python/quik_selenium/pydriver/SeleniumDriver.py")
            SeleniumDriver.Selenium()
            if SeleniumDriver.Selenium.ready:
                GoProQuikSeleniumTool.driver = SeleniumDriver.Selenium.driver
                GoProQuikSeleniumTool.b3txt.set("STOP Quik Selenium")
                GoProQuikSeleniumTool.scrolltxt.insert(END, "\nSelenium Driver Started Quik")
                GoProQuikSeleniumTool.scrolltxt.insert(END, "\n"+str(GoProQuikSeleniumTool.driver.capabilities))
            else:
                GoProQuikSeleniumTool.scrolltxt.insert(END, "\nSelenium Driver Failed to Start Quik")


    @staticmethod
    def js_eval_handler():
        mtxt=GoProQuikSeleniumTool.inputstxt[6]
        js_script=""
        GoProQuikSeleniumTool.scrolltxt.insert(END, "\nJavaScript Eval:")
        GoProQuikSeleniumTool.scrolltxt.insert(END, "\n" + js_script)
        rc=SeleniumDriver.Selenium.driver.execute_script(js_script)
        GoProQuikSeleniumTool.scrolltxt.insert(END, "\nRETURN:")
        GoProQuikSeleniumTool.scrolltxt.insert(END, "\n" + str(rc))

    @staticmethod
    def initUI():
        GoProQuikSeleniumTool.result_txt = StringVar()
        GoProQuikSeleniumTool.inputstxt = []
        GoProQuikSeleniumTool.inputsactiontxt = []
        GoProQuikSeleniumTool.v1 = IntVar()
        GoProQuikSeleniumTool.v1.set(1)
        GoProQuikSeleniumTool.v2 = IntVar()
        GoProQuikSeleniumTool.v2.set(1)
        GoProQuikSeleniumTool.v3 = IntVar()
        GoProQuikSeleniumTool.v3.set(1)
        GoProQuikSeleniumTool.v4 = IntVar()
        GoProQuikSeleniumTool.v4.set(1)

        GoProQuikSeleniumTool.b3txt = StringVar()
        GoProQuikSeleniumTool.b4txt = StringVar()
        GoProQuikSeleniumTool.root.wm_title("GoPro Quik Selenium Tester Tool")

        Label(GoProQuikSeleniumTool.root,
              text="Set selenium search method",
              justify=LEFT,
              padx=20).grid(row=0,
                            column=0)

        Label(GoProQuikSeleniumTool.root,
              text="find_element Reference",
              justify=LEFT,
              padx=20).grid(row=0,
                            column=1)

        Label(GoProQuikSeleniumTool.root,
              text="find_element Action",
              justify=LEFT,
              padx=20).grid(row=0,
                            column=2)
        Label(GoProQuikSeleniumTool.root,
              text="find_element Action Input",
              justify=LEFT,
              padx=20).grid(row=0,
                            column=3)
        ################################################################################
        # List items >>>
        for i in range(len(GoProQuikSeleniumTool.selenium_search_option_list)):
            # add the find element option buttons
            Radiobutton(GoProQuikSeleniumTool.root,
                        text=GoProQuikSeleniumTool.selenium_search_option_list[i],
                        justify=LEFT,
                        indicatoron=0,
                        width=20,
                        padx=20,
                        variable=GoProQuikSeleniumTool.v1,
                        command=GoProQuikSeleniumTool.selenium_search_option,
                        value=i+1).grid(row=(i+1),
                                        column=0)

            #add the find element input textbox
            GoProQuikSeleniumTool.inputstxt.append((GoProQuikSeleniumTool.selenium_search_option_list[i],
                                                    Entry(GoProQuikSeleniumTool.root,
                                                          width=20)))
            GoProQuikSeleniumTool.en=GoProQuikSeleniumTool.inputstxt[i]
            GoProQuikSeleniumTool.en=GoProQuikSeleniumTool.en[1]
            GoProQuikSeleniumTool.en.grid(row=(i + 1),
                                          column=1)


            # add the action input options
            if i<len(GoProQuikSeleniumTool.selenium_action_list):
                Radiobutton(GoProQuikSeleniumTool.root,
                            text=GoProQuikSeleniumTool.selenium_action_list[i],
                            justify=LEFT,
                            indicatoron=0,
                            width=20,
                            padx=20,
                            variable=GoProQuikSeleniumTool.v3,
                            command=GoProQuikSeleniumTool.selenium_action_option,
                            value=i + 1).grid(row=(i + 1),
                                              column=2)
            # add the action input textbox
            if i < len(GoProQuikSeleniumTool.selenium_action_list_input):
                if GoProQuikSeleniumTool.selenium_action_list_input[i]:
                    en2 = GoProQuikSeleniumTool.selenium_action_list[i],Entry(GoProQuikSeleniumTool.root,width=20)
                    GoProQuikSeleniumTool.inputsactiontxt.append(en2)
                    en2 = GoProQuikSeleniumTool.inputsactiontxt[i]
                    en2 = en2[1]
                    en2.grid(row=(i + 1),
                        column=3)

                else:
                    GoProQuikSeleniumTool.inputsactiontxt.append(None)
        # List items <<<<

        GoProQuikSeleniumTool.r1 = len(GoProQuikSeleniumTool.selenium_search_option_list)+2
        GoProQuikSeleniumTool.b1=Button(GoProQuikSeleniumTool.root,
                                        text="find_element",
                                        command=GoProQuikSeleniumTool.invoke_find_element)

        GoProQuikSeleniumTool.b1.grid(row=GoProQuikSeleniumTool.r1,
                                      column=0)

        GoProQuikSeleniumTool.b2=Button(GoProQuikSeleniumTool.root,
                                        text="Invoke Action",
                                        command=GoProQuikSeleniumTool.invoke_selenium_action_option)

        GoProQuikSeleniumTool.b2.grid(row=GoProQuikSeleniumTool.r1,
                                      column=1)

        GoProQuikSeleniumTool.b3=Button(GoProQuikSeleniumTool.root,
                                        text="Start Quik Selenium",
                                        textvariable=GoProQuikSeleniumTool.b3txt,
                                        command=GoProQuikSeleniumTool.start_selenium)

        GoProQuikSeleniumTool.b3.grid(row=GoProQuikSeleniumTool.r1,
                                      column=2)

        GoProQuikSeleniumTool.b3txt.set("START Quik Selenium")

        GoProQuikSeleniumTool.scrolltxt = ScrolledText(GoProQuikSeleniumTool.root,
                                                                    width=100,
                                                                    height=20,
                                                                    border=5)
        #scrolltxt.insert(END, "\nElement result info")
        #scrolltxt.insert(END,"\n"+str(scrolltxt.config()))
        GoProQuikSeleniumTool.scrolltxt.grid(row=(GoProQuikSeleniumTool.r1+1),
                                             column=0,
                                             columnspan=80)

        GoProQuikSeleniumTool.b4=Button(GoProQuikSeleniumTool.root,
                                        text="JS Eval",
                                        textvariable=GoProQuikSeleniumTool.b4txt,
                                        command=GoProQuikSeleniumTool.js_eval_handler)

        GoProQuikSeleniumTool.b4.grid(row=GoProQuikSeleniumTool.r1+3,
                                      column=0)

        GoProQuikSeleniumTool.b4txt.set('JS Eval')

        en4=Entry(GoProQuikSeleniumTool.root, width=80)

        GoProQuikSeleniumTool.inputstxt.append(en4)

        en4.grid(row=GoProQuikSeleniumTool.r1+4, column=0,
                                             columnspan=80)

        GoProQuikSeleniumTool.root.mainloop()


if __name__ == '__main__':
    g=GoProQuikSeleniumTool()
