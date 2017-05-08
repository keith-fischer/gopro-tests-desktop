#Quik Mac 2.3.0.6081
import os
import sys
import traceback
import platform
from datetime import datetime
from os.path import expanduser
import json
import org.sikuli.script.ImagePath
import shutil
from random import randint
from time import strftime
from types import *
from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython

import gda_utils
import gda_music_tests

d_report = {}
momentstestcounter = 0
######################################
# 
# window size=(630, 10, w1918, h857)
# 
######################################
    
def scrubtest(REGION):

    scrub60=gda_utils.EXISTS3("CREATE","4VIDEOS",Pattern("scrub-60.png").similar(0.69).targetOffset(-270,0))
    if scrub60:
        scrub60.highlight(1)
        #p=(Pattern("scrub-60.png").similar(0.69).targetOffset(-270,0)
        hover(scrub60)
        x=scrub60.getX()
        y=scrub60.getY()+40
        count=1
        step=5
        steps=[]
        st=10
        w=3
        w1=5
        for i in range(1,scrub60.getW(),step):
            print x
            hover(Location(x+i,y))
            
            #scrub60.mouseMove(Location(x,0))
            if count==1:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player1.png").similar(0.83),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==2:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player2.png").similar(0.85),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==3:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player3.png").similar(0.86),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==4:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player4.png").similar(0.74),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==5:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player5.png").similar(0.74),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==6:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player6.png").similar(0.82),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==7:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player7.png").similar(0.87),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==8:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player8.png").similar(0.72),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==9:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player9.png").similar(0.72),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==10:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player10.png").similar(0.72),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==11:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player11.png").similar(0.85),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==12:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player12.png").similar(0.72),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==13:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player13.png").similar(0.84),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=5
            elif count==14:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player14.png").similar(0.73),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==15:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player15.png").similar(0.72),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            elif count==16:
                m=gda_utils.EXISTS3("CREATE","PLAYER",Pattern("player16.png").similar(0.71),w)
                if m:
                    steps.append(count)
                    m.highlight(1)
                    count+=1
                    step=st
                else:
                    step=w1
            else:
                break
        print str(steps)               
         

def selectmediaforstory(REGION):
    
    gda_utils.WAIT(REGION,Pattern("view_btn_view-create.png").similar(0.98),5)  #media_txt_media-editor.png
    gda_utils.CLICK(REGION,Pattern("view_btn_view-create.png").similar(0.98).targetOffset(55,2))  #media_txt_media-editor.png
    gda_utils.WAIT(REGION,Pattern("create_txt_media.png").similar(0.71),10) # media_btn_selected-media.png

    #gda_utils.click(Pattern("media_btn_selected.png").similar(0.98)) #media_btn_selected
    gda_utils.WAIT(REGION,Pattern("editor_btn_selected.png").similar(0.98),10) #editor_btn_selected
    
    gda_utils.FIND(REGION,Pattern("editor_img_1-4.png").exact().targetOffset(-138,3)) # editor_img_1-4.png
    gda_utils.FIND(REGION,Pattern("editor_img_5-8.png").exact().targetOffset(-135,2)) # editor_img_5-8.png
    gda_utils.FIND(REGION,Pattern("editor_img_9-12.png").exact().targetOffset(-137,2)) # editor_img_9-12.png
    gda_utils.FIND(REGION,Pattern("editor_img_13-16.png").exact().targetOffset(-137,4)) # editor_img_13-16.png


######################################
# 
# 
# 
######################################    
def popup_areyousure_deletefile(REGION):
    rc=False
    foundreg=gda_utils.EXISTS2(REGION,Pattern("popup_txt_title-AREYOUSURE.png").similar(0.98))
    if foundreg:
        foundreg.highlight(1)
        subreg=foundreg.below(200)
        subreg=subreg.grow(30)
        subreg.highlight(1)
    #gda_utils.FIND(REGION,)
    #rc=gda_utils.FIND(REGION,Pattern("popup_txt_info-willpermanentlydeletefile.png").similar(0.92))
        rc=gda_utils.CLICK2(subreg,Pattern("popup_btn_delete-areyousure.png").similar(0.88))
    return rc

######################################
# 
# 
# returns true if the png of "Title" is found in textbox after textfield text is clear
######################################  
def cleartextfield(regionclick,validateclear=Pattern("popup_txt_title-mp4filenamesave.png").similar(0.68)):
    print "cleartextfield:>>>>>"
    rc=False
    wait(1)

    if gda_utils.d_gda_settings["isWindows"]=="True":
        regionclick.click()
        wait(1)

        regionclick.keyDown(Key.CTRL)
        wait(1)

        regionclick.type("a")
        wait(1)

        regionclick.keyUp(Key.CTRL)
        wait(1)

        regionclick.type(Key.BACKSPACE)
    elif gda_utils.d_gda_settings["isMac"]=="True":
        regionclick.click()
        wait(1)

        regionclick.keyDown(Key.CMD)
        wait(1)

        regionclick.type("a")
        wait(1)

        regionclick.keyUp(Key.CMD)
        wait(1)

        regionclick.type(Key.BACKSPACE)           
    wait(2)
    #regionclick=regionclick.grow(20)
    regionclick.highlight(1)
    m = regionclick.exists(validateclear)
    if not m:
        print "Failed to clear textfield"
        regionclick.highlight(5)
    else:
        rc=True

    print "cleartextfield:<<<<<<"
    return rc

######################################
# save btn, type filename(song), cancel share,returns to editor
# 
# 
###################################### 
def exportmp4(REGION,d_song,png,duration):
    print "exportmp4 >>>>> %d - %s" % (duration,png)
    rc=False
    saveresult="mp4saveresult_%d" % duration
    d_song[saveresult]="FAILED"
    
    dur="_%d" % duration
    mp4=png.replace(".png",dur)
    mp4=mp4.replace("_","")
    btnsave_blk=gda_utils.EXISTS3("CREATE","BOTTOM",Pattern("create_btn_save-nohover.png").similar(0.68))
    if not btnsave_blk:
        print "Save button not found"
        print "exportmp4 <<<<<<<<<<<<<<<<<<<!"
        return rc, d_song
    #hover(btnsave)
    #btnsave_blu=gda_utils.EXISTS3("CREATE","BOTTOM",Pattern("create_btn_save-hover.png").similar(0.80))
    btnsave_blk.click()
    wait(5)
    rpop=gda_utils.EXISTS2(REGION,Pattern("popup_lbl_nameyournewvideo.png").similar(0.68),120)
    if not rpop:
        print "FAILED: Popup for video save dialog %s" % mp4
        print "exportmp4 <<<<<<<<<<<<<<<<<<<!"
        REGION.click(Pattern("create-popup-save_btn_cancel.png").similar(0.69))
        return rc, d_song
    rpop = rpop.below(70)
    rpop.highlight(5)
    mlbl=gda_utils.EXISTS2(rpop,Pattern("popup_txt_info-findvideosineditsview.png").similar(0.69))
    if mlbl:
        rpop=mlbl.left(1)
        rpop=rpop.right(600)
        rpop=rpop.below(300)
    else:
        print "FAILED: Popup to find textbox video save %s" % mp4
        print "info label not found: You'll find your video in the Edits view"
        print "exportmp4 <<<<<<<<<<<<<<<<<<<!"
        rpop.click(Pattern("create-popup-save_btn_cancel.png").similar(0.69))
        return rc, d_song
    rpop.highlight(2)
    mtxt=gda_utils.EXISTS2(rpop,Pattern("popup_txt_title-mp4filenamesave.png").similar(0.68))
    if not mtxt:
        r1=gda_utils.EXISTS2(rpop,Pattern("create-popup-save_lbl_Quality.png").similar(0.68))
        if r1:
            r2=r1.left(5)
            r1=r2.right(100)
            r2=r1.above(300)
            r2.highlight(1)
            r1=gda_utils.EXISTS2(r2,Pattern("create-popup-save_img_textboxLeftborder.png").similar(0.69).targetOffset(70,0))
            if r1:
                r1.click(Pattern("create-popup-save_img_textboxLeftborder.png").similar(0.69).targetOffset(70,0))
                wait(1)
                r1.click(Pattern("create-popup-save_img_textboxLeftborder.png").similar(0.69).targetOffset(70,0))
                wait(1)
            #mtxt.click(Pattern("popup_txt_title_song.png").similar(0.69).targetOffset(283,0))

                if not cleartextfield(r1.right(100)):
                    print "FAILED: Popup to clear textbox with song name %s" % mp4
                    print "'song' name not foundew"
                    print "exportmp4 <<<<<<<<<<<<<<<<<<<!"
                    rpop.click(Pattern("create-popup-save_btn_cancel.png").similar(0.69))
                    return rc, d_song
                mtxt=gda_utils.EXISTS2(rpop,Pattern("popup_txt_title-mp4filenamesave.png").similar(0.68))
            else:
                print "FAILED: Popup to find textbox left edge for clearing old text"
                
                print "exportmp4 <<<<<<<<<<<<<<<<<<<!"
                rpop.click(Pattern("create-popup-save_btn_cancel.png").similar(0.69))
                return rc, d_song                
        else:
            print "FAILED: Popup to find textbox with song name %s" % mp4
            print "info label not found: You'll find your video in the Edits view"
            print "exportmp4 <<<<<<<<<<<<<<<<<<<!"
            rpop.click(Pattern("create-popup-save_btn_cancel.png").similar(0.69))
            return rc, d_song
    
    wait(1)

    mtxt.click()
    wait(1)
    mtxt.click()
    wait(1)
    print "TYPING TITLE NAME: %s" % mp4
    mtxt.type(mp4)
    mtxt=gda_utils.EXISTS2(rpop,Pattern("popup_btn_save-exportvideo.png").similar(0.72))
    savename="mp4savename_%d" % duration
    d_song[savename]=mp4
    if not mtxt:
        print "FAILED: Popup to find textbox video save %s" % mp4
        print "exportmp4 <<<<<<<<<<<<<<<<<<<!"
        rpop.click(Pattern("create-popup-save_btn_cancel.png").similar(0.69))
        return rc, d_song       
    mtxt.click()
    wait(1)
    mtxt.click()
    dta = datetime.now()
    mpopsave=gda_utils.EXISTS2(REGION,Pattern("popup_txt_savingtoedits.png").similar(0.69),30)
    if not mpopsave:
        print "FAILED: Popup to show save progress %s" % mp4
        print "exportmp4 <<<<<<<<<<<<<<<<<<<!"
        return rc, d_song
    wait(1)

    blu_view_status=gda_utils.EXISTS3("CREATE","TITLE",Pattern("view_txt_selectbarstatus-1itemselected.png").similar(0.69),700)
    if not blu_view_status:
        print "Failed: View status blue bar not found selected on new output mp4"
        print "exportmp4 <<<<<<<<<<<<<<<<<<<!"        
        return rc, d_song
    
    dtb = datetime.now()
    dtc=dtb-dta
    blu_view_status.highlight(1)
    savesecs="mp4savetime_%d" % duration
    d_song[savesecs]=dtc.seconds
    print "===================================="
    print "%d SECONDS ==============================" % dtc.seconds
    print "===================================="
    wait(1)

    blu_view_status.click(Pattern("view_txt_selectbarstatus-1itemselected.png").similar(0.69).targetOffset(-81,0))
    wait(1)

    if nav_view_to_create(REGION):
        saveresult="mp4saveresult_%d" % duration
        d_song[saveresult]="PASSED"
        rc=True
    else:
        print "Failed: navigate to create screen"
        print "exportmp4 <<<<<<<<<<<<<<<<<<<!"   
           
    print "exportmp4 <<<<<<<<<<<<<<<<<<<"
    return rc, d_song

def view_delete_selected(REGION):
    rc = False
    print ">>>>>>view_delete_selected"
    blu_view_status=gda_utils.EXISTS3("CREATE","TITLE",Pattern("view_txt_selectbarstatus-1itemselected.png").similar(0.69),30)
    if not blu_view_status:
        print "Failed: View status blue bar not found selected on new output mp4"
        print "view_delete_selected <<<<<<<<<<<<<<<<<<<!"        
        return rc, d_song
    statusregion=blu_view_status.right(650)
    statusregion=statusregion.grow(10)
    statusregion.highlight(1)
    itemdelete=gda_utils.EXISTS2(statusregion,Pattern("view_btn_bluitemselectedbar-delete.png").similar(0.71),30)
    if itemdelete:
        itemdelete.highlight(1)
        itemdelete.click()
        if popup_areyousure_deletefile(REGION):
            rc=True
    else:
        print "Failed: View status blue bar Delete button not found"
        print "view_delete_selected <<<<<<<<<<<<<<<<<<<!"        
   
    return rc


def nav_view_to_create(REGION):
    print ">>>>>>nav_view_to_create"
    rc=False
    createm=gda_utils.EXISTS3("CREATE","TOP",Pattern("view_btn_create-tab.png").similar(0.69),30)
    if createm:
        createm.click()
        if gda_utils.EXISTS3("CREATE","TITLE",Pattern("create_txt_media.png").similar(0.71),30):
            rc= True
    else:
        print("FAILED nav_view_to_create")
    print "<<<<<<<< nav_view_to_create"
    
    return rc
######################################
# 
# 
# 
######################################    
def init_music(REGION,msongs):
    gda_utils.CLICK(REGION,Pattern("editor_img_1-4.png").exact().targetOffset(-138,3),1,False) # editor_img_1-4.png
    #selectmusic(REGION) # editor_img_music-duration
    if selectmusic(REGION):
        if gda_utils.FIND(REGION,Pattern("music_btn_music-selected.png").similar(0.71)):
            if gda_music_tests.resetscrolltotop(REGION):
                p=gda_utils.PATTERN(msongs.getFirstSongItem(),0.69)
                gda_music_tests.EXISTS(REGION,p,None,False)                
                gda_music_tests.addtovideo(REGION)
                return True
    return False

######################################
# 
#
# 
######################################
def getdurationpopupregion(durationselectregion):
    #mselect=None
    mselect=durationselectregion.grow(50,0)
    mselect=mselect.below(150)
    mselect.highlight(1)
    return mselect

######################################
# 
# 
# 
######################################
def selectmusicduration(REGION,duration):
    print "selectmusicduration=%d  >>>>>>" % duration
    rc = False
    mdur60=None
    mdur30=None
    mdur15=None
    mselect=None
    nabove=100
    ricon=gda_utils.EXISTS3("CREATE","EDITCTRL",Pattern("create_img_duration-icon.png").similar(0.69))
    if ricon:
        rdur=ricon.right(15)
        if not rdur:
            print "Error: Moments duration region not found"
            return rc
        else:
            rdur=rdur.grow(15)
            rdur.highlight(1)
    else:
        print "Error: Moments duration region not found"
        return rc
        
    if duration==60:
        mdur60=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-60s.png").similar(0.80))
        if not mdur60:
            mdur60=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-30s.png").similar(0.80))
            if not mdur60:
                mdur60=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-15s.png").similar(0.80))
        if mdur60:
            mdur60.click()
            mselect=getdurationpopupregion(mdur60)
            if mselect:
                mselect.highlight(1)
                if mselect.exists(Pattern("editor_txt_popup-duration.png").similar(0.69).targetOffset(-1,22),10):    #editor_txt_popup-duration
                    mselect.click(Pattern("editor_txt_popup-duration.png").similar(0.69).targetOffset(-1,22))    #editor_txt_popup-duration
                mdur60=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-60s.png").similar(0.80)) #  #create_img_music-duration-60s
                if mdur60:
                    mdur60.highlight(1)
                    rc = True
                else:
                    print "FAILED to verify after selection music duration of 60Sec"
            else:
                print "FAILED to popup music duration of 60Sec"       
        else:
            print "FAILED to find music duration of 60Sec"
                
    elif duration==30:
        mdur30=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-30s.png").similar(0.80))
        if not mdur30:
            mdur30=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-60s.png").similar(0.80))
            if not mdur30:
                mdur30=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-15s.png").similar(0.80))        
        if mdur30:  #create_img_music-duration-60s
            mdur30.click()
            mselect=getdurationpopupregion(mdur30)
            if mselect:
                mselect.highlight(1)
                if mselect.exists(Pattern("editor_txt_popup-duration.png").similar(0.69).targetOffset(-1,-1),10):    # editor_txt_popup-duration.png   
                    mselect.click(Pattern("editor_txt_popup-duration.png").similar(0.69).targetOffset(-1,-1))    # editor_txt_popup-duration.png   
                mdur30=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-30s.png").similar(0.80)) #  #create_img_music-duration-30s
                if mdur30:
                    mdur30.highlight(1)
                    rc = True
                else:
                    print "FAILED to verify after selection music duration of 30Sec"
            else:
                print "FAILED to popup music duration of 30Sec"
        else:
            print "FAILED to find music duration of 30Sec"            
    elif duration==15:
        mdur15=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-15s.png").similar(0.80)) #create_img_music-duration-60s
        if not mdur15:
            mdur15=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-30s.png").similar(0.80))
            if not mdur15:
                mdur15=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-60s.png").similar(0.80))
        if mdur15:
            mdur15.click()
            mselect=getdurationpopupregion(mdur15)
            if mselect:
                mselect.highlight(1)
                if mselect.exists(Pattern("editor_txt_popup-duration.png").similar(0.69).targetOffset(0,-25),10):
                    mselect,click(Pattern("editor_txt_popup-duration.png").similar(0.69).targetOffset(0,-25)) # editor_txt_popup-duration.png    
                mdur15=gda_utils.EXISTS2(rdur,Pattern("create_img_music-duration-15s.png").similar(0.80)) #  #create_img_music-duration-15s
                if mdur15:  #create_img_music-duration-30s
                    mdur15.highlight(1)
                    rc=True
                else:
                    print "FAILED to verify after selection music duration of 30Sec"
            else:
                print "FAILED to popup music duration of 30Sec"
        else:
            print "FAILED to find music duration of 30Sec"            
                        
    else:
        print "FAILED selectmusicduration: invalid duration"
    if not rc:
        print "FAILED selectmusicduration:"
    else:
        mouseMove(gda_utils.getregion("CREATE","TOP"))
    print "selectmusicduration <<<<<<<<<<<<<<<"
    return rc


######################################
# 
# 
# 
######################################
def selectmusic(REGION):
    rc=False

    r=gda_utils.getregion("CREATE","BOTTOM")
    r.highlight(1)
    m=gda_utils.EXISTS2(r,Pattern("create_btn_music.png").similar(0.51))
    if m:
        if m.click(r.getLastMatch())>0:
            rc=True
    return rc
    #gda_utils.CLICK(r,Pattern("create_btn_music.png").similar(0.50).targetOffset(-25,2))

######################################
# 
# 
# 
######################################
def set_duration_moments(REGION,momentscount,durationmode):
    selectmusicduration(REGION,durationmode)
    selectmoments(REGION,momentscount,durationmode)
    selectmusic(REGION)

######################################
# 
# 
# 
######################################
def set_duration(REGION,momentscount,durationmode):
    selectmusicduration(REGION,durationmode)    
    selectmusic(REGION)

######################################
# checks for moments selection popup
# return the moments count,ispopup and pass true or failed false
# 
######################################
def evalmomentscounts(REGION,max,count,song=""):
    global d_report
    test={}
    #test['song']=song
    count += 1
    print "evalmomentscounts: >>>>>> count %d - max moment=%d" % (count,max)
    rc = False
    ispopup=False
    done=False
    test["momentpopup"]="FAILED"
    testname="MomentsPopup_%d-of-%d_%s" % (count,max,song)
    if count>(max):
        print "evalmomentscounts reached: max moment  =%d" % count
        m=gda_utils.EXISTS2(REGION,Pattern("popup_txt_easydoesit.png").similar(0.69),5)#popup_txt_easydoesit
        if m:
            m=gda_utils.EXISTS2(REGION,"popup_btn_easydoesit-gotit.png",5)#popup_btn_easydoesit-gotit
        else:
            rc=False
            gda_utils.ScreenShot(REGION,"",testname)

        #  Pattern("popup_btn_easydoesit-outofhilites.png").similar(0.68).targetOffset(5,81),5)
        
        if m:            
            test["momentpopup"]="PASSED"            
            m.click()
            done=True
            rc = True
        else:
            rc=False
            gda_utils.ScreenShot(REGION,"",testname)
    else:
        print "evalmomentscounts continue selecting moments"
        test["name"]="MomentsNOPopup-%d_of_%d-%s" % (count,max,song)
        m=gda_utils.EXISTS2(REGION,Pattern("popup_btn_easydoesit-outofhilites.png").similar(0.68).targetOffset(5,81),5)
        if m:#popup out of synch with max
            gda_utils.ScreenShot(REGION,"",testname)
            m.click()
            done=True
        else:#not found
            test["momentpopup"]="PASSED"
            rc=True
    print "evalmomentscounts: <<<<<<<<" 
    return count,done,rc,test


         
######################################
# 
# 
# 
######################################        
def selectmoment(REGION,PATTERN,momentid,momentcount,duration,song):
    global d_report
    vid=PATTERN.getFilename()#fullpath
    png=song
    song=song.replace(".png","")
    testname="selectmoment-%dsec-%d_of_%d-%s" % (duration,momentid,momentcount,song)
    print testname
    status=gda_utils.CLICK3("CREATE","4VIDEOS",PATTERN,5,True)
    #status=gda_utils.CLICK(REGION,PATTERN,2)
    test={}
    test['name']=testname
    test['song']=png
    test['video']=vid
    
    if status:
        print "PASSED:%s" % testname
        test['status']="PASSED"
    else:
        print "FAILED:%s" % testname
        test['status']="FAILED"
        gda_utils.ScreenShot(REGION,"",testname)
    return test
    #d_report['processed_songs'].append(test)


######################################
# predefined moment locations based on the GDA tests 
# with numeric videios of four 8min videos
# 
######################################    
def selectmoments(REGION, momentscount,durationmode,png=""):
    global d_report
    passfail = False
    rc=False
    status=0
    print "======================================================="
    print "selectmoments for %d Secs = %d >>>" % (durationmode,momentscount)
    if not selectmusicduration(REGION,60):
        return passfail
    mcount = 0
    test={}
    testselect={}
    #1=========================
    testselect=selectmoment(REGION,Pattern("editor_img_1-4.png").similar(0.69).targetOffset(-142,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #2=========================
    testselect=selectmoment(REGION,Pattern("editor_img_1-4.png").similar(0.69).targetOffset(-4,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #3=========================
    testselect=selectmoment(REGION,Pattern("editor_img_1-4.png").similar(0.69).targetOffset(132,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    
    #4=========================
    testselect=selectmoment(REGION,Pattern("editor_img_1-4.png").similar(0.69).targetOffset(269,0),mcount+1,momentscount,durationmode,png) # editor_img_5-8.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #5=========================
    testselect=selectmoment(REGION,Pattern("editor_img_5-8.png").similar(0.69).targetOffset(-142,0),mcount+1,momentscount,durationmode,png) # editor_img_5-8.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #6=========================
    testselect=selectmoment(REGION,Pattern("editor_img_5-8.png").similar(0.69).targetOffset(-5,0),mcount+1,momentscount,durationmode,png) # editor_img_5-8.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    
    #7=========================
    testselect=selectmoment(REGION,Pattern("editor_img_5-8.png").similar(0.69).targetOffset(132,0),mcount+1,momentscount,durationmode,png) # editor_img_9-12.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #8=========================
    testselect=selectmoment(REGION,Pattern("editor_img_5-8.png").similar(0.69).targetOffset(268,0),mcount+1,momentscount,durationmode,png) # editor_img_9-12.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    
    #9=========================
    testselect=selectmoment(REGION,Pattern("editor_img_9-12.png").similar(0.69).targetOffset(-142,0),mcount+1,momentscount,durationmode,png) # editor_img_9-12.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
   
    #10=========================
    testselect=selectmoment(REGION,Pattern("editor_img_9-12.png").similar(0.69).targetOffset(-5,0),mcount+1,momentscount,durationmode,png) # editor_img_13-16.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #11=========================
    testselect=selectmoment(REGION,Pattern("editor_img_9-12.png").similar(0.69).targetOffset(132,0),mcount+1,momentscount,durationmode,png) # editor_img_13-16.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #12=========================
    testselect=selectmoment(REGION,Pattern("editor_img_9-12.png").similar(0.69).targetOffset(269,0),mcount+1,momentscount,durationmode,png) # editor_img_13-16.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test

    #13=========================
    testselect=selectmoment(REGION,Pattern("editor_img_13-16.png").similar(0.69).targetOffset(-141,0),mcount+1,momentscount,durationmode,png)# editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        return passfail,test
    #14=========================
    testselect=selectmoment(REGION,Pattern("editor_img_13-16.png").similar(0.69).targetOffset(-4,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #15=========================
    testselect=selectmoment(REGION,Pattern("editor_img_13-16.png").similar(0.69).targetOffset(134,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #16=========================
    testselect=selectmoment(REGION,Pattern("editor_img_13-16.png").similar(0.69).targetOffset(270,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    
    #17=========================
    testselect=selectmoment(REGION,Pattern("editor_img_1-4.png").similar(0.69).targetOffset(-269,0),mcount+1,momentscount,durationmode,png) # editor_img_5-8.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    
    #18=========================
    testselect=selectmoment(REGION,Pattern("editor_img_1-4.png").similar(0.69).targetOffset(-132,0),mcount+1,momentscount,durationmode,png) # editor_img_5-8.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    
    #19=========================
    testselect=selectmoment(REGION,Pattern("editor_img_1-4.png").similar(0.69).targetOffset(5,0),mcount+1,momentscount,durationmode,png) # editor_img_5-8.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    
    #20=========================
    testselect=selectmoment(REGION,Pattern("editor_img_1-4.png").similar(0.69).targetOffset(142,0),mcount+1,momentscount,durationmode,png) # editor_img_5-8.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #21=========================
    testselect=selectmoment(REGION,Pattern("editor_img_5-8.png").similar(0.69).targetOffset(-269,0),mcount+1,momentscount,durationmode,png) # editor_img_9-12.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #22=========================
    testselect=selectmoment(REGION,Pattern("editor_img_5-8.png").similar(0.69).targetOffset(-132,0),mcount+1,momentscount,durationmode,png) # editor_img_9-12.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #23=========================
    testselect=selectmoment(REGION,Pattern("editor_img_5-8.png").similar(0.69).targetOffset(5,0),mcount+1,momentscount,durationmode,png) # editor_img_9-12.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #24=========================
    testselect=selectmoment(REGION,Pattern("editor_img_5-8.png").similar(0.69).targetOffset(143,0),mcount+1,momentscount,durationmode,png) # editor_img_9-12.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #25=========================
    testselect=selectmoment(REGION,Pattern("editor_img_9-12.png").similar(0.69).targetOffset(-269,0),mcount+1,momentscount,durationmode,png) # editor_img_13-16.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #26=========================
    testselect=selectmoment(REGION,Pattern("editor_img_9-12.png").similar(0.69).targetOffset(-131,0),mcount+1,momentscount,durationmode,png) # editor_img_13-16.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #27=========================
    testselect=selectmoment(REGION,Pattern("editor_img_9-12.png").similar(0.69).targetOffset(5,0),mcount+1,momentscount,durationmode,png) # editor_img_13-16.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #28=========================
    testselect=selectmoment(REGION,Pattern("editor_img_9-12.png").similar(0.69).targetOffset(142,0),mcount+1,momentscount,durationmode,png) # editor_img_13-16.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test

    #29=========================
    testselect=selectmoment(REGION,Pattern("editor_img_13-16.png").similar(0.69).targetOffset(-268,0),mcount+1,momentscount,durationmode,png)# editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #30=========================
    testselect=selectmoment(REGION,Pattern("editor_img_13-16.png").similar(0.69).targetOffset(-131,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #31=========================
    testselect=selectmoment(REGION,Pattern("editor_img_13-16.png").similar(0.69).targetOffset(6,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    #32=========================
    testselect=selectmoment(REGION,Pattern("editor_img_13-16.png").similar(0.69).targetOffset(143,0),mcount+1,momentscount,durationmode,png) # editor_img_1-4.png
    mcount,done,passfail,test=evalmomentscounts(REGION,momentscount,mcount,png)
    if done:
        print "selectmoments=%d - duration mode=%d" % (momentscount,durationmode)
        test["momentselect"]=testselect
        return passfail,test
    
    print "========================================================"
    print "FAILED past end 32 selectmoments=%d - duration mode=%d count=%d\n%s" % (momentscount,durationmode,mcount,png)
    print "========================================================"
    return False,test
    
######################################
# 
# 
# 
######################################
def clearstory(REGION):
    rc=False
    print "clearstory >>>>>>"
    r=gda_utils.getregion("CREATE","MOMENTS")
    r.highlight(1)
    m=gda_utils.EXISTS2(r,Pattern("editor_img_emptystory.png").similar(0.50),10)
    if m:
        print "clearstory <<<<<<<<"
        return True
    rp=gda_utils.getregion("CREATE","EDITCTRL")
    rp.highlight(2)

    #rp=rp.below(75)
    #rp.highlight(20)
    rc=gda_utils.CLICK2(rp,Pattern("editor_btn_clear.png").similar(0.69)) # editor_btn_clear.png
    if rc:
        rc=popup_areyousure(REGION)
    m=gda_utils.EXISTS2(r,Pattern("editor_img_emptystory.png").similar(0.50),20) # editor_img_music-duration-60s.png
    if m:
        m.highlight(1)
        rc= True
    print "clearstory <<<<<<<<"    
    return rc
######################################
# 
# 
# 
######################################
def popup_keepstory(REGION):
    gda_utils.FIND(REGION,Pattern("popup_txt_title-KEEPTHISSTORY.png").similar(0.98))
    #gda_utils.FIND(REGION,Pattern("popup_txt_info-doyouwanttoclear.png").similar(0.98))
    #click(Pattern("popup_btn_KEEPIT.png").similar(0.98))
    gda_utils.CLICK(REGION,Pattern("popup_btn_CLEARIT.png").similar(0.98))
    
######################################
# 
# 
# 
######################################    
def popup_areyousure(REGION):
    rc=False
    rc=gda_utils.FIND(REGION,Pattern("popup_txt_title-AREYOUSURE.png").similar(0.98))
    #gda_utils.FIND(REGION,)
    #rc=gda_utils.FIND(REGION,Pattern("popup_txt_info-Areyousureyouwanttodothis.png").similar(0.98))
    rc=gda_utils.CLICK(REGION,Pattern("popup_btn_ok-areyousure.png").similar(0.98))
    return rc

######################################
# 
# 
# 
######################################
def getbeatregion(REGION):
    if gda_utils.d_gda_settings["isWindows"]=="True":
        return getbeatswinregion(REGION)
    elif gda_utils.d_gda_settings["isMac"]=="True":
        return getbeatsmacregion(REGION)
    else:
        print "ERROR: Invalid platform not Mac or Win"
    return None
    
######################################
# 
# 
# 
######################################
def getbeatswinregion(REGION):
    rh = 65
    rx = REGION.getX()+10
    rw = REGION.getW()-20
    ry = REGION.getY()+REGION.getH()-210 #200
    newregion = Region(rx,ry,rw,rh)
    #newregion.highlight(1)
    return newregion
######################################
# 
# 
# 
######################################
def getbeatsmacregion(REGION):
    rh = 65
    rx = REGION.getX()+10
    rw = REGION.getW()-20
    ry = REGION.getY()+REGION.getH()-200
    newregion = Region(rx,ry,rw,rh)
    #newregion.highlight(1)
    return newregion

######################################
# 
# 
# 
######################################
def getmomentsregion(beatsregion):
    rh = 90
    rx = beatsregion.getX()
    ry = beatsregion.getY()-110  #110
    rw = beatsregion.getW()
    newregion = Region(rx,ry,rw,rh)
    #newregion.highlight(1)
    return newregion
################################################
#
#
#
################################################
def getmomentsfilename(png,duration,beatsdir,no_eval=False):
    rc= no_eval
    newname = "_viewmoments_%d.png" % duration
    beats = png.replace(".png",newname)
    imgpath = os.path.join(beatsdir, beats)
    if os.path.isfile(imgpath):
        rc = True
        print "File Exists:%s" % imgpath
    return rc,imgpath

def checkexclusivetests(msongs,png):
    rc=False
    if msongs.isexclusive(png):
        #check if png on list
        rc=True
    return rc
################################################
#
# Example
    #selectedmoments-Video_1-4_15sec_4cnt_song_RAINDOWN.png
    #selectedmoments-Video_1-4_30sec_13cnt_song_RAINDOWN.png
    #selectedmoments-Video_1-4_60sec_16cnt_song_RAINDOWN.png
    #selectedmoments-Video_5-8_15sec_4cnt_song_RAINDOWN.png
    #selectedmoments-Video_5-8_30sec_13cnt_song_RAINDOWN.png
    #selectedmoments-Video_5-8_60sec_16cnt_song_RAINDOWN.png
    #selectedmoments-Video_9-12_15sec_4cnt_song_RAINDOWN.png
    #selectedmoments-Video_9-12_30sec_13cnt_song_RAINDOWN.png
    #selectedmoments-Video_9-12_60sec_16cnt_song_RAINDOWN.png
    #selectedmoments-Video_13-16_15sec_4cnt_song_RAINDOWN.png
    #selectedmoments-Video_13-16_30sec_13cnt_song_RAINDOWN.png
    #selectedmoments-Video_13-16_60sec_16cnt_song_RAINDOWN.png

# checks all 18 expected files are found return True,False
# return dict of all file paths found
# return rc=True will process this png song
################################################
def getregressionfilelists(png,beatsdir):
    global d_report
    rc= False

    search = ["_viewbeats_15.png","_viewbeats_30.png","_viewbeats_60.png","_viewmoments_15.png","_viewmoments_30.png","_viewmoments_60.png","1-4_15","1-4_30","1-4_60","5-8_15","5-8_30","5-8_60","9-12_15","9-12_30","9-12_60","13-16_15","13-16_30","13-16_60"]
    flist=os.listdir(beatsdir)
    fsearch=[]
    bname = str(os.path.basename(png).split('/')[-1].split('.')[0])+"_"
    print bname
    #make search item array
    for item in search:
        if "viewbeats" in item:
            fsearch.append(item)
        elif "viewmoments" in item:
            fsearch.append(item)
        else:
            s1="%s%ssec_" % ("selectedmoments-Video_",item)
            fsearch.append(s1)
    found={}
    #iterate all files for match png and fsearch item and set the actual file name in fsearch
    for item in flist:
        if (png in item) or (bname in item):
            for i in range(0,len(fsearch)):
                if fsearch[i] in item:
                    imgpath = os.path.join(beatsdir, item)
                    if os.path.isfile(imgpath):
                        print "key=%s - File Exists:%s" % (fsearch[i],imgpath)
                        found[fsearch[i]]=imgpath
                    else:
                        print "Not exists:%s" % imgpath
        
            
    if len(found)==18:
        rc=True
    #lets skip regression test songs already proccessed as passed
    #will override rc=False from True to False if found as PASSED regression test
    if d_report and "songs" in d_report:
        for song in d_report["songs"]:
            if "png" in song:
                if song["png"]==png:
                    if gda_utils.d_gda_settings['exclusive_songs']==False:
                        if "PASSED" in song:
                            if song["PASSED"]=="Song Regression Tests":
                                rc=False
                    
                    break
                    
            
    return rc,found

################################################
#
#
#
################################################
def savemomentsscreenshot(region,imgpath,msg="save moments screenshot"):
    rc = False
    print "savemomentsscreenshot >>>>>>>>>>>>>>>>"
    found = False

    beatsr = region#getsongbeatsregion(region)
    if not beatsr:
        print "!!!!!!!!!!!!!!!!!!!!!!!!"
        print "FAILED savemomentsscreenshot region not found"
        print "!!!!!!!!!!!!!!!!!!!!!!!!"
        print "savemomentsscreenshot <<<<<<<<<<<<<<<<<"
        return False
    #newname = "_musicbeats_%d.png" % duration
    #beats = png.replace(".png",newname)
    beatsr.highlight(1)
    #wait(2)
    
    #imagepath=ImagePath.getBundlePath()
    #imagepath=imgdir
    fpath = capture(beatsr)
    #print str(fpath)
    if os.path.isfile(str(fpath)):
        print "%s >>> MOVE >>> \n%s" % (fpath,imgpath)
        #imgpath = os.path.join(imagepath, beats)        
        try:
            shutil.move(str(fpath), str(imgpath))
        except:
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
            print "FAILED shutil.move: file not found\n%s" % str(imgpath)
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
        wait(5.0)
        print msg
        if os.path.isfile(imgpath):
            print "SAVED: %s" % imgpath
            rc = True
        else:
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
            print "FAILED file not found: \n%s" % imgpath
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
    else:
        print "!!!!!!!!!!!!!!!!!!!!!!!!"
        print "FAILED capture png: file not found"
        print "!!!!!!!!!!!!!!!!!!!!!!!!"
    print "savemomentsscreenshot <<<<<<<<<<<<<<<<<"    
    return rc
################################################
#
#
#
################################################
def verifymomentsscreenshot(region,imgpath,msg="verify moments screenshot",similarity=0.80):
    rc = False
    print "verifymomentsscreenshot >>>>>>>>>>>>>>>>"
    
    beatsr = region.grow(10)#getbeatsregion(region)
    if not beatsr:
        print "FAILED verifymomentsscreenshot region not found"
        print "verifymomentsscreenshot <<<<<<<<<<<<<<<<<"
        return False
    #newname = "_musicbeats_%d.png" % duration
    #beats = png.replace(".png",newname)
    beatsr.highlight(1)
    #wait(2)

    #imagepath=ImagePath.getBundlePath()
    #imagepath=imgdir
    #fpath = capture(beatsr)
    rc,fmatch=gda_utils.verifyregion(beatsr,imgpath,similarity)
    score=0
    #rc, fmatch = gda_utils.compare_img1path_img2path(fpath,imgpath,0.69)
    if fmatch:
        score="%.2f" % fmatch.getScore()
        print "verifymomentsscreenshot: Similarity score=%s" % score
    if rc:
        print "PASSED: %s" % msg
        rc = True
        fname="PASSED-%s_%s" % (msg,os.path.basename(imgpath))
        gda_utils.ScreenShot(beatsr,fname,"score-"+str(score))
    else:
        print "FAILED: %s" % msg
        beatsr.highlight(10)
        fname="FAILED-%s_%s" % (msg,os.path.basename(imgpath))
        gda_utils.ScreenShot(beatsr,fname,"score-"+str(score))        
    print "verifymomentsscreenshot <<<<<<<<<<<<<<<<<"
    return rc

################################################
#
#
#
################################################
def getbeatsfilename(png,duration,beatsdir,no_eval=False):
    print "getbeatsfilename >>>>>>>>>>>>>>>>"
    rc = no_eval
    newname = "_viewbeats_%d.png" % duration
    beats = str(png).replace(".png",newname)
    imgpath = os.path.join(beatsdir, beats)
    if os.path.isfile(imgpath):
        rc = True
        print "File Exists:%s" % imgpath
    else:
        print "FAILED:%s" % imgpath 
    print "getbeatsfilename <<<<<<<<<<<<<<<<<"    
    return rc,imgpath

################################################
#
#
#
################################################
def savebeatsscreenshot(region,imgpath,msg="save beats screenshot"):
    rc = False
    print "savebeatsscreenshot >>>>>>>>>>>>>>>>"
    found = False

    beatsr = region#getbeatsregion(region)
    if not beatsr:
        print "!!!!!!!!!!!!!!!!!!!!!!!!"
        print "FAILED savebeatsscreenshot region not found"
        print "!!!!!!!!!!!!!!!!!!!!!!!!"
        print "savebeatsscreenshot <<<<<<<<<<<<<<<<<"
        return False
    #newname = "_musicbeats_%d.png" % duration
    #beats = png.replace(".png",newname)
    beatsr.highlight(1)
    #wait(2)

    #imagepath=ImagePath.getBundlePath()
    #imagepath=imgdir
    fpath = capture(beatsr)
    #print str(fpath)
    if os.path.isfile(str(fpath)):
        print "%s >>> MOVE >>> \n%s" % (fpath,imgpath)
        #imgpath = os.path.join(imagepath, beats)
        try:
            shutil.move(str(fpath), str(imgpath))
        except:
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
            print "FAILED shutil.move: file not found\n%s" % str(imgpath)
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
        wait(2)
        print msg
        if os.path.isfile(imgpath):
            print "SAVED: %s" % imgpath
            rc = True
        else:
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
            print "FAILED file not found: %s" % imgpath
            print "!!!!!!!!!!!!!!!!!!!!!!!!"
        
        
    else:
        print "!!!!!!!!!!!!!!!!!!!!!!!!"
        print "FAILED capture png: file not found"
        print "!!!!!!!!!!!!!!!!!!!!!!!!"
    print "savebeatsscreenshot <<<<<<<<<<<<<<<<<"
    return rc
################################################
#
#
#
################################################
def verifybeatsscreenshot(region,imgpath,msg="verify beats screenshot",similarity=0.80):
    rc = False
    print "verifybeatsscreenshot >>>>>>>>>>>>>>>>"
    
    beatsr = region.grow(10) #getbeatsregion(region)
    if not beatsr:
        print "FAILED verifybeatsscreenshot region not found"
        print "verifybeatsscreenshot <<<<<<<<<<<<<<<<<"
        return False
    #newname = "_musicbeats_%d.png" % duration
    #beats = png.replace(".png",newname)
    beatsr.highlight(1)
    #wait(2)

    #imagepath=ImagePath.getBundlePath()
    #imagepath=imgdir
    #fpath = capture(beatsr)
    rc,fmatch=gda_utils.verifyregion(beatsr,imgpath,similarity)
    #rc, fmatch = gda_utils.compare_img1path_img2path(fpath,imgpath,0.69)
    score=0
    if fmatch:
        score="%.2f" % fmatch.getScore()
        print "verifybeatsscreenshot: Similarity score=%s" % score
    if rc:
        print "PASSED: %s" % msg
        fname="PASSED-%s_%s" % (msg,os.path.basename(imgpath))
        gda_utils.ScreenShot(beatsr,fname,"score-"+str(score))
    else:
        print "FAILED: %s" % msg
        beatsr.highlight(10)
        fname="FAILED-%s_%s" % (msg,os.path.basename(imgpath))
        gda_utils.ScreenShot(beatsr,fname,"score-"+str(score))

    print "verifybeatsscreenshot <<<<<<<<<<<<<<<<<"
    return rc
################################################
#
#
#
################################################
def verify_all_moment_selection_regions(REGION,d_filelist,momentcount,duration,song,imgdir):
    print "verify_all_moment_selection_regions >>>>>>:%d - %s\n%s" % (duration,song,imgdir)
    rc = False
    tcount=0
    tests={}
    f1=None

    p1 = Pattern("editor_img_1-4.png").similar(0.80) # editor_img_1-4
    k1 = "selectedmoments-Video_1-4_%isec_" % duration  #selectedmoments-Video_1-4_60sec_

    p2 = Pattern("editor_img_5-8.png").similar(0.80) # editor_img_5-8
    k2 = "selectedmoments-Video_5-8_%isec_" % duration

    p3 = Pattern("editor_img_9-12.png").similar(0.80) # editor_img_9-12
    k3 = "selectedmoments-Video_9-12_%isec_" % duration

    p4 = Pattern("editor_img_13-16.png").similar(0.80) # editor_img_13-16
    k4 = "selectedmoments-Video_13-16_%isec_" % duration
    
    sdur1=str(duration)
    tests={}
    #tests[sdur1]={}
    tests["dir"]=imgdir
    tests["duration"]=sdur1
    smomentc1=str(momentcount)
    tests["count"]=smomentc1
    score=0
    scorelist="SCORES:"
    print "TEST: %s" % str(p1)
    r1 = gda_utils.EXISTS3("CREATE", "4VIDEOS", p1)
    if r1:
        r1=r1.grow(10)
        r1.highlight(1)
        print "Found region: %s - %s" % (k1,song)
        testname1=""
        if k1 in d_filelist:
            testname1=os.path.basename(d_filelist[k1])
            print testname1
            tests["Video_1-4"]={}
            tests["Video_1-4"]["testpng"]=testname1
            tests["Video_1-4"]["status"]="FAILED"
            tests["Video_1-4"]["score"]=-1
            msg = "VERIFY MOMENTS SELECTIONS: %s" % testname1
            print msg
            rc,m_match = gda_utils.verifyregion(r1,d_filelist[k1],0.80)
            if rc and m_match:
                score="%.2f" % m_match.getScore()
                msg= "PASSED-SCORE=%s - %s" % (score,msg)
                print msg
                tests["Video_1-4"]["status"]="PASSED"
                tests["Video_1-4"]["score"]=score
                tcount+=1
                gda_utils.ScreenShot(r1,"",msg)  
            else:
                r1.highlight(10)
                msg="FAILED-%s" % msg
                print msg
                gda_utils.ScreenShot(r1,"",msg)
        else:
            print "Error: invalid path in d_filelist key=%s" % k1
    else:
        print "FAILED: %s" % str(p1)

    print "TEST: %s" % str(p2)
    r2 = gda_utils.EXISTS3("CREATE","4VIDEOS",p2)
    if r2:
        print "Found region: %s - %s" % (k2,song)
        r2=r2.grow(10)
        r2.highlight(1)
        testname1=""
        if k2 in d_filelist:
            testname2=os.path.basename(d_filelist[k2])
            tests["Video_5-8"]={}
            tests["Video_5-8"]["testpng"]=testname2
            tests["Video_5-8"]["status"]="FAILED"
            tests["Video_5-8"]["score"]=-1
            msg="VERIFY MOMENTS SELECTIONS: %s" % testname2
            print msg
            rc,m_match = gda_utils.verifyregion(r2,d_filelist[k2],0.80)
            if rc and m_match:
                score="%.2f" % m_match.getScore()
                msg= "PASSED-SCORE=%s - %s" % (score,msg)
                print msg
                tests["Video_5-8"]["status"]="PASSED"
                tests["Video_5-8"]["score"]=score
                tcount+=1
                gda_utils.ScreenShot(r2,"",msg)
            else:
                r2.highlight(10)
                msg="FAILED-%s" % msg
                print msg
                gda_utils.ScreenShot(r2,"",msg)   
        else:
            print "Error: invalid path in d_filelist key=%s" % k2
    else:
        print "FAILED: %s" % str(p2)

    print "TEST: %s" % str(p3)
    r3 = gda_utils.EXISTS3("CREATE","4VIDEOS",p3)
    if r3:
        print "Found region: %s - %s" % (k3,song)
        r31=r3.grow(10)
        r3.highlight(1)
        testname1=""
        if k3 in d_filelist:
            testname3=os.path.basename(d_filelist[k3])
            tests["Video_9-12"]={}
            tests["Video_9-12"]["testpng"]=testname3
            tests["Video_9-12"]["status"]="FAILED"
            tests["Video_9-12"]["score"]=-1 
            msg="VERIFY MOMENTS SELECTIONS: %s" % testname3
            rc,m_match = gda_utils.verifyregion(r3,d_filelist[k3],0.80)
            if rc and m_match:
                score="%.2f" % m_match.getScore()
                msg= "PASSED-SCORE=%s - %s" % (score,msg)
                print msg
                tests["Video_9-12"]["status"]="PASSED"
                tests["Video_9-12"]["score"]=score                
                tcount+=1
                gda_utils.ScreenShot(r3,"",msg)
            else:
                r3.highlight(10)
                msg="FAILED-%s" % msg
                print msg
                gda_utils.ScreenShot(r3,"",msg)   
        else:
            print "Error: invalid path in d_filelist key=%s" % k3
    else:
        print "FAILED: %s" % str(p3)

    print "TEST: %s" % str(p4)
    r4 = gda_utils.EXISTS3("CREATE","4VIDEOS",p4)
    if r4:
        print "Found region: %s - %s" % (k4,song)
        r4=r4.grow(10)
        r4.highlight(1)
        testname1=""
        if k4 in d_filelist:
            testname4=os.path.basename(d_filelist[k4])
            tests["Video_13-16"]={}
            tests["Video_13-16"]["testpng"]=testname4
            tests["Video_13-16"]["status"]="FAILED"
            tests["Video_13-16"]["score"]=-1
            msg="VERIFY MOMENTS SELECTIONS: %s" % testname4
            rc,m_match = gda_utils.verifyregion(r4,d_filelist[k4],0.80)
            if rc and m_match:
                score="%.2f" % m_match.getScore()
                msg= "PASSED-SCORE=%s - %s" % (score,msg)
                print msg
                tests["Video_13-16"]["status"]="PASSED"
                tests["Video_13-16"]["score"]=score                
                tcount+=1
                gda_utils.ScreenShot(r4,"",msg)
            else:
                r4.highlight(10)
                msg="FAILED-%s" % msg
                print msg
                gda_utils.ScreenShot(r4,"",msg)   
        else:
            print "Error: invalid path in d_filelist key=%s" % k4
    else:
        print "FAILED: %s" % str(p4)
        
    if tcount==4:
        #All passed
        rc = True
        msg= "PASSED-All: %s" % song
        print msg
        gda_utils.ScreenShot(REGION,"",msg) 
    else: #failed
        rc = False
        msg= "FAILED-%d-of-4:-%s" % (tcount,song)
        print msg
        gda_utils.ScreenShot(REGION,"",msg)
        
    print "verify_all_moment_selection_regions <<<<<<<"
    return rc,tests
        

######################################
# After all moment selections done, grab screenshots of the individual video regions
# This will be the input validations to each song. 
# if this does not pass then the beats & moments thumbs are probably invalid too
# We need this for cross validation for bugs
# 1. find the four video regions
# 2. define appropriate region file names with png
# 3. 
######################################
def save_all_moment_selection_regions(REGION,momentcount,duration,song,imgdir):
    print "save_all_moment_selection_regions >>>>>>:%d - %s" % (duration,song)
    rc = False
    tcount=0
    tests={}
    p1 = Pattern("editor_img_1-4.png").similar(0.80) # editor_img_1-4
    r1 = gda_utils.EXISTS3("CREATE","4VIDEOS",p1)
    p2 = Pattern("editor_img_5-8.png").similar(0.80) # editor_img_5-8
    r2 = gda_utils.EXISTS3("CREATE","4VIDEOS",p2) 
    p3 = Pattern("editor_img_9-12.png").similar(0.80) # editor_img_9-12
    r3 = gda_utils.EXISTS3("CREATE","4VIDEOS",p3)
    p4 = Pattern("editor_img_13-16.png").similar(0.80) # editor_img_13-16
    r4 = gda_utils.EXISTS3("CREATE","4VIDEOS",p4)
    
    sdur1=str(duration)
    tests={}
    #tests[sdur1]={}
    tests["dir"]=imgdir
    tests["duration"]=sdur1
    smomentc1=str(momentcount)
    tests["count"]=smomentc1
    
    if r1:
        testname1="selectedmoments-Video_1-4_%dsec_%dcnt_%s" % (duration,momentcount,song)
        path1=os.path.join(imgdir,testname1)
        tests["Video_1-4"]={}
        tests["Video_1-4"]["testpng"]=testname1
        tests["Video_1-4"]["status"]="FAILED"
        msg="SAVE MOMENTS SELECTIONS: %s" % testname1
        if savebeatsscreenshot(r1,path1,msg):
            print "PASSED: %s" % msg
            tests["Video_1-4"]["status"]="PASSED"
            tcount+=1
        else:
            print "FAILED: %s" % msg
            r1.highlight(5)
        
    if r2:        
        testname2="selectedmoments-Video_5-8_%dsec_%dcnt_%s" % (duration,momentcount,song)
        path1=os.path.join(imgdir,testname2)
        tests["Video_5-8"]={}
        tests["Video_5-8"]["testpng"]=testname2
        tests["Video_5-8"]["status"]="FAILED"
        msg="SAVE MOMENTS SELECTIONS: %s" % testname2
        if savebeatsscreenshot(r2,path1,msg):
            print "PASSED: %s" % msg
            tests["Video_5-8"]["status"]="PASSED"
            tcount+=1
        else:
            print "FAILED: %s" % msg
            r2.highlight(5)

    if r3:
        testname3="selectedmoments-Video_9-12_%dsec_%dcnt_%s" % (duration,momentcount,song)
        path1=os.path.join(imgdir,testname3)
        tests["Video_9-12"]={}
        tests["Video_9-12"]["testpng"]=testname3
        tests["Video_9-12"]["status"]="FAILED"
        msg="SAVE MOMENTS SELECTIONS: %s" % testname3
        if savebeatsscreenshot(r3,path1,msg):
            print "PASSED: %s" % msg
            tests["Video_9-12"]["status"]="PASSED"
            tcount+=1
        else:
            print "FAILED: %s" % msg
            r3.highlight(5)
    if r4:        
        testname4="selectedmoments-Video_13-16_%dsec_%dcnt_%s" % (duration,momentcount,song)
        path1=os.path.join(imgdir,testname4)
        tests["Video_13-16"]={}
        tests["Video_13-16"]["testpng"]=testname4
        tests["Video_13-16"]["status"]="FAILED"
        msg="SAVE MOMENTS SELECTIONS: %s" % testname4
        if savebeatsscreenshot(r4,path1,msg):
            print "PASSED: %s" % msg
            tests["Video_13-16"]["status"]="PASSED"
            tcount+=1
        else:
            print "FAILED: %s" % msg
            r4.highlight(5)
            
    if tcount==4:
        #All passed
        rc = True
        print "All 4 PASSED: %s" % song
    else: #failed
        print "%d of 4 FAILED: %s" % (tcount,song)
    print "save_all_moment_selection_regions <<<<<<<"
    return rc,tests
        
######################################
# 
#
# 
######################################
def recordmomentsandbeats(REGION,d_song,png,duration,momentcount):
    global d_report
    sdur="%sSecs" % str(duration)
    if not png:
        return False,d_song
    beatsregion = gda_utils.getregion("CREATE","BEATS") #getbeatsregion(REGION)
    momentsregion= gda_utils.getregion("CREATE","MOMENTS") #getmomentsregion(beatsregion)#need the beats region as reference
    #imgdir = os.path.join("/Automation", "gda_music_images")
    imgdir = gda_utils.d_gda_settings["gda_music_images"]
    tests=None
    rc,tests=save_all_moment_selection_regions(REGION,momentcount,duration,png,imgdir)
    print sdur
    if rc and tests:
        if "regression_moments_select" not in d_song:
            d_song["regression_moments_select"]={}
        d_song["regression_moments_select"][sdur]={}
        d_song["regression_moments_select"][sdur]=tests
    else:
        if tests:
            if "regression_moments_select" not in d_song:
                d_song["regression_moments_select"]={}
            d_song["regression_moments_select"][sdur]={}
            d_song["regression_moments_select"][sdur]=tests
        print "FAILED SKIPPING BEATS & MOMENTS THUMBS REGION CAPTURES"
        return False,d_song
    
    rc,imgpath = getbeatsfilename(png,duration,imgdir,True)
    
    if "regression_beats" not in d_song:
        d_song["regression_beats"]={}
    d_song["regression_beats"][sdur]={}
    d_song["regression_beats"][sdur]["name"]="record-beats-%s_%d" % (png,duration)
    d_song["regression_beats"][sdur]["path"]=imgpath
    d_song["regression_beats"][sdur]["status"]="No Test"
    if rc and savebeatsscreenshot(beatsregion,imgpath):
        d_song["regression_beats"][sdur]["status"]="PASSED"
        rc,imgpath = getmomentsfilename(png,duration,imgdir,True)
        if "regression_story" not in d_song:
            d_song["regression_story"]={}
        d_song["regression_story"][sdur]={}
        d_song["regression_story"][sdur]["name"]="record-moments-%s_%d" % (png,duration)
        #d_song["regression_story"][sdur]["png"]=png
        #d_song["regression_story"][sdur]["duration"]=duration
        d_song["regression_story"][sdur]["path"]=imgpath
        d_song["regression_story"][sdur]["status"]="No Test"
        if rc and savemomentsscreenshot(momentsregion,imgpath):
            d_song["regression_story"][sdur]["status"]="PASSED"
            return True,d_song
        else:
            d_song["regression_story"][sdur]["status"]="FAILED"
            print "FAILED: to savemomentsscreenshot %s" % imgpath
    else:
        d_song["regression_beats"][sdur]["status"]="FAILED"
        print "FAILED: to savebeatsscreenshot %s" % imgpath 
    return False, d_song
        
######################################
# verify all four moments selections 
# if passed, then verify beats and story graph
# test results update into d_song
# d_filelist list of all the png imge files for verification of the given png
# d_song dict is the test report
######################################
def verifymomentsandbeats(REGION,d_song,d_filelist,png,duration,momentcount):
    print "verifymomentsandbeats >>>>>>"
    rc=False
    d_song.pop("PASSED",None)
    msg=""
    if not png:
        msg="no png file"
        print "verifymomentsandbeats <<<<<<< %s" % msg
        return False,d_song,msg
    beatsregion = gda_utils.getregion("CREATE","BEATS") #beatsregion = getbeatsregion(REGION)
    momentsregion= gda_utils.getregion("CREATE","MOMENTS") #momentsregion=getmomentsregion(beatsregion)#need the beats region as reference
    #imgdir = os.path.join("/Automation", "gda_music_images")
    imgdir = gda_utils.d_gda_settings["gda_music_images"]
    rc=verify_all_moment_selection_regions(REGION,d_filelist,momentcount,duration,png,imgdir)
    if rc:
        rc,imgpath = getbeatsfilename(png,duration,imgdir)
        if rc and verifybeatsscreenshot(beatsregion,imgpath):
            rc,imgpath = getmomentsfilename(png,duration,imgdir)
            if rc and verifymomentsscreenshot(momentsregion,imgpath):
                d_song.pop("FAILED",None)
                msg="verifymomentsandbeats_%i" % duration
                d_song["PASSED"]=msg
                print "PASSED verifymomentsandbeats:%s" % d_song["PASSED"]
                gda_utils.ScreenShot(REGION,msg,"T"+png+"-PASS") 
                rc = True
            else:
                rc = False
                msg= "FAILED: verifymomentsscreenshot %i" % duration
                d_song["FAILED"]=msg
                gda_utils.ScreenShot(REGION,msg,"T"+png+"-FAIL") 
        else:
            rc = False
            msg="verifybeatsscreenshot_%i" % duration
            d_song["FAILED"]=msg
            print "FAILED verifymomentsandbeats: %s" % d_song["FAILED"]
            gda_utils.ScreenShot(REGION,msg,"T"+png+"-FAIL") 
    else:
        rc = False
        msg="verify_all_moment_selection_regions %i %i" % (duration,momentcount)
        d_song["FAILED"]=msg
        print "FAILED verifymomentsandbeats: %s" % d_song["FAILED"]
        gda_utils.ScreenShot(REGION,msg,"T"+png+"-FAIL")
    print "verifymomentsandbeats <<<<<<< %s" % png
    return rc, d_song, msg

######################################
# 
# 
# 
######################################
def evalstory_60sec(REGION,moments_png=None, beats_png=None):
    gda_utils.CLICK(REGION,Pattern("editor_btn_PREVIEW.png").similar(0.98)) # editor_btn_PREVIEW.png
    wait(60)
    gda_utils.WAIT(REGION,Pattern("editor_btn_PREVIEW.png").similar(0.98),70) # editor_btn_PREVIEW.png



    if not moments_png:
        gda_utils.FIND(REGION,Pattern("create_img_storymoments-riseup-60s.png").exact()) # create_img_storyhilites-riseup-60s
    if not beats_png:
        gda_utils.FIND(REGION,Pattern("create_img_storymusicbeat-riseup-60s.png").similar(0.98)) # create_img_storymusicbeat-riseup-60s


######################################
# 
# 
# 
######################################
def play_preview(duration):
    gda_utils.CLICK3("CREATE","BOTTOM",Pattern("editor_btn_PREVIEW.png").similar(0.80)) # editor_btn_PREVIEW.png
    wait(duration+10)
    mouseMove(0,0)
    gda_utils.EXISTS3("CREATE","BOTTOM",Pattern("editor_btn_PREVIEW.png").similar(0.81),70) # editor_btn_PREVIEW.png    
    
######################################
# 
# 
# 
######################################
def evalstory_30sec(REGION,moments_png=None, beats_png=None):

    gda_utils.CLICK(REGION,Pattern("create_img_music-duration-60s.png").exact().targetOffset(80,4)) #create_img_music-duration-60s

    gda_utils.CLICK(REGION,Pattern("create_btn_music-15-30-60-select.png").exact()) # create_btn_music-15-30-60-select

    gda_utils.WAIT(REGION,Pattern("create_img_music-duration-30s.png").exact().targetOffset(87,3),10) # create_img_music-duration-30s

    gda_utils.CLICK(REGION,Pattern("editor_btn_PREVIEW.png").similar(0.98)) # editor_btn_PREVIEW.png
    wait(30)
    gda_utils.WAIT(REGION,Pattern("editor_btn_PREVIEW.png").similar(0.98),70) # editor_btn_PREVIEW.png    
    if not moments_png:
        gda_utils.FIND(REGION,Pattern("create_img_storyhilites-riseup-30s.png").similar(0.98)) # create_img_storyhilites-riseup-30s
    if not beats_png:
        gda_utils.FIND(REGION,Pattern("create_img_musicbeats-riseup-30s.png").exact()) #create_img_musicbeats-riseup-30s

######################################
# 
# 
# 
######################################
def evalstory_15sec(REGION,moments_png=None, beats_png=None):
    gda_utils.CLICK(REGION,Pattern("create_img_music-duration-30s.png").exact().targetOffset(86,2)) # create_img_music-duration-30s
   
    gda_utils.CLICK(REGION,Pattern("create_btn_music-15-30-60-select.png").exact().targetOffset(-1,-25)) # create_btn_music-15-30-60-select
    
    gda_utils.WAIT(REGION,Pattern("create_img_music-duration-15s.png").exact().targetOffset(82,3),10) # create_img_music-duration-15s

    gda_utils.CLICK(REGION,Pattern("editor_btn_PREVIEW.png").similar(0.98)) # editor_btn_PREVIEW.png
    wait(15)
    gda_utils.WAIT(REGION,Pattern("editor_btn_PREVIEW.png").similar(0.98),70) # editor_btn_PREVIEW.png    
    if not moments_png:
        gda_utils.FIND(REGION,Pattern("create_img_storyhilites-riseup-15s.png").exact()) # create_img_storyhilites-riseup-15s
    if not beats_png:
        gda_utils.FIND(REGION,Pattern("story_img_musicbeats-riseup-15s.png").exact()) #story_img_musicbeats-riseup-15s

######################################
# 
# 
# 
######################################
def select_moment_to_music(REGION):
    if not gda_utils.WAIT(REGION,Pattern("create_txt_media.png").similar(0.81),5,70): # create_txt_media.png
        return
    clearstory(REGION)
    gda_utils.CLICK(REGION,Pattern("editor_img_1-4.png").exact().targetOffset(-136,0),2) # editor_img_1-4.png
    gda_utils.CLICK(REGION,Pattern("create_img_music-duration-30s.png").similar(0.96).targetOffset(-84,2))
    
######################################
# 
# 
# 
######################################
def record_moments_beat(REGION,duration,max_moments,png):
    global momentstestcounter
    
    selectmusicduration(REGION,duration)
    if selectmoments(REGION,max_moments,duration):
        recordmomentsandbeats(REGION,png,duration)
        gda_utils.CLICK(REGION,Pattern("create_img_music-duration-30s.png").similar(0.96).targetOffset(-84,2))
    else:
        print "FAILED in selectmoments"
    clearstory(REGION)
    momentstestcounter += 1

######################################
# 
# 
# 
######################################    
def setmusic(REGION,png):
    rc=False
    selectmusic(REGION) # select goto music screen
    #p=gda_utils.PATTERN(png,0.59)
    #gda_music_tests.findsongregion(p)
    if gda_music_tests.selectsong_addtovideo(REGION,png,0,60):
        if gda_utils.WAIT(REGION,Pattern("create_txt_media.png").similar(0.71),10):
            return True
    #gda_music_tests.addtovideo(REGION)
    return rc

######################################
# Assumes automation window size Mac{x35,y35,w1280, h836}
# for windows using Autoit we need to identify the inner region w,h relative to mac and set the win size accordingly
# Win,Mac window container border widths are different
# this is global region list for more accurate image query
######################################
def set_CREATE_SCREEN_regions(REGION):
    print "==============================="
    print "IMAGE PATHS"
    imgPath = getImagePath() # get the list
    # to loop through
    for p in imgPath:
        print p
    print "==============================="
    if gda_utils.d_gda_settings["isWindows"]=="True":
        set_Win_CREATE_SCREEN_regions(REGION)
        return True
    elif gda_utils.d_gda_settings["isMac"]=="True":
        set_Mac_CREATE_SCREEN_regions(REGION)
        return True
    else:
        print "ERROR: Invalid platform not Mac or Win"
    return False

######################################
# 
# 
# 
######################################  
def set_Win_CREATE_SCREEN_regions(REGION):
    #SetAppWindow.au3  sets the window size & position
    #$w=1280,$h=920,$x=@DesktopWidth-($w+10),$y=10; move top right corner,WinMove($hWnd,"",$x,$y,$w,$h)
    #main win{X=850,Y=39,Width=1288,Height=855}
    #container {X=854,Y=87,Width=1280,Height=803}
    #dif width=8 left/right edge
    #diff height=52 (the bottom edge and upper menubar
    #;mac=set size of window 1 to {1280, 836}
    #WinMove($hWnd,"GoPro",600,50,1200,875,1)
    BORDER=12       
    screenregion="CREATE"
    subregion="4VIDEOS"
    print subregion
    rx=REGION.getX()+ BORDER
    ry=REGION.getY()+160
    rw=590
    rh=370
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    r2=r.above(30)
    subregion="TITLE"
    print subregion
    rx=REGION.getX()+ BORDER
    ry=REGION.getY()+175
    rw=590
    rh=50
    r=Region(rx,ry,rw,rh)
    r=r2.grow(5)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    
    subregion="BOTTOM"
    print subregion
    rx=REGION.getX()+BORDER
    ry=REGION.getY()+REGION.getH()-70-BORDER
    rw=REGION.getW()-(BORDER*2)
    rh=70
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    
    subregion="WINDOW"
    print subregion
    rx=REGION.getX()
    ry=REGION.getY()
    rw=REGION.getW()
    rh=30
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    
    subregion="MENU"
    print subregion
    rx=REGION.getX()+ BORDER
    ry=REGION.getY()+32#+REGION.getH()-80
    rw=REGION.getW()-(BORDER*2)
    rh=20
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    
    subregion="TOP"
    print subregion
    rx=REGION.getX()+ BORDER
    ry=REGION.getY()+55#+REGION.getH()-80
    rw=REGION.getW()-(BORDER*2)
    rh=60
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    
    subregion="BEATS"
    r=getbeatswinregion(REGION)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    
    subregion="MOMENTS"
    print subregion
    r=getmomentsregion(r)#relative to the beats region win/mac are same
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    
    r1=gda_utils.getregion("CREATE","4VIDEOS")
    r2=gda_utils.getregion("CREATE","MOMENTS")
    r3=gda_utils.getregion("CREATE","TOP")
    
    subregion="PLAYER"
    print subregion
    rx=REGION.getX()+r1.getW()
    ry=REGION.getY()+120
    rw=REGION.getW()-r1.getW()-BORDER
    rh=(r2.getY()-REGION.getY()-120)
    #print rh
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    
######################################
# 
# 
# 
######################################  
def set_Mac_CREATE_SCREEN_regions(REGION):
    #MENUBAR x:0 y:0 w:1280 h: 22  #close win,min win, max/norm win
    #TOP x:0 y:22 w:1280 h:56   #view/create button, alerts,settings, user, account/logout
    #TITLE x:0 y:78 w:590 h:55
    #PLAYER x:602 y:78 w:650 h:420   #play/pause/stop
    #4VIDEOS x:0 y:132 w:590 h:380   #video moments selections
    #EDITCTRL x:0 y:512 w:1280 h:40   #music title, edit length, clip count, clear editor thumbs and moments selection
    #MOMENTS: x:0 y:552 w:1280 h:107  #moments thumb clips
    #BEATS:  x:0 y:659 w:1280 h:95  #music beats wave graph
    #BOTTOM:   x:0 y:754 w:1280 h:80 #music, outro, start over back to media, save export to mp4
    h1=1
    screenregion="CREATE"
    #--------------------------------------------
    subregion="MENUBAR"
    rx=REGION.getX()
    ry=REGION.getY() #relative from top
    rw=1280
    rh=22
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
    
    #--------------------------------------------
    subregion="TOP"
    rx=REGION.getX()
    ry=REGION.getY()+22 #relative from top
    rw=1280
    rh=56
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
    
    #--------------------------------------------
    subregion="TITLE"
    rx=REGION.getX()
    ry=REGION.getY()+78 #relative from top
    rw=590
    rh=55
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
    
    #--------------------------------------------
    subregion="PLAYER"
    rx=REGION.getX()+602
    ry=REGION.getY()+78 #relative from top
    rw=650
    rh=420
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
    
    
    #--------------------------------------------
    subregion="4VIDEOS"
    rx=REGION.getX()
    ry=REGION.getY()+132 #relative from top
    rw=590
    rh=380
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
    
    #--------------------------------------------
    subregion="EDITCTRL"
    rx=REGION.getX()
    ry=REGION.getY()+REGION.getH()-326 #relative from bottom
    rw=1280
    rh=40
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
    
    #--------------------------------------------
    subregion="MOMENTS"
    rx=REGION.getX()
    ry=REGION.getY()+REGION.getH()-280 #relative from bottom
    rw=1280
    rh=107
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
    
    #--------------------------------------------
    subregion="BEATS"
    rx=REGION.getX()
    ry=REGION.getY()+REGION.getH()-177 #relative from bottom
    rw=1280
    rh=96
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
   
    #--------------------------------------------    
    subregion="BOTTOM"
    rx=REGION.getX()
    ry=REGION.getY()+REGION.getH()-80 #relative from bottom
    rw=1280
    rh=80
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
   

    
######################################
# 
# 
# 
######################################
def reset(REGION):
    if gda_music_tests.back(REGION):
        return True
    return False
######################################
# 
# 
# this is obsolete
######################################
def regression_moments_beats(GPA,REGION):
    global momentstestcounter
    failcount=0
    gda_utils.WAIT(REGION,Pattern("create_txt_media.png").similar(0.81),5) # create_txt_media.png
    msongs=gda_music_tests.GDA_music()
    if not msongs:
        print "FAILED to init music song list gda_music_tests.GDA_music"
        return False
    msongs.songreport() 
    gda_music_tests.testmusic_init(msongs)
#    clearstory(REGION)
    if not init_music(REGION,msongs):
        print "FAILED to init music screen song list"
        return False


    for i in range(0,msongs.getGDAsongcount()):
        try:
            title, png, t15, t30, t60 = msongs.getsortednextsong()
            clearstory(REGION)
            setmusic(REGION,png)
            clearstory(REGION)
            selectmusicduration(REGION,60)
            selectmoments(REGION,t60,60)
            verifymomentsandbeats(REGION,png,60)
            selectmusicduration(REGION,30)
            verifymomentsandbeats(REGION,png,30)
            selectmusicduration(REGION,15)
            verifymomentsandbeats(REGION,png,15)
            gda_utils.putDictToFile(gda_utils.d_similarity)
            momentstestcounter += 1
        except Exception as e:
            print "Error: %s" % str(e)
            failcount += 1

######################################
# 
# 
# 
######################################       
def doesrecordfilesexists(png,gda_music_images):
    rc=False
    durations = [60,30,15]
    count=0
    path1=None
    path2=None
    for dur in durations:
        rc1,imgpath1 = getbeatsfilename(png,dur,gda_music_images)
        rc2,imgpath2 = getmomentsfilename(png,dur,gda_music_images)
        if not rc1 or not rc2:
            count+=1
            path1=imgpath1
            path2=imgpath2
    if count==0:
        rc=True
        
    return rc, path1,path2

######################################
# 
# 
# 
######################################
def createmoment():
    print "createmoment >>>>>"
    p=Pattern("editor_img_1-4.png").similar(0.69).targetOffset(-242,0)
    
    bslow=True
    rc= gda_utils.CLICK3("CREATE","4VIDEOS",p,5,bslow)
    if rc:    
        print "createmoment: OK"
    else:
        print "createmonent: FAILED, not clicked"
    print "createmoment <<<<<"
    return rc

######################################
# 
# 
# 
######################################
def previewplay(duration):
    rc = False
    gda_utils.CLICK3("CREATE","BOTTOM",Pattern("create_btn_preview.png").similar(0.69))
    wait(duration+10)
    mouseMove(Location(0,0))
    wait(1)
    mprev=gda_utils.EXISTS3("CREATE","BOTTOM",Pattern("create_btn_preview.png").similar(0.69),10)
    if mprev:
        rc = True  # preview ends and returns to create screen view
    else: # stuck in preview is a fail try to get out of preview
        print "FAILED song & video preview: Stuck and did not return to create screen."
        mstop=gda_utils.EXISTS3("CREATE","BOTTOM", Pattern("create_btn_stop-nohighlight.png").similar(0.69),5)
        if mstop:
            mstop.click()
            wait(1)
            #rbottom=gda_utils.getregion("CREATE","BOTTOM")
            mouseMove(Location(0,0))
            mprev=gda_utils.EXISTS3("CREATE","BOTTOM",Pattern("create_btn_preview.png").similar(0.69),10)
            if not mprev:
                print "FAILED to exit out of preview"
    return rc

######################################
# 
# 
# 
######################################
def putsongitem(songitem,index=-1):
    global d_report
    if index>=0: #valid index
        if index<len(d_report["songs"]):
            d_report["songs"][index]=songitem
            return True
    else: #search for expected song 
        for i in range(0,len(d_report["songs"])):
            if d_report["songs"][i]["png"]==songitem["png"]:
                d_report["songs"][i]=songitem
                return True
    return False
                
######################################
# 
# 
# return dict song item and array index
######################################
def getsongitem(png):
    global d_report
    if "songs" in d_report:
        
        for i in range(0,len(d_report["songs"])):
            songitem=d_report["songs"][i]
            if "png" in songitem:
                if songitem["png"]==png:
                    return songitem,i
    else:
        print str(d_report)
        exit(-1)
    return None,-1

def update_regression_report_summary():
    global d_report
    faillist=[]
    errorlist=[]
    passcount=0
    failcount=0
    songcount=len(d_report["songs"])
    errors=0
    report={}
    sfail=""
    serror=""
    version=""

    if "version" in d_report:
        version=d_report["version"] #Mac 2.0.0.4334
    for songitem in d_report["songs"]:
        sitem=""
        if "png" not in songitem:
            continue # must have song ref
        if "PASSED" in songitem:
            if songitem["PASSED"]=="Song Regression Tests":
                passcount += 1
        elif "FAILED" in songitem:
            failcount += 1
            faillist.append(songitem)
            if songitem["FAILED"] in songitem:
                err=songitem[songitem["FAILED"]]
                if err:
                    if isinstance(err,list):
                        sitem+=str(err)
#                        if len(err)>0:
 #                           for item in err:
  #                              sitem += item+"\n"
                    else:
                        sitem = str(err)+"\n"
                
                sfail += "\nFAILED: %s ---------\n%s" % (songitem["title"],sitem)
        elif "Script ERROR" in songitem:
            errors += 1
            errorlist.append(songitem)
            if "Script ERROR" in songitem:
                err=songitem["Script ERROR"]
                if err:
                    if isinstance(err,list):
                        sitem+=str(err)
#                        for item in err:
 #                           sitem += item+"\n"
                    else:
                        sitem = str(err)+"\n"
               
                serror += "\nERRORS: %s ---------\n%s" % (songitem["title"],sitem)
                
    totaltest=passcount+failcount+errors
    report["title"]="QUIK Song Regression Test %i of %i songs processed %s" % (totaltest,songcount,version)
    report["passfail"]="RUN STATUS: PASSED=%i, FAILED=%i, ERRORS=%i" % (passcount,failcount,errors)
    report["passed"]=passcount
    report["failed"]=failcount
    report["errors"]=errors
    report["songcount"]=songcount
    report["failedinfo"]=faillist
    report["errorlist"]=errorlist
    report["failinfo"]=sfail
    report["errorinfo"]=serror
    d_report["summaryreport"]=report
    print "==================================================="
    print " S U M M A R Y - R E P O R T"
    print "==================================================="
    print report["title"]
    print report["passfail"]
    print report["failinfo"]
    print report["errorinfo"]
    print "==================================================="
    print "==================================================="
        
######################################
# write the test result to JSON format 
# d_song,id required for reporting
# 
######################################
def update_report(passfail,test,msg,title,d_song,id,testmode="gda_create_tests_regression_reportpath"): #gda_create_tests_record_reportpath
    global d_report
    print "REPORT ITEM ========================"
    print "%s-%s - %s" % (str(passfail),title,msg)
    rc=False
    if d_song and id>=0:
        prevdate=gda_utils.getdate()
        if "lastdate" in d_song: 
            prevdate=d_song["lastdate"]
        else:
            prevtime=gda_utils.gettime()     
        if "lasttime" in d_song:
            prevtime=d_song["lasttime"]
            
        d_song["lastdate"] = gda_utils.getdate()
        d_song["lasttime"] = gda_utils.gettime()
        d_song[test] = msg
        if passfail:
            d_song["PASSED"]=test
            if "FAILED" in d_song:
                smsg="FAILED %s-%s: %s\n" % (prevdate,prevtime,str(d_song["FAILED"]))
                #show history from failed to passed state
                if "summaryreport" not in d_report:
                    d_report["summaryreport"]={}                
                if "failinfo" in d_report["summaryreport"]:
                    smsg="FAILED %s-%s: %s\n" % (prevdate,prevtime,str(d_song["FAILED"]))
                    d_report["summaryreport"]["failinfo"] += smsg
                else:
                    d_report["summaryreport"]["failinfo"] = smsg
                del d_song["FAILED"]
            gda_utils.passtotal += 1
        else:
            if "PASSED" in d_song: del d_song["PASSED"]
            d_song["FAILED"]=test
            gda_utils.failtotal += 1
        rc=putsongitem(d_song,id) # update d_report of the song results
        update_regression_report_summary() #refresh run summary
        if testmode in gda_utils.d_gda_settings:
            gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings[testmode])
        else:
            print "================================="
            print "FAILED to save report JSON"
            print "gda_utils.d_gda_settings key error: testmode=%s" % testmode
            print "================================="
    else:
        print "================================="
        print "FAILED to save report JSON"
        print "d_song=%s %s" % (title,testmode)
        print "================================="
    return rc

######################################
#
# 
def nav_to_create_screen():
    if gda_utils.EXISTS3("CREATE","TOP",Pattern("media_btn_add-media.png").similar(0.69).targetOffset(-47,1),5):
        gda_utils.CLICK3("CREATE","TOP",Pattern("media_btn_create.png").similar(0.69))        
    if not gda_utils.EXISTS3("CREATE","TITLE",Pattern("create_txt_media.png").similar(0.69),5): # create_txt_media.png
#        gda_music_tests.back(REGION) #check if gda stuck in music screen, go back
#        if not gda_utils.EXISTS3("CREATE","TITLE",Pattern("create_txt_media.png").similar(0.69),5): # create_txt_media.png
        print "FAILED to find CREATE screen. Testrun will exit"
        return exit(-1)
                    
    
######################################
# iterates the music list and verifies screenshots of 
# the music beats graph and moments graph
# checks regression json and skips songs with test data
# 
######################################
def regression_momentsbeats(REGION):
    global momentstestcounter
    global d_report
    exceptionlist=""
    failmsglist=""
    failcount=0
    errorcount=0
    skippcount=0
    gda_utils.failexit=99
    set_CREATE_SCREEN_regions(REGION)
    gda_music_tests.set_MUSIC_SCREEN_regions(REGION)
        
    if not gda_utils.EXISTS3("CREATE","TITLE",Pattern("create_txt_media.png").similar(0.69),10): # create_txt_media.png
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "FAILED to find CREATE STORY SCREEN"
        gda_music_tests.back(REGION) #check if gda stuck in music screen, go back
        if not gda_utils.EXISTS3("CREATE","TITLE",Pattern("create_txt_media.png").similar(0.69),5): # create_txt_media.png
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "FAILED to find CREATE STORY SCREEN"
            print "Exiting test run"
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            return False
    
    msongs=gda_create_init()
#    rc=clearstory(REGION) #clear to reset for moments selection test
#    rc=createmoment() #set one moment so song iteration can select the next song
    
    title=""
    png=""
    t15=0
    t30=0
    t60=0
    durations = [60,30,15]
    e=""
    tempfail=failcount
    temperr=errorcount

    for i in range(0,msongs.getGDAsongcount()):
        if i>0:
            print "DEBUG exit"
            #break
        reportname="Song-%d. regression_momentsbeats - %s" % (momentstestcounter,title)
        gda_utils.printreport(reportname,False)
        gda_utils.failcount+=gda_utils.failtotal
        gda_utils.failtotal=0
        gda_utils.passcount+=gda_utils.passtotal
        gda_utils.passtotal=0
        if errorcount>temperr:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "ERROR EXCEPTIONS"
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print exceptionlist
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            
        if failcount>tempfail:
            print "::::::::::::::::::::::::::::::::::::::::::::"
            print "WORKFLOW FAILURES"
            print failmsglist
            print "::::::::::::::::::::::::::::::::::::::::::::"
            #if failcount==3 or errorcount==3:
            #    gda,REGION=refreshscreenregion()
        if failcount>10 or errorcount>10: #restart the script if too many workflow errors
            print "Exiting test run"
            gda_utils.ScreenShot(REGION,"","FAILURES")
            exit(-1) #shell should be running in a loop and restart this run
        tempfail=failcount
        temperr=errorcount
        rc=False
        d_song=None #the song node item
        test=None #child test item of d_song
        id=-1
        print "================================================="
        try:
            title, png, t15, t30, t60 = msongs.getsortednextsong()
            rc,d_pngregressionpaths=getregressionfilelists(png,gda_utils.d_gda_settings["gda_music_images"])
            if not rc:
                print "SKIPPED: Not all png regression files found OR\n Already processed as PASSED\nSKIPPED:%s" % png
                continue
            rc = checkexclusivetests(msongs,png)
            if not rc:
                print "SKIPPED: Running in exclusive song mode, SKIPPING:%s" % png
                continue
                
            momentstestcounter += 1
            if rc: #start validate the beats & story & moments files for regression  
                d_song,id=getsongitem(png)
                if not d_song or id<0:
                    e = "ERROR in getsongitem: invalid song obj or id-%s: SKIPPING song %s" % (png,title)
                    update_report(False,"getsongitem",e,title,None,id)
                    continue
                
                rc=selectmusicduration(REGION,60)
                if not rc:
                    e = "ERROR in selectmusicduration-%d: SKIPPING song %s" % (60,title)
                    update_report(rc,"select music duration-60",e,title,d_song,id)
                    continue
                
                rc=clearstory(REGION) #clear to reset for moments selection test
                if not rc:
                    e= "ERROR in clearstory: SKIPPING song %s" % title
                    update_report(rc,"clear story",e,title,d_song,id)
                    continue

                rc=createmoment() #set one moment so song iteration can select the next song
                if not rc:
                    e= "ERROR in createmoment: SKIPPING song %s" % title
                    update_report(rc,"create moment",e,title,d_song,id)
                    continue

                rc=setmusic(REGION,png) #goto music screen and select the song iteration title and return to create screen                
                if not rc:
                    e= "ERROR in setmusic: SKIPPING song %s" % title                    
                    update_report(rc,"setmusic",e,title,d_song,id)
                    continue
                
                rc=clearstory(REGION) #clear to reset for moments selection test
                if not rc:
                    e= "ERROR in clearstory: SKIPPING song %s" % title
                    update_report(rc,"clear story",e,title,d_song,id)
                    continue
                
                rc,test=selectmoments(REGION,t60,60,png)
                if test:
                    d_song["selectmoments"]=test
                if not rc:
                    e= "ERROR in selectmoments: SKIPPING song %s" % title
                    update_report(rc,"select moments-60",e,title,d_song,id)
                    continue

                for dur in durations:
                    if not rc:
                        break #fail song item test on first found fail and continue to next song                    
                    if dur==60:
                        #verify moments selection
                        #play music to end
                        #verifymomentandbeats
                        # report pass/fail json
                        rc=previewplay(dur)
                        if not rc:
                            e = "FAILED: previewplay=%d" % dur
                            update_report(rc,"previewplay-60",e,title,d_song,id)
                            break
                        msg="%s-%d" % (png,dur)
                        gda_utils.ScreenShot(REGION,"",msg)                        
                        rc,d_song,msg=verifymomentsandbeats(REGION,d_song,d_pngregressionpaths,png,dur,t60)

                        print str(rc)
                        if not rc:
                            e = "FAILED: verifymomentsandbeats(REGION,d_song,d_pngregressionpaths,png,dur,t60)"
                            update_report(rc,msg,e,title,d_song,id)
                            break
                        
                    elif dur==30:
                        rc=selectmusicduration(REGION,dur)
                        if not rc:
                            e= "ERROR in selectmusicduration-%d: SKIPPING song %s" % (dur,title)
                            update_report(rc,"select music duration-30",e,title,d_song,id)
                            break
                        rc=previewplay(dur)
                        if not rc:
                            e = "FAILED: previewplay=%d" % dur
                            update_report(rc,"previewplay-30",e,title,d_song,id)
                            break
                        msg="%s-%d" % (png,dur)
                        gda_utils.ScreenShot(REGION,"",msg)
                        rc,d_song,msg=verifymomentsandbeats(REGION,d_song,d_pngregressionpaths,png,dur,t30)
                        if not rc:
                            e = "FAILED: verifymomentsandbeats(REGION,d_song,d_pngregressionpaths,png,dur,t30)"
                            update_report(rc,msg,e,title,d_song,id)
                            break
                    elif dur==15:
                        rc=selectmusicduration(REGION,dur)
                        if not rc:
                            e= "ERROR in selectmusicduration-%d: SKIPPING song %s" % (dur,title)
                            update_report(rc,"select music duration-15",e,title,d_song,id)
                            break
                        rc=previewplay(dur)
                        if not rc:
                            e = "FAILED: previewplay=%d" % dur
                            update_report(rc,"previewplay-15",e,title,d_song,id)
                            break
                        msg="%s-%d" % (png,dur)
                        gda_utils.ScreenShot(REGION,"",msg)
                        rc,d_song,msg=verifymomentsandbeats(REGION,d_song,d_pngregressionpaths,png,dur,t15)
                        if not rc:
                            e = "FAILED: verifymomentsandbeats(REGION,d_song,d_pngregressionpaths,png,dur,t15)"
                            update_report(rc,msg,e,title,d_song,id)
                            break
                    else:
                        print "INVALID MOMENTS DURATION !!!!!!!!!!!!!!!"
                
                if rc: #report passed test
                    update_report(rc,"Song Regression Tests","OK",title,d_song,id)
               
                    
                    #d_song["PASSED"]="True"
                #rc=putsongitem(d_song,id) # update d_report of the song results        
                #gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                gda_utils.putDictToFile(gda_utils.d_similarity)
                
                print "VERIFIED %d: SONG :\n%s\n%s" % (momentstestcounter,png,title)
            else:
                print "SKIPPED %d: SONG :\n%s\n%s" % (momentstestcounter,png,title)                
                skippcount+=1
        except Exception as err:
            errorcount += 1
            # stackinfo=traceback.format_exc()
            tb = sys.exc_info()[2]
            tbinfo = ""
            tbinfo = traceback.extract_tb(tb)
            update_report(False,"Script ERROR",tbinfo,str(title),d_song,id)
    
            print tbinfo  # should print a list with entries like
            exceptionlist += "\n%i-----------------------\n%s\n%s\n" % (errorcount, err, str(tbinfo))
            print "Error: %s" % str(err)
            print "ERROR %d: File not saved" % (momentstestcounter)

            if d_song and id > -1:
                rc = putsongitem(d_song, id)
                gda_utils.putDictToFile(d_report, gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                gda_utils.putDictToFile(gda_utils.d_similarity)
            if len(exceptionlist) > 0:
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print "ERROR EXCEPTIONS"
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print exceptionlist
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print "::::::::::::::::::::::::::::::::::::::::::::"
                print "WORKFLOW FAILURES"
                print failmsglist
                print "::::::::::::::::::::::::::::::::::::::::::::"
                print "Exiting test run"
                gda_utils.ScreenShot(REGION, "", "ExceptionErrors")
                if errorcount > 5:
                    print "EXCEPTION ERRORS: Too many errors=%i exiting this run" % errorcount
                    exit(-1)




######################################
# iterates the music list and grabs screenshots of 
# the music beats graph and moments graph
# doesrecordfilesexists checks for png files and skips
# 
######################################
def record_momentsbeats(REGION):
    global momentstestcounter
    global d_report
    rc=False
    exceptionlist=""
    failmsglist=""
    failcount=0
    errorcount=0
    skippcount=0
    gda_utils.failexit=99
    set_CREATE_SCREEN_regions(REGION)
    gda_music_tests.set_MUSIC_SCREEN_regions(REGION)
# record_momentsbeats
    nav_to_create_screen()
    
    msongs=gda_create_init(True)
    if not msongs:
        print "Error: msongs=gda_create_init(2.0.0.9999,True)"
        return False
#    rc=clearstory(REGION) #clear to reset for moments selection test
#    rc=createmoment() #set one moment so song iteration can select the next song
    tr=None
    if 'testrail' in gda_utils.d_gda_settings:
        tr=gda_utils.d_gda_settings['testrail']
        if not tr:
            print "No Testrail object in settings"
            exit(1)
    else:
        print "No testrail key in settings"
        exit(1)      

    title = ""
    png = ""
    t15 = 0
    t30 = 0
    t60 = 0
    durations = [60,30,15]
    tempfail=failcount
    temperr=errorcount
    for i in range(0,msongs.getGDAsongcount()):
        reportname="Song-%d. record_momentsbeats - %s" % (momentstestcounter,title)
        gda_utils.printreport(reportname,False)
        gda_utils.failcount+=gda_utils.failtotal
        gda_utils.failtotal=0
        gda_utils.passcount+=gda_utils.passtotal
        gda_utils.passtotal=0
        if errorcount>temperr:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "ERROR EXCEPTIONS"
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print exceptionlist
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

        if failcount>tempfail:
            print "::::::::::::::::::::::::::::::::::::::::::::"
            print "WORKFLOW FAILURES"
            print failmsglist
            print "::::::::::::::::::::::::::::::::::::::::::::"
            #if failcount==3 or errorcount==3:    
            #    gda,REGION=refreshscreenregion()
        if failcount>6 or errorcount>6: #restart the script if too many workflow errors
            print "Exiting test run"
            gda_utils.ScreenShot(REGION,"","FAILURES")        
            exit(-1) #shell should be running in a loop and restart this run
        tempfail=failcount
        temperr=errorcount    
        rc=False
        d_song=None #the song node item
        test=None #child test item of d_song
        id=-1
        print "================================================="
        try:
            title, png, t15, t30, t60 = msongs.getsortednextsong()
            rc,imgpath1,imgpath2= doesrecordfilesexists(png,gda_utils.d_gda_settings["gda_music_images"])
                
            momentstestcounter += 1
            if not rc: #create all duration & both region files for regression
                d_testrail_songs=testrail_group(png) # with png music name return dict testrun test cases group
                if not d_testrail_songs:
                    continue
                gda_music_tests.back(REGION) #get out of music screen if out of sync
                d_song,id=getsongitem(png)
                if "FAILED" not in d_song:
                    d_song["FAILED"]=""
                if "PASSED" not in d_song:
                    d_song["PASSED"]=""
                #"work flows-------------------------------------------"
                rc=selectmusicduration(REGION,60)
                if not rc:
                    gda_utils.failtotal += 1
                    e = " ERROR in selectmusicduration-%d: SKIPPING song %s" % (60,title)
                    failmsglist += "\n%s\n" % e
                    d_song["FAILED"] += e + "|"
                    print e
                    rc=putsongitem(d_song,id) # update d_report of the song results        
                    gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                    failcount+=1
                    continue
                
                rc=clearstory(REGION) #clear to reset for moments selection test
                if not rc:
                    gda_utils.failtotal+=1
                    e= " ERROR in clearstory: SKIPPING song %s" % title
                    failmsglist += "\n%s\n" % e
                    d_song["FAILED"]+=e+"|"
                    print e
                    rc=putsongitem(d_song,id) # update d_report of the song results        
                    gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                    failcount+=1
                    continue
                
                rc=createmoment() #set one moment so song iteration can select the next song
                if not rc:
                    gda_utils.failtotal+=1
                    e= " ERROR in createmoment: SKIPPING song %s" % title
                    failmsglist += "\n%s\n" % e
                    d_song["FAILED"]+=e+"|"
                    print e
                    rc=putsongitem(d_song,id) # update d_report of the song results        
                    gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                    failcount+=1
                    continue
                        
                #tr_songtest=d_testrail_songs["song_tests"][0]
                tr_songtest=get_test_title(d_testrail_songs["song_tests"], "Select Song")
                tr_passfail="failed"
                tr_elapsed="1m"
                tr_comment="Sikuli Automation - %s - " % tr_songtest["title"]
                rc=setmusic(REGION,png) #goto music screen and select the song iteration title and return to create screen                
                if not rc:
                    gda_utils.failtotal+=1
                    e = " ERROR in setmusic: SKIPPING song %s" % title
                    failmsglist += "\n%s\n" % e
                    d_song["FAILED"]+=e+"|"                    
                    print e
                    rc = putsongitem(d_song,id) # update d_report of the song results
                    gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                    failcount+=1
                    tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment)
                    if not tc:
                        print "FAILED to report to TESTRAIL"
                    continue
                        
                tc=report_to_testrail(tr_songtest,"passed",tr_elapsed,tr_comment)
                if not tc:
                    print "FAILED to report to TESTRAIL"
                rc=clearstory(REGION) #clear to reset for moments selection test
                if not rc:
                    gda_utils.failtotal+=1
                    e = " ERROR in clearstory: SKIPPING song %s" % title
                    failmsglist += "\n%s\n" % e
                    d_song["FAILED"]+=e+"|"
                    print e
                    rc=putsongitem(d_song,id) # update d_report of the song results        
                    gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                    failcount+=1
                    continue
                        
                #tr_songtest=d_testrail_songs["song_tests"][1]
                tr_songtest = get_test_title(d_testrail_songs["song_tests"], "Moments Select Max 60")
                tr_comment="Sikuli Automation - %s - " % tr_songtest["title"]

                rc,test=selectmoments(REGION,t60,60,png)
                if test:
                    d_song["selectmoments"]=test
                if not rc:
                    gda_utils.failtotal+=1
                    e = " ERROR in selectmoments: SKIPPING song %s" % title
                    failmsglist += "\n%s\n" % e
                    d_song["FAILED"]+=e+"|"
                    print e
                    rc=putsongitem(d_song,id) # update d_report of the song results        
                    gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                    failcount+=1
                    tc=report_to_testrail(tr_songtest,"failed",tr_elapsed,tr_comment+e)
                    if not tc:
                        print "FAILED to report to TESTRAIL"

                    continue
                        
                tc=report_to_testrail(tr_songtest,"passed",tr_elapsed,tr_comment)
                if not tc:
                    print "FAILED to report to TESTRAIL"
                for dur in durations:
                    
                    if dur==60:
                        tr_songtest = get_test_title(d_testrail_songs["song_tests"], "Output MP4 60 Sec")
                        tr_comment = "Sikuli Automation - %s - " % tr_songtest["title"]

                        rc,d_song=recordmomentsandbeats(REGION,d_song,png,dur,t60)
                        if not rc:
                            e = " ERROR in recordmomentsandbeats-%d: SKIPPING song %s" % (dur,title)
                            tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment + e)
                            if not tc:
                                print "FAILED to report to TESTRAIL"
                            update_report(rc,"recordmomentsandbeats-60",e,title,d_song,id,"gda_create_tests_record_reportpath")
                            break
                        else:
                            rc,d_song = exportmp4(REGION,d_song,png,dur)
                            if not rc:
                                e = " ERROR in exportmp4-%d: SKIPPING song %s" % (dur,title)
                                update_report(rc,"exportmp4-60",e,title,d_song,id,"gda_create_tests_record_reportpath")
                                tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment + e)
                                if not tc:
                                    print "FAILED to report to TESTRAIL"
                                break
                            tc = report_to_testrail(tr_songtest, "passed", tr_elapsed, tr_comment)
                            if not tc:
                                print "FAILED to report to TESTRAIL"
                    elif dur==30:
                        tr_songtest = get_test_title(d_testrail_songs["song_tests"], "Output MP4 30 Sec")
                        tr_comment = "Sikuli Automation - %s - " % tr_songtest["title"]
                        rc=selectmusicduration(REGION,dur)
                        if not rc:
                            e= " ERROR in selectmusicduration-%d: SKIPPING song %s" % (dur,title)
                            tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment + e)
                            if not tc:
                                print "FAILED to report to TESTRAIL"
                            update_report(rc,"select music duration-30",e,title,d_song,id,"gda_create_tests_record_reportpath")
                            break

                        rc,d_song=recordmomentsandbeats(REGION,d_song,png,dur,t30)
                        if not rc:
                            e = " ERROR in recordmomentsandbeats-%d: SKIPPING song %s" % (dur,title)

                            tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment + e)
                            if not tc:
                                print "FAILED to report to TESTRAIL"
                            update_report(rc,"recordmomentsandbeats-30",e,title,d_song,id,"gda_create_tests_record_reportpath")
                            break
                        else:
                            rc,d_song = exportmp4(REGION,d_song,png,dur)
                            if not rc:
                                e = " ERROR in exportmp4-%d: SKIPPING song %s" % (dur,title)
                                update_report(rc,"exportmp4-30",e,title,d_song,id,"gda_create_tests_record_reportpath")
                                break
                        tc = report_to_testrail(tr_songtest, "passed", tr_elapsed, tr_comment)
                        if not tc:
                            print "FAILED to report to TESTRAIL"
                    elif dur==15:
                        tr_songtest = get_test_title(d_testrail_songs["song_tests"], "Output MP4 15 Sec")
                        tr_comment = "Sikuli Automation - %s - " % tr_songtest["title"]
                        rc=selectmusicduration(REGION,dur)
                        if not rc:
                            e= " ERROR in selectmusicduration-%d: SKIPPING song %s" % (dur,title)
                            tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment + e)
                            if not tc:
                                print "FAILED to report to TESTRAIL"
                            update_report(rc,"select music duration-15",e,title,d_song,id,"gda_create_tests_record_reportpath")
                            break
                        
                        rc,d_song=recordmomentsandbeats(REGION, d_song, png, dur, t15)
                        if not rc:
                            e = " ERROR in recordmomentsandbeats-%d: SKIPPING song %s" % (dur,title)
                            tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment + e)
                            if not tc:
                                print "FAILED to report to TESTRAIL"
                            update_report(rc,"recordmomentsandbeats-30",e,title,d_song,id,"gda_create_tests_record_reportpath")
                            break
                        else:
                            rc,d_song = exportmp4(REGION,d_song,png,dur)
                            if not rc:
                                e = " ERROR in exportmp4-%d: SKIPPING song %s" % (dur,title)
                                tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment + e)
                                if not tc:
                                    print "FAILED to report to TESTRAIL"
                                update_report(rc,"exportmp4-15",e,title,d_song,id,"gda_create_tests_record_reportpath")
                                break
                        tc = report_to_testrail(tr_songtest, "passed", tr_elapsed, tr_comment)
                        if not tc:
                            print "FAILED to report to TESTRAIL"
                    else:
                        e = " INVALID MOMENTS DURATION !!!!!!!!!!!!!!!"
                        print e
                        tc = report_to_testrail(tr_songtest, "failed", tr_elapsed, tr_comment + e)
                        if not tc:
                            print "FAILED to report to TESTRAIL"
                if rc:
                    #d_song["PASSED"]="True"
                    update_report(rc,"Song Record Tests","OK",title,d_song,id,"gda_create_tests_record_reportpath")
                rc = putsongitem(d_song,id) # update d_report of the song results
                gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                gda_utils.putDictToFile(gda_utils.d_similarity)
                failcount=0 # reset the failures
                print "SAVED %d: Created file:\n%s\n%s" % (momentstestcounter,imgpath1,imgpath2)
            else:
                print "SKIPPED %d: Found file:\n%s\n%s" % (momentstestcounter,imgpath1,imgpath2)
                skippcount+=1
        except Exception as err:
            errorcount += 1
            #stackinfo=traceback.format_exc()
            tb = sys.exc_info()[2]
            tbinfo=""
            tbinfo = traceback.extract_tb(tb)

            print tbinfo # should print a list with entries like
            exceptionlist += "\n%i-----------------------\n%s\n%s\n" % (errorcount,err,str(tbinfo))
            print "Error: %s" % str(err)
            print "ERROR %d: File not saved" % (momentstestcounter)

            if d_song and id>-1:
                rc=putsongitem(d_song,id)
                gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])
                gda_utils.putDictToFile(gda_utils.d_similarity)
            if len(exceptionlist)>0:
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print "ERROR EXCEPTIONS"
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print exceptionlist
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print "::::::::::::::::::::::::::::::::::::::::::::"
                print "WORKFLOW FAILURES"
                print failmsglist
                print "::::::::::::::::::::::::::::::::::::::::::::"
                print "Exiting test run"                
                gda_utils.ScreenShot(REGION,"","ExceptionErrors")
                if errorcount>5:
                    print "EXCEPTION ERRORS: Too many errors=%i exiting this run" % errorcount
                    exit(-1)
            #gda,REGION=refreshscreenregion()       

# record_momentsbeats <<<<        

######################################
# 
# 
# 
######################################    
def story(REGION,duration,moments,png=None):
    global momentstestcounter
    gda_utils.WAIT(REGION,Pattern("create_txt_media.png").similar(0.91),5) # create_txt_media.png
    recordmomentsandbeats(REGION,png,duration)
    exit(-1)
    
    clearstory(REGION)    
    
    
    if selectmoments(REGION,moments,duration):#REGION, momentscount,durationmode):

        evalstory_60sec(REGION)
        evalstory_30sec(REGION)
        evalstory_15sec(REGION)
    else:
        print "ERROR: selectmoments"
        
    clearstory(REGION)    

    
######################################
# 
# 
# 
######################################    
def gda_create_tests(gpa, gpr,duration,moments):
    gpr=gda_utils.refreshregion(gpa)
    if gpr:
        story(gpr,duration,moments,"song_RISEUP.png") #media screen
        gda_utils.putDictToFile(gda_utils.d_similarity)
    else:
        print "ERROR in DEBUG: No region found"


######################################
# 
# 
# 
######################################
def record_moments_beats(gpa,gpr):
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: CAPTURE GDA_MUSIC_MOMENTS & BEATS"
    print "++++++++++++++++++++++++++++++++++"
    record_momentsbeats(gpr)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("CAPTURE GDA_MUSIC_MOMENTS & BEATS")
    
######################################
# 
# 
# 
######################################
def gda_create_init(runmode_rec=False):
    global d_report
    print "gda_create_init >>>>>> %s" % str(runmode_rec)
    gda_utils.d_gda_settings["gda_create_tests_record_reportpath"]=os.path.join(gda_utils.d_gda_settings["gda_music_images"],"gda_create_tests_record.json")
    gda_utils.d_gda_settings["gda_create_tests_regression_reportpath"]=os.path.join(gda_utils.d_gda_settings["gda_music_images"],"gda_create_tests_regression.json")
    rmode="gda_create_tests_regression_reportpath"

    _os="Mac%s" % (gda_utils.d_gda_settings['OSVersion'])
    d_report['version']="%s:%s" % (_os,gda_utils.d_gda_settings['version'])
    if gda_utils.d_gda_settings["isWindows"]=="True":
        _os="Win%s" % (gda_utils.d_gda_settings['OSVersion'])
        d_report['version']="%s:%s" % (_os,gda_utils.d_gda_settings['version'])
    print "=================="    
    print d_report['version']
    print "=================="
    if runmode_rec:
        rmode="gda_create_tests_record_reportpath"
        print rmode
        d_report=gda_utils.getDictFromFile(gda_utils.d_gda_settings[rmode])
    else:
        d_report=gda_utils.getDictFromFile(gda_utils.d_gda_settings[rmode])
    if not d_report:
        d_report={}
        
    msongs=gda_music_tests.GDA_music()
    if not msongs.isready:
        print "FAILED gda_create_init: msongs.isready"
        print "gda_create_init <<<<<<<"
        return None
    #New run we set the default from GDA music list into the d_report json
    if ("songs" not in d_report) or (len(d_report["songs"])<199):
        print "Generating new gda_create_tests_record.json  file"
        
        if not msongs:
            print "FAILED to init music song list gda_music_tests.GDA_music"
            print "gda_create_init <<<<<<<"
            exit(-1)
        elif msongs.getGDAsongcount()<199:
            print "FAILED invalid number of songs=%i of 199" % msongs.getGDAsongcount()
            print "gda_create_init <<<<<<<"
            exit(-2)
            
        d_report["songs"]=msongs.songreport()
        
    gda_music_tests.testmusic_init(msongs)
    if "processed_songs" in d_report:
        print "found %d songs processed" % len(d_report["processed_songs"])
    else:
        print "Starting new song record process"
        d_report["processed_songs"]=[]
    print "gda_create_init <<<<<<<"
        
    return msongs


def refreshscreenregion():
    gpa,gpr=gda_utils.AppStart("Quik")
    set_CREATE_SCREEN_regions(gpr)
    gda_music_tests.set_MUSIC_SCREEN_regions(gpr)
    return gpa,gpr


######################################
#  T E S T R A I L

# testrailtestlist=[" - 1.Select Song",
#                   " - 2.Moments Select Max 60",
#                   " - 3.Output MP4 60 Sec",
#                   " - 4.Output MP4 30 Sec",
#                   " - 5.Output MP4 15 Sec",
#                   " - 6.MP4 in Edits-Scene Detect-60 Sec",
#                   " - 7.MP4 in Edits-Scene Detect-30 Sec",
#                   " - 8.MP4 in Edits-Scene Detect-15 Sec",
#                   " - 9.MP4 in Edits-Song Analysis-60 Sec",
#                   " - 10.MP4 in Edits-Song Analysis-30 Sec",
#                   " - 11.MP4 in Edits-Song Analysis-15 Sec"]

def get_test_title(mtestrail, testtext):
    print "get_test_title >>>>>>>>>>>>"
    print str(mtestrail)
    for test in mtestrail:
        if testtext in test["title"]:
            return test
    print "get_test_title <<<<<<<<<<<"
    return None

def report_to_testrail(tr_songitem,passfail,elapsed,comment):
    if not tr_songitem:
        return None
    #tr.setteststatus("passed",test["id"],test["run_id"],"2s",t)
    #report_testrail_status(passfail, testid, runid, elapsed="5s",comment="sikuli automation reported status"):
    #print str(tr_songitem)
    new_test_status=gda_utils.report_testrail_status(passfail, tr_songitem["id"], tr_songitem["run_id"], elapsed, comment)
    return new_test_status



######################################
# testrail_song_group finds all the song tests
#
#
######################################
def testrail_group2(png):
    song_testrail={}
    tr=None
    if 'testrail' in gda_utils.d_gda_settings:
        tr=gda_utils.d_gda_settings['testrail']
        if not tr:
            print "No Testrail object in settings"
            return None
    else:
        print "No testrail key in settings"
        return None
    print "testrail_group:%s   >>>>>>>>>>>>>>" % png
    name=png.replace(".png","").replace("song_","")

    tlist = [name+" - 1.Select Song",
                      name+" - 2.Moments Select Max 60",
                      name+" - 3.Output MP4 60 Sec",
                      name+" - 4.Output MP4 30 Sec",
                      name+" - 5.Output MP4 15 Sec",
                      name+" - 6.MP4 in Edits-Scene Detect-60 Sec",
                      name+" - 7.MP4 in Edits-Scene Detect-30 Sec",
                      name+" - 8.MP4 in Edits-Scene Detect-15 Sec",
                      name+" - 9.MP4 in Edits-Song Analysis-60 Sec",
                      name+" - 10.MP4 in Edits-Song Analysis-30 Sec",
                      name+" - 11.MP4 in Edits-Song Analysis-15 Sec"]

    for t in tlist:
        print "-----------------------------"
        test=tr.find_test_name(t)
        if test and "title" in test:
            print test["title"]
            if test["status_id"] != 1:
                testlist=tr.find_all_test_contains_name(name)
                print str(testlist)
            print "PASSED: Skipped"
        else:
            print "test not found %s" % t

######################################
# testrail_song_group finds all the song tests
#
#
######################################
def testrail_group(png):
    song_testrail = {}
    tr = None
    if 'testrail' in gda_utils.d_gda_settings:
        tr = gda_utils.d_gda_settings['testrail']
        if not tr:
            print "No Testrail object in settings"
            return None
    else:
        print "No testrail key in settings"
        return None
    print "testrail_group:%s   >>>>>>>>>>>>>>" % png
    name = png.replace(".png", "").replace("song_", "")

    print "-----------------------------"

    song_testrail["song_tests"] = tr.find_all_test_contains_name(name)
    if song_testrail["song_tests"] and len(song_testrail["song_tests"]) > 0:
        for i in range(0, len(song_testrail["song_tests"])):
            title = song_testrail["song_tests"][i]["title"]
            song_testrail[title] = i
    else:
        song_testrail = None
    return song_testrail



                #gda_music_tests.set_MUSIC_SCREEN_regions(gpr)

    #flist=os.listdir("/Users/keithfisher/Dropbox (GoPro)/gda_music_images/160725")
    #for item in flist:
    #    print item
def gettestofgroup(findtest,testgroup):
    for test in testgroup:
        if findtest in test["title"]:
            return test

############################################################################
############################################################################
############################################################################
# D E B U G G I N G

######################################
# for debugging in sikuli ide
#
#
######################################
def test_module1():
    gda_utils.GetEnvInfo()
    gpa, gpr = gda_utils.AppStart("GoPro Quik")
    # record_momentsbeats(gpr)

    # set_CREATE_SCREEN_regions(gpr)

    # gda_music_tests.set_MUSIC_SCREEN_regions(gpr)
    regression_momentsbeats(gpr)


######################################
# for debugging in sikuli ide
#
#
######################################
def test_module2():
    gda_utils.d_gda_settings[ "NO-TestRail"]=True
    gda_utils.GetEnvInfo()
    gpa, REGION = gda_utils.AppStart("GoPro Quik")
    msongs = gda_create_init()
    # exit(1)
    set_CREATE_SCREEN_regions(REGION)
    
    for i in range(1, 10):
        # set_CREATE_SCREEN_regions(REGION)
        # continue
        rc = selectmusicduration(REGION, 60)
        if not rc:
            print "FAILED selectmusicduration(REGION,60)"
            break
        rc = selectmusicduration(REGION, 30)
        if not rc:
            print "FAILED selectmusicduration(REGION,30)"
            break
        rc = selectmusicduration(REGION, 30)
        if not rc:
            print "FAILED selectmusicduration(REGION,30)"
            break
        rc = selectmusicduration(REGION, 15)
        if not rc:
            print "FAILED selectmusicduration(REGION,15)"
            break
        continue

        title = "song_dog.png"
        dur = 60
        rc = selectmusicduration(REGION, dur)
        if not rc:
            print "FAILED selectmusicduration(REGION,dur)"

        rc, d_song = recordmomentsandbeats(REGION, d_song, png, dur, dur)
        if not rc:
            e = "ERROR in recordmomentsandbeats-%d: SKIPPING song %s" % (dur, title)
            print e
        dur = 30
        rc = selectmusicduration(REGION, dur)
        if not rc:
            e = "ERROR in selectmusicduration-%d: SKIPPING song %s" % (dur, title)
            print e
        rc, d_song = recordmomentsandbeats(REGION, d_song, png, dur, dur)
        if not rc:
            e = "ERROR in recordmomentsandbeats-%d: SKIPPING song %s" % (dur, title)
            print e
        dur = 15
        rc = selectmusicduration(REGION, dur)
        if not rc:
            e = "ERROR in selectmusicduration-%d: SKIPPING song %s" % (dur, title)
            print e
        rc, d_song = recordmomentsandbeats(REGION, d_song, png, dur, dur)
        if not rc:
            e = "ERROR in recordmomentsandbeats-%d: SKIPPING song %s" % (dur, title)
            print e


def test_module3():
    gda_utils.d_gda_settings['version']="debugQuik_mac"
    gda_utils.d_gda_settings["NO-TestRail"]=True
    
    gda_utils.GetEnvInfo()
    gpa,REGION=gda_utils.AppStart("GoPro Quik")
    #msongs=gda_create_init()

    set_CREATE_SCREEN_regions(REGION)
    d_song={}
    #title, png, t15, t30, t60 = msongs.getsortednextsong()
    png = "song_TEST%d.png" % 1
    #d_song=testrail_group(png)
    rc,d_song=exportmp4(REGION,d_song,png,1)


def test_module4():
    gda_utils.d_gda_settings['version']="debugQuik_win"
    gda_utils.d_gda_settings["NO-TestRail"]=True
    
    gda_utils.GetEnvInfo()
    gpa,REGION=gda_utils.AppStart("GoPro Quik")
    msongs=gda_create_init()
    #exit(1)
    set_CREATE_SCREEN_regions(REGION)
    gda_music_tests.set_MUSIC_SCREEN_regions(REGION)
    selectmusic(REGION)
    gda_music_tests.cancelmusicscreen()    
    selectmusicduration(REGION,15)
    selectmusicduration(REGION,30)
    selectmusicduration(REGION,60)
    selectmusicduration(REGION,30)
    selectmusicduration(REGION,15)
    selectmusicduration(REGION,60)

    exit(1)
    #rc=popup_areyousure_deletefile(REGION)
    d_song={}
    tr=None
    if 'testrail' in gda_utils.d_gda_settings:
        tr=gda_utils.d_gda_settings['testrail']
        if not tr:
            print "No Testrail object in settings"
            exit(1)
    else:
        print "No testrail key in settings"
        exit(1)      
    print "testcases found=%d" % len(tr.testcases)
    for i in range(1,200):
        print "======================================================"
        title, png, t15, t30, t60 = msongs.getsortednextsong()
        print png
        testgrp=[" - Select Song", " - Moments Select Max 60", " - Output MP4 60 Sec"," - Output MP4 30 Sec"," - Output MP4 15 Sec"]
        d_song=testrail_group(png)
        if d_song:
            print str(d_song)

            for test in testgrp: #d_song["song_tests"]:
                print "------------------------------------"
                tr_songtest=gettestofgroup(test,d_song["song_tests"])
                #tr_songtest=test
                tr_passfail="failed"
                tr_elapsed="1m"
                tr_comment="FAILED: Sikuli Automation - %s - " % tr_songtest["title"]
                n=randint(1,6)
                if n>1:
                    tr_passfail="passed"
                    tr_comment = "Sikuli Automation - %s - " % tr_songtest["title"]
                print "%s - %s" % (tr_songtest["title"], str(tr_songtest))
                tc = report_to_testrail(tr_songtest, tr_passfail, tr_elapsed, tr_comment)
                print str(tc)
                if n==1:
                    break
    exit(1)
        # tlist=[]
        # s="%s - Select Song" % name
        # tlist.append(s)
        # s="%s - Moments Select Max 60" % name
        # tlist.append(s)
        # s="%s - Output MP4 60 Sec" % name
        # tlist.append(s)
        # s="%s - Output MP4 30 Sec" % name
        # tlist.append(s)
        # s="%s - Output MP4 15 Sec" % name
        # tlist.append(s)
        # s="%s - MP4 Edits Scene Detect" % name
        # tlist.append(s)
        # s="%s - Song Analysis" % name
        # tlist.append(s)
        
        # for t in tlist:
        #     print "-----------------------------"
        #     test=tr.find_test_name(t)
        #     if test and "title" in test:
        #         print test["title"]
        #         if test["status_id"] != 1:
        #             teststatus=tr.setteststatus("passed",test["id"],test["run_id"],"2s",t)
        #             print str(teststatus)
        #         print "PASSED: Skipped"
        #     else:
        #         print "test not found %s" % t
    #exit(1)               
        #png = "song_TEST%d.png" % i
        #rc,d_song=exportmp4(REGION,d_song,png,i)
        
#    scrubtest(REGION)
    
    
######################################
# for debugging in sikuli ide
# 
# KEEP THIS COMMENTED when checking in to GIT
######################################    
#test_module1()
#test_module4()
#test_module3()



# record_momentsbeats
# 	set_CREATE_SCREEN_regions(REGION)
# 	gda_music_tests.back(REGION)
# 	gda_utils.EXISTS3
# 	msongs=gda_create_init("2.0.0.9999")
# 	clearstory(REGION)
# 	init_music(REGION,msongs)
# 	msongs.getGDAsongcount()
# 	gda_utils.printreport(reportname)
# 	title, png, t15, t30, t60 = msongs.getsortednextsong()
# 	rc,imgpath1,imgpath2= doesrecordfilesexists(png,gda_utils.d_gda_settings["gda_music_images"])
# 	selectmusicduration(REGION,60)
#     setmusic(REGION,png)                
# 	clearstory(REGION)
# 	selectmoments(REGION,t60,60,png)
# 	recordmomentsandbeats(REGION,png,dur)
# 	gda_utils.putDictToFile(d_report,gda_utils.d_gda_settings["gda_create_tests_record_reportpath"])


