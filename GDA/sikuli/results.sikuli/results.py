import sys
import os
import shutil
#import math
#import ast
import json
import codecs
from time import strftime
import datetime
from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython


###########################################
# Tracks screenshots to show historical 
# events to the failed testcase
# add() returns the list pop item used for screenshot cleanup
#
###########################################
class fifo:
    class fifoitem:
        def __init__(self,testname, region=(0, 0, 0, 0), passfail=0, testdetails="", info=""):
            self.name = testname
            self.region = region
            self.passfail = passfail
            self.details = testdetails
            self.info = info


    def __init__(self, rootpath, fifolength=5):
        self.fifo = []
        self.fifolen = fifolength
        self.fifoid = -1
        self.imgrootpath = rootpath


    def add(self, fifoitem):
        self.fifo.insert(0, fifoitem)
        _pop = None
        if len(self.fifo) > self.fifolen:
            _fifoitem = self.fifoitem(self.fifo.pop(self.fifolen))
            if _fifoitem:
                _pop = self.imgrootpath + str(_fifoitem.name)
        return _pop


    def getfifo(self):
        if not self.fifo or len(self.fifo) == 0:
            return None
        return self.fifo


#<failure message="fail">[[html failure message]]</failure>
class xmlreport:
    def __init__(self, archivepath, testsuite, starttime = None):
        self.xmlstart = "<testsuites><testsuite name=\"[[TESTSUITE]]\" tests=\"[[TESTS]]\" failures=\"[[FAILS]]\" errors=\"[[ERRORS]]\" skipped=\"[[SKIPPED]]\" time=\"[[TIME]]\" timestamp=\"[[TIMESTAMP]]\">"
        self.properties = "<properties>[[PROPERTY]]</properties>"
        self.property = "<property name=\"[[NAME]]\" value=\"[[VALUE]]\"/>"
        self.xmlproperty = []
        self.test = "<testcase classname=\"[[CLASSNAME]]\" name=\"[[NAME]]\" time=\"[[TIME]]\">[[TESTINFO]]</testcase>"
        self.xmlend = "</testsuite></testsuites>"
        self.sysout = "<system-out><![CDATA[[[SYSOUT]]]]></system-out>"
        self.syserr = "<system-err><![CDATA[[[SYSERR]]]]></system-err>"
        self.xmlcdata = "<![CDATA[[[CDATA]]]]>"
        self.failure = "<failure message=\"fail\">[[HTMLFAILURE]]</failure>"
        self.testrun = []
        self.testid = -1
        self.testsuite = testsuite
        self.archivepath = archivepath
        self.countpass = 0
        self.countfail = 0
        self.countskip = 0
        self.durationsecs = 0
        self.starttime = starttime #"2016-04-13T10:02:52"
        
    class xmlitem:
        def __init__(self, testname, testid, classname, seconds, failmsg=None, sysout=None  ,syserr=None):
            self.test=testname
            self.classname = classname
            self.duration = seconds
            self.failed = failmsg
            self.sysout = sysout
            self.syserr = syserr
            self.testid = testid
            self.filename = "GDAResults.xml"
            
    def addtest_items(self, testname, testid, classname, seconds, failmsg=None, sysout=None  ,syserr=None):
        item=self.xmlitem(testname, testid, classname, seconds, failmsg, sysout ,syserr)
        return self.addtest(item)
    
    def addtest(self, testcaseitem):
        if not testcaseitem:
            return len(self.testrun)
        self.testrun.append(testcaseitem)
        return len(self.testrun)
    
    def addproperty(self,name, value):
        if name and value:
            self.xmlproperty.append(self.property.replace("[[NAME]]",name).replace("[[VALUE]]",str(value)))
        return len(self.xmlproperty)
    
    def save(self,filename):
        if filename: self.filename=filename
        properties = ""
        if self.xmlproperty and len(self.xmlproperty)>0:
            for propitem in self.xmlproperty:
                properties+=propitem
        self.properties = self.properties.replace("[[PROPERTY]]",properties)
        #print self.properties
        testrun = ""
        testcount = 0
        testfail = 0
        skip = 0
        duration = 0
        #construct testcase results portion of the xml
        if self.testrun and len(self.testrun)>0:
            
            for testitem in self.testrun:
                if not testitem: continue
                test = None
                fail = None
                sysout = None
                syserr = None
                testinfo = ""             
                test = self.test.replace("[[CLASSNAME]]",testitem.classname)
                test = test.replace("[[NAME]]",testitem.test)                
                test = test.replace("[[TIME]]",str(testitem.duration))
                if testitem.failed and len(testitem.failed)>0:
                    fail = self.failure.replace("[[HTMLFAILURE]]",self.xmlcdata.replace("[[CDATA]]",testitem.failed))
                if testitem.sysout and len(testitem.sysout)>0:
                    sysout = self.sysout.replace("[[SYSOUT]]",testitem.sysout)
                if testitem.syserr and len(testitem.syserr)>0:
                    syserr = self.syserr.replace("[[SYSERR]]",testitem.syserr)
                if fail:
                    testfail += 1
                    testinfo += fail
                if sysout:
                    testinfo += sysout
                if syserr:
                    testinfo += syserr
                test = test.replace("[[TESTINFO]]",testinfo)
                testrun += test
                duration+=float(testitem.duration)
                
        suite = self.xmlstart.replace("[[TESTS]]",str(testcount))
        suite = suite.replace("[[FAILS]]",str(testfail))
        suite = suite.replace("[[ERRORS]]",str(testfail))
        suite = suite.replace("[[TESTSUITE]]",self.testsuite)
        suite = suite.replace("[[SKIPPED]]",str(skip))
        suite = suite.replace("[[TIME]]",str(duration))
        suite = suite.replace("[[TESTSUITE]]",self.testsuite)
        suite = suite.replace("[[TIMESTAMP]]",str(self.starttime))
        testfile = suite + self.properties + testrun + self.xmlend
        writefile(filename,testfile)
        return testfile  #.replace(chr(10),"")
    
def mac_to_cwin_path(mpath):
    if not "/" in mpath:
        return mpath
    wpath="C:"

    items = mpath.split("/")
    print items
    if len(items)>0:
        for item in items:
            wpath+='\\'+item
        return wpath
    return mpath

def testxmlreport(testcount):
    x = xmlreport("/path", "mytestsuite", datetime.datetime.now())
    for i in range(1,testcount):
        m=i%2
        t=x.xmlitem("test" + str(i), i, "class" + str(i), 1.1)
        if m==0:
            #testname, testid, classname, seconds, failmsg=None, sysout=None  ,syserr=None
            t=x.xmlitem("test" + str(i),i,"class" + str(i),1.0,"failed" + str(i),"syslog" + str(i),"syserr" + str(i))
            p=x.addproperty("p" + str(i),"v" + str(i))
        n=x.addtest(t)
    winpath = mac_to_cwin_path("/automation/myreportfile.xml")
    print winpath
    xmlfile = x.save(winpath)
    print "============================================"
    print xmlfile #.replace(chr(10),"").replace(chr(13),"")
    print "============================================"
    
def writefile(filepath,data):
    target = None
    try:
        target = open(filepath, 'w')
        target.truncate()
        target.write(data)
        target.close()
    except:        
        print "FAILED:writefile "+str(sys.exc_info())
    finally:
        if target:
            target.close()
    
def stringtest(filename):
    t = "!!!!!!!!!#"
    o="" #MutableString()
#    for i in range(1,1000):
#        o+=t
    o=''.join([t.replace('\n','') for i in xrange(1000)]).replace('\n','')        
    target = open(filename, 'w')
    target.truncate()
    target.write(o)
    target.close()
    print o

 
#stringtest("/Automation/results.xml")
testxmlreport(50)

