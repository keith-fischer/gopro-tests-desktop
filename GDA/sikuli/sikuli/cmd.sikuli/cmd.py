

import java.lang.System
import java
import sys, getopt
import os
import shutil
#import math
#import ast
import json
from time import strftime
from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython
import org.sikuli.script.ImagePath
#import results
setShowActions(False)
Debug.setDebugLevel(3)

d_settings = {}
def parseargs():
    global d_settings
    if len(sys.argv) == 3:
        d_settings["path"] = sys.argv[1]
        d_settings["verify"] = sys.argv[2]
        return True
    return False
##########################################
# parse the args
##########################################
def main(argv):
    init()
    if not parseargs():
        print "Invalid args:%s" % str(sys.argv)
        exit(1)
    do_verify()
    
def init():
    global d_settings
    d_settings["root"] = "/Automation/Sikuli"
    ImagePath.setBundlePath(d_settings["root"])
    d_settings["path"] = "/Automation/Sikuli/img-region.png"
    d_settings["verify"] = "img-verify-3.png"
    d_settings["similarity"] = 0.99 # maybe add this as third param for different mobile devices
    
##########################################
# create region and validate
# region png should be larger than the verify png
##########################################
def do_verify():
    # /Users/keithfisher/Desktop/ScreenShots/Screen Shot 2016-06-14 at 9.28.05 AM.png
    global d_settings
    preview_region = Finder(d_settings["path"]) #your screenshot
    #m = preview_region.load(Pattern(d_settings["path"]).exact().targetOffset(1,0))
    #find(Pattern("zzzzzz.png").exact().targetOffset(1,0))
    if preview_region:
        #verify your test template png is found in the screenshot
        preview_region.find(Pattern( d_settings["verify"]).similar(d_settings["similarity"]))
        if preview_region.hasNext():
            while preview_region.hasNext():
                fmatch = preview_region.next()
                if fmatch:
                    print "FOUND:%s\n%s-->%s" % (str(fmatch),d_settings["verify"],d_settings["path"])
                    print "similarity:%s" % str(fmatch.getScore())
                else:
                    print "NOT FOUND:%s" % d_settings["verify"]
        else:
            print "NOT FOUND:%s" % d_settings["verify"]
        preview_region.destroy()
    else:
        print "NOT FOUND:%s" % d_settings["verify"]
        
if __name__ == "__main__":
    main(sys.argv[1:])

    