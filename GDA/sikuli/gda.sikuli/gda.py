
from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython
import org.sikuli.script.ImagePath

import gda_utils
import gda_create_tests
import gda_music_tests
import gda_BAT
import gda_img_regression

######################################
# 
# 
# 
######################################
def DEBUG(gpa, gpr):
    #gda_create_tests(gpa,gpr)
    gda_music_tests.testsongs(gpa,gpr,15)


    
##########################################
# main script
##########################################

gda_utils.GetEnvInfo()
#gda_utils.d_gda_settings['runtest']='gda_img_regression'
#gda_utils.d_gda_settings['testpath']="/Users/keithfisher/gda_music_images-Mac4790"
#gda_utils.d_gda_settings['baselinepath']="/Users/keithfisher/gda_music_images-Mac4781"

# Non GUI GDA TESTS
if gda_utils.d_gda_settings['runtest']=='gda_img_regression':
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: GDA IMAGE REGRESSION TESTS"
    print "++++++++++++++++++++++++++++++++++"
    bpath=gda_utils.d_gda_settings['baselinepath']
    tpath=gda_utils.d_gda_settings['testpath']
    rc=gda_img_regression.compare_image_sets(bpath,tpath)
    if rc:
        print "PASSED: gda_img_regression"
    else:
        print "FAILED: gda_img_regression"
        exit(-1)
    exit(0)    
#gp,gpr=AppStartRetry("GoPro",3)
gpa,gpr=gda_utils.AppStart("Quik")

if not gpa:
    print "ERROR: App not found"
    exit(1)
if not gpr:
    print "ERROR: App Window Region not found"
    if gpa:
        gpa.close()
    exit(1)
    
print "%d X %d" % (gpr.w,gpr.h)    

gda_utils.d_similarity=gda_utils.getDictFromFile()
if gda_utils.d_similarity:
    print "JSON ====================="
    print gda_utils.printjson(gda_utils.d_similarity)
    print "=========================="
else:
    print "JSON ====================="
    print "FAILED TO Load JSON: d_similarity file NOT found"
    print "Test run will run VERY slow"
    print "Assumed automation has never run on this machine."
    print "A new d_similarity file will be created"
    print "You should not see this message when you rerun the automation on this machine."
    print "=========================="        

gda_utils.ScreenShot(gpr,"startup")
#for i in range(1,6,1):
#    story(gpr)
if gda_utils.d_gda_settings['runtest']=='default':
    #exit(0)
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: DEFAULT"
    print "++++++++++++++++++++++++++++++++++"
    exit(1)
    #ocr(gpr,"")
    #gda_BAT.BAT(gpa,gpr)
    for i in range(1,9999):
        print "================================================="
        print "%d <<<<<<<<<<<<<<<<<<<<" % i
        print "================================================="
        tryexcept=False
        try:
            gda_create_tests.record_momentsbeats(gpr)
        except Exception, err:
            print "FAILED: ###################################"
            print str(err)
            gda_utils.failcount+=1
            tryexcept=True
        gda_utils.putDictToFile(gda_utils.d_similarity)    
        gda_utils.printreport("GDA_MOMENTS TEST")
        gda_utils.resetglobals()
        if tryexcept:
            exit(1)

elif gda_utils.d_gda_settings['runtest']=='gda_view_tests':
    gda_create_tests.gda_create_tests(gpa,gpr,60,16)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("GDA_MOMENTS TEST")
    gda_utils.resetglobals()
    
elif gda_utils.d_gda_settings['runtest']=='gda_music_tests-capture':
   
    gda_music_tests.test_music_60(gpa,gpr)
    
elif gda_utils.d_gda_settings['runtest']=="gda_create_tests-record":
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: RECORD GDA_CREATE_TESTS MOMENTS_MUSIC"
    print "++++++++++++++++++++++++++++++++++"     
    gda_create_tests.record_moments_beats(gpa,gpr)
elif gda_utils.d_gda_settings['runtest']=="gda_create_tests-regression":
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: REGRESSION GDA_CREATE_TESTS MOMENTS_MUSIC"
    print "++++++++++++++++++++++++++++++++++"     
    gda_create_tests.regression_momentsbeats(gpr)
elif gda_utils.d_gda_settings['runtest']=="gda_analytics-regression":
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: REGRESSION GDA_CREATE_TESTS MOMENTS_MUSIC"
    print "++++++++++++++++++++++++++++++++++"     
    gda_music_tests.test_analytics("song_ARECKONING.png")

elif gda_utils.d_gda_settings['runtest']=='gda_music_tests-regression':
    #DEBUG(gpa, gpr)
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: REGRESSION GDA_MUSIC_TESTS 15"
    print "++++++++++++++++++++++++++++++++++"    
    gda_music_tests.testsongs(gpa,gpr,15)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("REGRESSION GDA_MUSIC_TESTS")
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: REGRESSION GDA_MUSIC_TESTS 30"
    print "++++++++++++++++++++++++++++++++++"    
    gda_music_tests.testsongs(gpa,gpr,30)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("REGRESSION GDA_MUSIC_TESTS")
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: REGRESSION GDA_MUSIC_TESTS 60"
    print "++++++++++++++++++++++++++++++++++"    
    gda_music_tests.testsongs(gpa,gpr,60)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("REGRESSION GDA_MUSIC_TESTS")

elif gda_utils.d_gda_settings['runtest']=='gda_BAT':
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: GDA_BAT TESTS"
    print "++++++++++++++++++++++++++++++++++"    
    gda_BAT.BAT(gpa,gpr)
elif gda_utils.d_gda_settings['runtest']=='gda_img_regression':
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: GDA IMAGE REGRESSION TESTS"
    print "++++++++++++++++++++++++++++++++++"    
    # gda_img_regression.compare_image_sets(gpa,gpr)

else:
    s=""
    if 'runtest' in gda_utils.d_gda_settings:
        s = gda_utils.d_gda_settings['runtest']
    print "++++++++++++++++++++++++++++++++++"
    print "ERROR: NO TEST DEFINED" 
    print s
    print "++++++++++++++++++++++++++++++++++"


    