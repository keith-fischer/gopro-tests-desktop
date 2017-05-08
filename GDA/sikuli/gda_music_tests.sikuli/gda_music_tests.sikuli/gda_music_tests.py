
import os
import sys
import traceback
import platform
from os.path import expanduser
import json
import org.sikuli.script.ImagePath;
import shutil
from time import strftime
from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython

import gda_utils
#import gda_create_tests
################################################
#
#
#
################################################
class GDA_music:
    def __init__(self):        
        self.reset()
        self.musiclistfile = "GDA_musiclist.json"
        self.automation_root = ""
        self.evalplatform()
        self.job_name = "GDA_Regression"
        self.isready=False
        self.musiclist = self.load_json(self.automation_root+self.musiclistfile)
        if self.musiclist:
            print "musiclist items count=%i" % len(self.musiclist)
            self.isready=True
        self.missingsongs = []
        self.newsongs = []
        self.currentsong = {}
        #these songs are skipped from testing in the sortedsonglist
#        self.skipsongslist = [
#            "song_THENIGHTWEDANCED.png",            
#            "song_CHOKINCHICKENS.png",
#            "song_GLASSDARKLY.png",
#            "song_HUNDREDDOLLAGIRLZ.png"]
        self.skipsongslist = []
        #start regression script args with "ex_songs", only runs songlist in exclusivesonglist = []

        self.exclusivesonglist = [
            "song_BURYMYLOVE.png",
            #"song_CARRYMEBACKHOME.png",                
            #"song_COLDFEET.png", # song_COLDFEET                
            #"song_COMBATREADY.png", # song_COMBATREADY                
            #"song_BRINGMEBACKTOLIFE.png", #PASS
            "song_CRANKIT.png"] # song_CRANKIT
        
        #Sorted Quik song list with plus
        #validated 2017/02/27
        self.sortedsonglist = [ #freebies
			"song_THENIGHTWEDANCED.png", #176 song_THENIGHTWEDANCED.png
			"song_AFTERGLOW.png", #2 song_AFTERGLOW.png
			"song_BRINGIT.png", #28 song_BRINGIT.png
			"song_COMETHRU.png", #40 song_COMETHRU.png
			"song_DAFTCRUNK.png", #46 song_DAFTCRUNK.png
			"song_FEELTHELOVE.png", #62 song_FEELTHELOVE.png
			"song_GUILTYMAN.png", #75 song_GUILTYMAN.png
			"song_HIDEANDFREAK.png", #83 song_HIDEANDFREAK.png
			"song_RAINDOWN.png", #144 song_RAINDOWN.png
			"song_RISEUP.png", #148 song_RISEUP.png >>>>> plus songs
            #>>>>>>>>>>>>>>
			"song_ARECKONING.png", #9 song_ARECKONING.png
			"song_ATICKOFTIME.png", #13 song_ATICKOFTIME.png
			"song_AWONDERFULSACRIFICE.png", #15 song_AWONDERFULSACRIFICE.png
			"song_ATLDIRTYBIRDS.png", #14 song_ATLDIRTYBIRDS.png
			"song_ABOVEANDBELOW.png", #1 song_ABOVEANDBELOW.png
			"song_AINTNOWAY.png", #3 song_AINTNOWAY.png
			"song_ALLIKNOW.png", #4 song_ALLIKNOW.png
			"song_ALLYOURLIGHTS.png", #5 song_ALLYOURLIGHTS.png
			"song_AMAZEBALLS.png", #6 song_AMAZEBALLS.png
			"song_AMIGOS4LIFE.png", #7 song_AMIGOS4LIFE.png
			"song_ARABIANNIGHTS.png", #8 song_ARABIANNIGHTS.png
			"song_ARIZONA.png", #10 song_ARIZONA.png
			"song_ARROOTSYFINGERPICKING.png", #11 song_ARROOTSYFINGERPICKING.png
			"song_ASITEVERWAS.png", #12 song_ASITEVERWAS.png
			"song_BFF.png", #20 song_BFF.png
			"song_BACKFROMTHEROAD.png", #16 song_BACKFROMTHEROAD.png
			"song_BACKSTAGE.png", #17 song_BACKSTAGE.png
			"song_BADBLOOD.png", #18 song_BADBLOOD.png
			"song_BANDSAW.png", #19 song_BANDSAW.png
			"song_BIPOLAR.png", #23 song_BIPOLAR.png
			"song_BIGBOY.png", #21 song_BIGBOY.png
			"song_BIGLIFE.png", #22 song_BIGLIFE.png
			"song_BITEME.png", #24 song_BITEME.png
			"song_BLAME.png", #25 song_BLAME.png
			"song_BLINDEDBYTHESUN.png", #26 song_BLINDEDBYTHESUN.png
			"song_BLOODFEUD.png", #27 song_BLOODFEUD.png
			"song_BRINGMEBACKTOLIFE.png", #29 song_BRINGMEBACKTOLIFE.png
			"song_BRINGMESPIRITANIMAL.png", #30 song_BRINGMESPIRITANIMAL.png
			"song_BURYMYLOVE.png", #31 song_BURYMYLOVE.png
			"song_CAICOS.png", #32 song_CAICOS.png
			"song_CANNESCUTIT.png", #33 song_CANNESCUTIT.png
			"song_CARRYMEBACKHOME.png", #34 song_CARRYMEBACKHOME.png
			"song_CHOKINCHICKENS.png", #35 song_CHOKINCHICKENS.png
			"song_CITYLIGHTS.png", #36 song_CITYLIGHTS.png
			"song_CLUBCORNERS.png", #37 song_CLUBCORNERS.png
			"song_COLDFEET.png", #38 song_COLDFEET.png
			"song_COMBATREADY.png", #39 song_COMBATREADY.png
			"song_CONQUISTADOR.png", #41 song_CONQUISTADOR.png
			"song_CONTAGIOUS.png", #42 song_CONTAGIOUS.png
			"song_CRANBERRY.png", #43 song_CRANBERRY.png
			"song_CRANKIT.png", #44 song_CRANKIT.png
			"song_CRUNCHIT.png", #45 song_CRUNCHIT.png
			"song_DJBLOWUPTHESPEAKERS.png", #50 song_DJBLOWUPTHESPEAKERS.png
			"song_DARKFADER.png", #47 song_DARKFADER.png
			"song_DARKWOODS.png", #48 song_DARKWOODS.png
			"song_DEADANDGONE.png", #49 song_DEADANDGONE.png
			"song_DOYOUFEELALIVE.png", #52 song_DOYOUFEELALIVE.png
			"song_DOPEDELUXE.png", #51 song_DOPEDELUXE.png
			"song_DREAMPOP.png", #53 song_DREAMPOP.png
			"song_DROPPINDIMES.png", #54 song_DROPPINDIMES.png
			"song_ELDIABLO.png", #55 song_ELDIABLO.png
			"song_ETERNALLYYOURS.png", #56 song_ETERNALLYYOURS.png
			"song_EVEREST.png", #57 song_EVEREST.png
			"song_EVERYTHING.png", #58 song_EVERYTHING.png
			"song_FALLINGFASTER.png", #59 song_FALLINGFASTER.png
			"song_FEELITCOMINGON.png", #60 song_FEELITCOMINGON.png
			"song_FEELSLIKEIMADEIT.png", #61 song_FEELSLIKEIMADEIT.png
			"song_FIFTEENWAYS.png", #63 song_FIFTEENWAYS.png
			"song_FIREINTHEENGINEROOM.png", #64 song_FIREINTHEENGINEROOM.png
			"song_FLATBUSH.png", #65 song_FLATBUSH.png
			"song_FOLLOWALONG.png", #66 song_FOLLOWALONG.png
			"song_FRAGMENTS.png", #67 song_FRAGMENTS.png
			"song_FRETCOLLECTOR.png", #68 song_FRETCOLLECTOR.png
			"song_GETTINGBUZZED.png", #69 song_GETTINGBUZZED.png
			"song_GLASSDARKLY.png", #70 song_GLASSDARKLY.png
			"song_GLOCKNROLL.png", #71 song_GLOCKNROLL.png
			"song_GODWILLCUTYOUDOWN.png", #72 song_GODWILLCUTYOUDOWN.png
			"song_GOOD4THAHOOD.png", #73 song_GOOD4THAHOOD.png
			"song_GROOVEMEMATE.png", #74 song_GROOVEMEMATE.png
			"song_GYROSCOPE.png", #76 song_GYROSCOPE.png
			"song_HALLOWEDGROUND.png", #77 song_HALLOWEDGROUND.png
			"song_HANDSUPFORLOVE.png", #78 song_HANDSUPFORLOVE.png
			"song_HAUNTEDCOMPUTER.png", #79 song_HAUNTEDCOMPUTER.png
			"song_HEAVYFOG.png", #80 song_HEAVYFOG.png
			"song_HEAVYWEATHER.png", #81 song_HEAVYWEATHER.png
			"song_HEROESDRESSINBLACK.png", #82 song_HEROESDRESSINBLACK.png
			"song_HINDSIGHT.png", #84 song_HINDSIGHT.png
			"song_HOLDYOURHEADUP.png", #85 song_HOLDYOURHEADUP.png
			"song_HOTANDCOLD.png", #86 song_HOTANDCOLD.png
			"song_HUNDREDDOLLAGIRLZ.png", #87 song_HUNDREDDOLLAGIRLZ.png
			"song_IDAREYOU.png", #88 song_IDAREYOU.png
			"song_INAROW.png", #89 song_INAROW.png
			"song_INTHAMAISON.png", #92 song_INTHAMAISON.png
			"song_INTHEMIST.png", #93 song_INTHEMIST.png
			"song_INDIE.png", #90 song_INDIE.png
			"song_INSPIRED.png", #91 song_INSPIRED.png
			"song_ITSOURS.png", #94 song_ITSOURS.png
			"song_JAYLTER.png", #95 song_JAYLTER.png
			"song_JOYRIDE.png", #96 song_JOYRIDE.png
			"song_JUSTALITTLE.png", #97 song_JUSTALITTLE.png
			"song_KEEPTHEFAITHALIVE.png", #98 song_KEEPTHEFAITHALIVE.png
			"song_KILLINFLOOR.png", #99 song_KILLINFLOOR.png
			"song_KNUCKLEDRAGGER.png", #100 song_KNUCKLEDRAGGER.png
			"song_LASTCHANCESURVIVAL.png", #101 song_LASTCHANCESURVIVAL.png
			"song_LEANBACKSAX.png", #102 song_LEANBACKSAX.png
			"song_LETSMAKEADEAL.png", #104 song_LETSMAKEADEAL.png
			"song_LETSGETSAXY.png", #103 song_LETSGETSAXY.png
			"song_LEVEL.png", #105 song_LEVEL.png
			"song_LIFEDOESNOTSUCK.png", #106 song_LIFEDOESNOTSUCK.png
			"song_LIGHTEMUP.png", #107 song_LIGHTEMUP.png
			"song_LIGHTNINGRYDER.png", #108 song_LIGHTNINGRYDER.png
			"song_LONGLEGS.png", #109 song_LONGLEGS.png
			"song_LOSTCAUSES.png", #110 song_LOSTCAUSES.png
			"song_LOVECONQUERSALL.png", #111 song_LOVECONQUERSALL.png
			"song_MADISONSQUARE.png", #112 song_MADISONSQUARE.png
			"song_MADRIDISTA.png", #113 song_MADRIDISTA.png
			"song_MAINFLOOR.png", #114 song_MAINFLOOR.png
			"song_MAKEITMOVE.png", #115 song_MAKEITMOVE.png
			"song_MAKINGFYRE.png", #116 song_MAKINGFYRE.png
			"song_MAPODOUFU.png", #117 song_MAPODOUFU.png
			"song_MATTEROFFACTION.png", #118 song_MATTEROFFACTION.png
			"song_MEADOWMIND.png", #119 song_MEADOWMIND.png
			"song_MEETME.png", #120 song_MEETME.png
			"song_MOCKDRAFT.png", #121 song_MOCKDRAFT.png
			"song_MOONSHINEANDGASOLINE.png", #122 song_MOONSHINEANDGASOLINE.png
			"song_MOVINGUP.png", #123 song_MOVINGUP.png
			"song_NEVERNEEDEDYOU.png", #124 song_NEVERNEEDEDYOU.png
			"song_NEWDAY.png", #125 song_NEWDAY.png
			"song_NEXTDOOR.png", #126 song_NEXTDOOR.png
			"song_NIGHTOFTHECRICK.png", #127 song_NIGHTOFTHECRICK.png
			"song_NOTLOOKINBACK.png", #128 song_NOTLOOKINBACK.png
			"song_NUCLEAR.png", #129 song_NUCLEAR.png
			"song_ONTHEDL.png", #132 song_ONTHEDL.png
			"song_ONCEAGAIN.png", #130 song_ONCEAGAIN.png
			"song_ONEOFAKIND.png", #131 song_ONEOFAKIND.png
			"song_OPENSKY.png", #133 song_OPENSKY.png
			"song_PALESAND.png", #134 song_PALESAND.png
			"song_PARTYWILLCOMEALIVE.png", #135 song_PARTYWILLCOMEALIVE.png
			"song_PHOTOGRAPHS.png", #136 song_PHOTOGRAPHS.png
			"song_PIXIE.png", #137 song_PIXIE.png
			"song_PLAYTHATBACKWUT.png", #138 song_PLAYTHATBACKWUT.png
			"song_POUNDITOUT.png", #139 song_POUNDITOUT.png
			"song_PUNCHING.png", #140 song_PUNCHING.png
			"song_PUSHUPTHEBEAT.png", #141 song_PUSHUPTHEBEAT.png
			"song_PUZZLE.png", #142 song_PUZZLE.png
			"song_PYRAMID.png", #143 song_PYRAMID.png
			"song_REACHFORTH.png", #145 song_REACHFORTH.png
			"song_READYORNOT.png", #146 song_READYORNOT.png
			"song_REASONS.png", #147 song_REASONS.png
			"song_ROASTEDTURNT.png", #149 song_ROASTEDTURNT.png
			"song_ROCKYOURWORLD.png", #151 song_ROCKYOURWORLD.png
			"song_ROCKAWAY.png", #150 song_ROCKAWAY.png
			"song_RUSHES.png", #152 song_RUSHES.png
			"song_SCENTOFAWARENESS.png", #153 song_SCENTOFAWARENESS.png
			"song_SCREENDOORSLAM.png", #154 song_SCREENDOORSLAM.png
			"song_SECONDSIGHT.png", #155 song_SECONDSIGHT.png
			"song_SERENGETI.png", #156 song_SERENGETI.png
			"song_SHAKE.png", #157 song_SHAKE.png
			"song_SHAKEITOUT.png", #158 song_SHAKEITOUT.png
			"song_SKULKY.png", #159 song_SKULKY.png
			"song_SMOKINFIRE.png", #160 song_SMOKINFIRE.png
			"song_SOMEONECHORDS.png", #161 song_SOMEONECHORDS.png
			"song_SOUNDANDSIGNAL.png", #162 song_SOUNDANDSIGNAL.png
			"song_SOUNDBOI.png", #163 song_SOUNDBOI.png
			"song_STILLFRAMES.png", #164 song_STILLFRAMES.png
			"song_STRANGECONDITION.png", #165 song_STRANGECONDITION.png
			"song_STRINGOFTRUTH.png", #166 song_STRINGOFTRUTH.png
			"song_STRONGWORDS.png", #167 song_STRONGWORDS.png
			"song_SUGARGIRL.png", #168 song_SUGARGIRL.png
			"song_SURGE.png", #169 song_SURGE.png
			"song_SWINGOVER.png", #170 song_SWINGOVER.png
			"song_TALIGADO.png", #171 song_TALIGADO.png
			"song_TELLMETOSTAY.png", #173 song_TELLMETOSTAY.png
			"song_TELLER.png", #172 song_TELLER.png
			"song_THEAIRUPNORTH.png", #174 song_THEAIRUPNORTH.png
			"song_THEBOARDERLANDS.png", #175 song_THEBOARDERLANDS.png
			"song_THEOLIOTHEORY.png", #177 song_THEOLIOTHEORY.png
			"song_THEPOWEROUT.png", #178 song_THEPOWEROUT.png
			"song_THERIODEAL.png", #179 song_THERIODEAL.png
			"song_THRILLSWITCH.png", #180 song_THRILLSWITCH.png
			"song_THUNDERDROME.png", #181 song_THUNDERDROME.png
			"song_TIMETOFLY.png", #182 song_TIMETOFLY.png
			"song_TOYDIVISION.png", #183 song_TOYDIVISION.png
			"song_TRYSOHARD.png", #184 song_TRYSOHARD.png
			"song_TWERKINPROGRESS.png", #185 song_TWERKINPROGRESS.png
			"song_VINTAGENIGHTS.png", #186 song_VINTAGENIGHTS.png
			"song_WALKINTALL.png", #187 song_WALKINTALL.png
			"song_WANNAHAVEFUN.png", #188 song_WANNAHAVEFUN.png
			"song_WANTEDMAN.png", #189 song_WANTEDMAN.png
			"song_WHATWESTARTED.png", #190 song_WHATWESTARTED.png
			"song_WHENSHEWAS.png", #191 song_WHENSHEWAS.png
			"song_WHITEGIRLS.png", #192 song_WHITEGIRLS.png
			"song_WHITEWASHEDTOMB.png", #193 song_WHITEWASHEDTOMB.png
			"song_WHYDOI.png", #194 song_WHYDOI.png
			"song_WORKOUT.png", #195 song_WORKOUT.png
			"song_YANGBANG.png", #196 song_YANGBANG.png
			"song_ZEROFSGIVEN.png", #197 song_ZEROFSGIVEN.png
			"song_ZEROHOUR.png", #198 song_ZEROHOUR.png
			"song_ZOMBIEDROP.png"] #199 song_ZOMBIEDROP.png

    def findsortedsongindex(self,png):
        for i in range(0,len(self.sortedsonglist)):
            if png==self.sortedsonglist[i]:
                return i
        return -1

    ################################################
    # return False if is in exclusive_songs mode and png is NOT in exclusive song list
    # return True if not in n exclusive_songs mode and uses self.sortedsonglist
    # return True if is in exclusive_songs mode and png IS in the exclusive song list
    ################################################         
    def isexclusive(self, png):
        rc=False
        if gda_utils.d_gda_settings['exclusive_songs']==True: #False return true using self.sortedsonglist song list
            for song in self.exclusivesonglist:
                if png==song:
                    print "isexclusive TRUE:%s" % str(song)
                    rc=True
                    break
        else:
            print "d_gda_settings['exclusive_songs'] = FALSE:%s" % str(png)
            rc=True
        return rc
    def getsortedsongcount(self):
        return len(self.sortedsonglist)
    
    def getGDAsongcount(self):
        if self.musiclist:
            return len(self.musiclist)
        return -1
    ################################################
    #
    #
    #
    ################################################          
    def getFirstSongItem(self):
        if self.sortedsonglist and len(self.sortedsonglist)>0:
            return self.sortedsonglist[0]
        return None
    ################################################
    #
    #
    #
    ################################################      
    def getLastSongItem(self):
        if self.sortedsonglist and len(self.sortedsonglist)>0:
            return self.sortedsonglist[len(self.sortedsonglist)-1]
        return None
    ################################################
    #
    #
    #
    ################################################       
    def load_json(self,jpath):
        mj = None
        if os.path.exists(jpath):
            with open(jpath, 'r') as f:
                mj = json.load(f)
            if mj:
                return mj['musiclist']
        else:
            print "Error: invalid path=%s" % jpath
        return None
    ################################################
    #
    #
    #
    ################################################ 
    def evalplatform(self):
        self.platform_system = platform.system()  # Darwin = Mac
        self.platform_release = platform.release()
        print self.platform_system
        print self.platform_release
        #self.home = expanduser("~")
        self.musiclist = []
        self.isWin = False
        self.isMac = False
        if Env.isWindows():
            print "Windows"
            #self.automation_root = "%s\\workspace\\" % self.home
            self.automation_root = "C:\\Automation\\gopro-tests-desktop\\GDA\\Music_Tests\\"
            self.isWin = True
        elif Env.isMac():
            print "Mac"
            self.automation_root = "/Automation/gopro-tests-desktop/GDA/Music_Tests/"
            #self.automation_root = "%s/workspace/" % self.home
            self.isMac = True
    ################################################
    #
    #
    #
    ################################################             
    def validatesonglists(self):
        for song1 in self.sortedsonglist:
            mj=self.findsong(song1)
            if not mj:
                self.missingsongs.apprend(song1)
        for mj in self.musiclist:
            if mj:
                png = mj['pngsong_name']
                if png not in self.sortedsonglist:
                    self.newsongs.append(png)
        report = ""
        if len(self.missingsongs)>0:
            report += "-------------------------"
            report += "MISSING SONG LIST\n"
            for song1 in self.missingsongs:
                report += "MISSING: %s\n" % song1
            report += "-------------------------"
        if len(self.newsongs)>0:
            report += "-------------------------"
            report += "NEW SONG LIST\n"
            for song1 in self.newsongs:
                report += "NEW: %s\n" % song1
            report += "-------------------------"
            
        if len(report)==0:
            report += "SONG LIST VALIDATED OK: FOUND %d SONGS" % len(self.sortedsonglist)
            print report
            return None
        return report

    def songreport(self):
        self.reset()
        report=[]
        print "====================================="
        print "SONG LIST"
        print "png\t\ttitle\t\t15s\t30s\t60s"
        for i in range(0,self.getmusiccount()):
            d={}
            title, png, t15, t30, t60=self.getsortednextsong()
            row="%s\t\t%s\t\t%d\t%d\t%d" % (png,title,t15,t30,t60)
            d['png']=png
            d['title']=title
            d['t15']=t15
            d['t30']=t30
            d['t60']=t60
            if self.currentsong and 'tracks' in self.currentsong:
                d['tracks']=self.currentsong['tracks']
            report.append(d)
            print row        
            print "====================================="
        
        self.reset()
        return report
    ################################################
    #
    #
    #
    ################################################                 
    def reset(self):
        self.song_index = -1
    ################################################
    #
    #
    #
    ################################################ 
    def getmusiccount(self):
        if not self.musiclist or len(self.musiclist)==0:
            print "Error: music list is not loaded"
            return None

        return len(self.musiclist)
    ################################################
    #
    #
    #
    ################################################ 
    def getsortednext(self):
        self.song_index += 1
        if not self.sortedsonglist:
            print "Done: No song list"
            return None
            
        if self.song_index >= len(self.sortedsonglist):
            print "Done: end of song list"
            return None
        
        pngsong = self.sortedsonglist[self.song_index]
        if not pngsong or len(pngsong)==0:
            print "Error: sorted song item name is empty"
            return None
        songitem = self.findsong(pngsong)
        if not songitem:
            print "Error: song data not found %s" & pngsong
            return None
        print "============================================================================="
        n=len(self.sortedsonglist)
        print ">>> Song %i of %i %s <<<" % (self.song_index, n, pngsong)    
        return songitem

    ################################################
    #
    #
    #
    ################################################     
    def getnext(self,songindex = -1):
        if not self.musiclist or len(self.musiclist)==0:
            print "Error: music list is not loaded"
            return None
        if songindex>=0:
            self.song_index = songindex
        else:
            self.song_index += 1

        if self.song_index >=0 and self.song_index < len(self.musiclist):
            return self.musiclist[self.song_index]
        else:
            print "Error: music index exceeds music list"
            return None
    ################################################
    #
    #
    #
    ################################################ 
    def findsong(self, pngsongname):
        for songitem in self.musiclist:
            if pngsongname == songitem['pngsong_name']:
                return songitem
        return None
    ################################################
    #
    #
    #
    ################################################     
    def gettracks(self,tracks):
        if not tracks:
            return None, None, None
        t15=0
        t30=0
        t60=0
        if len(tracks) == 3:
            t0 = len(tracks[0]['marks'])
            t1 = len(tracks[1]['marks'])
            t2 = len(tracks[2]['marks'])
            if t0<t1<t2:
                t15=t0
                t30=t1
                t60=t2
            elif t2<t1<t0:
                t15=t2
                t30=t1
                t60=t0
            elif t0<t2<t1:
                t15=t0
                t30=t2
                t60=t1
            elif t2<t0<t1:
                t15=t2
                t30=t0
                t60=t1
            elif t1<t0<t2: # t15-t0=13,t30-t1=6,t60-t2=19
                t15=t1
                t30=t0
                t60=t2
            elif t0<t1<=t2: # t15-t0=5,t30-t1=15,t60-t2=15 MAKINGFYRE
                t15=t0
                t30=t1
                t60=t2
            else:
                print "Error: Order t15-t0=%d,t30-t1=%d,t60-t2=%d" % (t0,t1,t2)
                return None, None, None
                
            return t15, t30, t60
        print "Error: invalid number of tracks=%d" % len(tracks)
        return None, None, None
    ################################################
    # get specfic song info by song png name
    #
    #
    ################################################ 
    def getsonginfo(self,songpngname):
        for songinfo in self.musiclist:
            if self.ispngsong(songpngname,songinfo):
                return self.getsonginfo(songinfo)
        return None, None, None, None, None
    ################################################
    # quick match for pngsong name
    #
    #
    ################################################ 
    def ispngsong(self,pngsongname,songdata):       
        if songdata and ('pngsong_name' in songdata) and (songdata['pngsong_name']==pngsongname):
            return True
        return False

    ################################################
    # 
    #
    #
    ################################################ 
    def getsonginfo(self,songdata):
        if not songdata:
            return None, None, None, None, None
        
        if 'pngsong_name' in songdata:
            png = songdata['pngsong_name']
            title=None
            if 'music_title' in songdata and 'en' in songdata['music_title']:
                title = str(songdata['music_title']['en'])
            t15, t30, t60 = self.gettracks(songdata['tracks'])
            self.currentsong=songdata
            return str(title), str(png), t15, t30, t60
        else:
            print "Error: png not found >>%s<<" % str(songdata)
            return None, None, None, None, None
    ################################################
    # fast troubleshooting not retry problem songs   
    #
    #
    ################################################ 
    def isskipped(self,png):
        if self.skipsongslist and len(self.skipsongslist)>0:
            if png in self.skipsongslist:
                return True
        return False

    ################################################
    # Checks if song has been tested from the testrail run
    #
    # return False if no testrail or testrail has testcase status_id as not "passed"
    # returns True if testrail testcase status is set as passed
    # True the png is skipped
    # False the png is tested NOT skipped
    ################################################     
    def istestrail(self,png):
        tr=gda_utils.get_testrail_object()
        if not tr:
            return False
        name=png.replace(".png","").replace("song_","")
        s="%s - Select Song" % name
        for test in tr.testcases:
            if test["title"]==name:
                #get the latest test status
                t=tr.gettest(test["id"])
                if t:
                    if t["status_id"]==1: #passed
                        print "Testrail: Skipping %s" % name
                        return True
                    else:
                        print "Testrail: Test %s" % name
                        return False
                
        print "Test case not found in testrun: %s" % name
        return False
            
    ################################################
    #
    #
    #
    ################################################     
    def getsortednextsong(self):
        songdata = self.getsortednext()
        if songdata:
            title,png,t15,t30,t60=self.getsonginfo(songdata)
            if self.isskipped(png): #skip song and get the next song
                title,png,t15,t30,t60=self.getsortednextsong()
            if self.istestrail(png):
                title,png,t15,t30,t60=self.getsortednextsong()
            
            return title,png,t15,t30,t60
        print "FAILED in gda_music_tests GDA_songs.getsortednext()"
        return None, None, 0, 0, 0 

    ################################################
    #
    #
    #
    ################################################         
    def getnextsong(self):
        mj = self.getnext()
        if not mj:
            return None, None, None, None, None
        png = mj['pngsong_name']
        title = str(mj['music_title']['en'])
        t15, t30, t60 = self.gettracks(mj['tracks'])
        return str(title), str(png), t15, t30, t60
    ################################################
    #
    #
    #
    ################################################ 
    def gettext(self,png):
        mpng = None
        t = "NO_TXT"
        p = "NO_PNG"
        try:
            mpng = Finder(png)
            if mpng:
                mpng.find(png)
                if mpng.hasNext():
                    m = mpng.next()
                    if m:
                        return "PNG_OK"
                        #OCR does not work
                        #perhaps try the external teseract ocr on the terminal works much better
#                        t=str(m.text())
#                        if len(t)>0:
#                            return t
#                        return "NO_TXT"
        except:
            return p
        return p
    ################################################
    #
    #
    #
    ################################################     
    def testclass(self):
        mcount = 0
        title = object
        while title:
            mcount += 1
            title, png, t15, t30, t60 = self.getnextsong()
            if not title:
                print "Done"
                return
            
            t = self.gettext(png)

            p = "%d. %s|%s|%d|%d|%d|%s" % (mcount, title, png,t15,t30,t60,t)
            p = p.replace('\n','')
            print p
###########################################################
# END CLASS ###############################################
###########################################################

################################################
# compare current region with previous screenshot
# W x H of screenshot must be >= to the region or else fail
#
################################################
def comparescreens(REGION,screenshotpath):
    f=Finder(screenshotpath)
    #r=REGION.grow(-10)
    #wait(3)
    p=gda_utils.getPattern(capture(REGION),0.98)
    try:
        if f.find(p): #is region in screenshot
            return True
        else:
            return False
    except: #not found
        return False
    
################################################
#
#
#
################################################
def addtovideo(REGION):
    rc = False
#    rx=REGION.getX()+(REGION.getW()/2)-200
#    ry=REGION.getY()+REGION.getH()-60
#    rw=400
#    rh=70
#    r=Region(rx,ry,rw,rh)
    if gda_utils.CLICK3("MUSIC","BOTTOM",Pattern("music_btn_addtovideo.png").similar(0.69),5):
        rc=True
    return rc
    
################################################
#
#
# fails if not found,
################################################
def back(REGION):
    if ismusic_screen(REGION):
        rc = False
        #rx=REGION.getX()+(REGION.getW()/2)-200
        #ry=REGION.getY()+REGION.getH()-60
        #rw=400
        #rh=70
        #r=Region(rx,ry,rw,rh)
        if gda_utils.CLICK3("MUSIC","BOTTOM",Pattern("music_btn_back.png").similar(0.69),5):
            rc=True
        return rc
    else: #not at music screen
        return True
        
    
################################################
# Try to reset the music screen to show all music
# returns true is at music scren or false not
# call back to get out of music screen
################################################
def ismusic_screen(REGION):
    #narrow the search region for more accuracy
    #rx=REGION.getX()
    #ry=REGION.getY()    
    #rw=400
   # rh=100
    #r=Region(rx,ry,rw,rh)
    #r.highlight(1)    
    m=gda_utils.EXISTS3("MUSIC","TITLE",Pattern("music_btn_musiclist.png").similar(0.80),5) #music_btn_musiclist
    if m:
        return True # is at music list view
    m=gda_utils.EXISTS3("MUSIC","TITLE",Pattern("music_btn_history-selected.png").similar(0.80),5) #music_btn_musiclist
    if m:
        m=gda_utils.EXISTS3("MUSIC","TITLE",Pattern("music_btn_music-unselected.png").similar(0.80),5) #music_btn_musiclist
        if m:
            m.click()
            return True
    
    m=gda_utils.EXISTS3("MUSIC","TITLE",Pattern("music_btn_ALL.png").similar(0.80).targetOffset(-15,0),5) #music_btn_musiclist
    if m:
        m.click()
        return True
    return False        
################################################
#
#
#
################################################
def scrollfind(REGION,searchpattern):  
    lastcapture = None
    restart=0
    lm = None
    rc = False
    checklastsong = 0
    
    #while not REGION.exists(searchpattern):
    while not gda_utils.FIND(REGION,searchpattern,1,60,True):
        print "SEARCHPATTERN=%s" % str(searchpattern)
        #REGION.highlight(1)
        #wait(1)
        #lastcapture = capture(REGION)
        rc = doscroll(REGION)
        
        #REGION.highlight(1)
        if rc: # if scroll happened
            checklastsong += 1
            if checklastsong>4:
                checklastsong = 0
                #REGION.highlight(1)
                if REGION.exists(gda_utils.getPattern(gda_utils.d_gda_settings["LAST_SONG"],0.85)):
                    resetsonglist(REGION,gda_utils.d_gda_settings["FIRST_SONG"])
                #if comparescreens(REGION,lastcapture):
                    #REGION.highlight(8)
                    if restart>2:
                        print "FAILED to find song after 1 retry in song list"
                        print "test is aborting"
                        return None
                    #resetsonglist(REGION,gda_utils.d_gda_settings["FIRST_SONG"])
                    restart +=1

    lm = REGION.getLastMatch()
    #lm.highlight(1)
    #lastitem = lm
    return lm

################################################
#
#
#
################################################    
def doscroll(REGION):
    #global lastitem
    print "doscroll >>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    p=None
    try:
        foundlist =[]
        #p=gda_utils.d_gda_settings["MUSIC_LIST_ITEM_UNSELECTED"]
        p = gda_utils.d_gda_settings["MUSIC_LIST_ITEM_UNSELECTED"]
        print "findALL: %s" % p
        wait(2)
        
        mm = REGION.findAll(p)
        while mm.hasNext():
            item = mm.next()
            if item:
                print str(item)
                foundlist.append(item)
                #item.highlight(1)
        y=0
        wait(10)
        for i in range(0,len(foundlist)):
            t=foundlist[i]
            print str(t)
            #t.highlight(1)
            if t.getY()>y:
                y=t.getY()
                item=t
            print "%d - %s" % (y,str(item))
        #last=len(foundlist)
        #item=itemlist[0]
        item.highlight(1)
        item.doubleClick()
        #item.mouseDown(1)
        wait(1)
        #item,click()
        #item.mouseUp(1)
        dotyperepeat(item,Key.DOWN,7)
        return True
    except Exception as e:
        print "ERROR: doscroll items not found"
        print "PATTERN=%s" % str(p)
        print "ERROR=%s" % str(e)
    print "doscroll <<<!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    return False
################################################
#
#
#
################################################ 
def dotyperepeat(region,key,count):
    if region:
        try:
            for i in range(1,count,1):
                region.type(key)
                wait(0.5)
        except:
            print "dotyperepeat:type key error"
    else:
        print "dotyperepeat:invalid region error"


lastitem = None
lastpattern = None


################################################
#
#
#
################################################
def EXISTS(REGION,PATTERN,MATCH=None,do_play=True):
    global lastitem
    global lastpattern
    wait(1)
    m=MATCH
    #if REGION.exists(PATTERN):
    if not m:
        #if gda_utils.FIND(REGION,PATTERN,1,70,True):
        r = Region(REGION.getX(),(REGION.getY()+50),(REGION.getW()-800),(REGION.getH()-50))
        #r.highlight(1)
        if r.exists(PATTERN):
            m = r.getLastMatch()
        else:
            m = scrollfind(r,PATTERN)
    if m:    
        lastitem = m
        lastpattern = PATTERN
        print "FOUND: %s - %s" % (PATTERN.getFilename(),str(("%.2f" % m.getScore())))
        m.click()
        if r.exists(PATTERN):
            m=r.getLastMatch()
            
            m.highlight(1)
            m.click()  
            if do_play:
                wait(1)            
                try:
                    m1=m.right(300)
                    m1=m1.grow(1,30)
                    m.click()
                    #m.highlight(1)
                    m1.click(Pattern("music_btn_play-selected.png").similar(0.69))
                    return True
                except:
                    print "Play button not found"
                    m.click()
                    m.type(Key.DOWN)
            else:
                return True
        
    else:
        return False
        print "++NOT FOUND: %s" % PATTERN.getFilename()
        m = scrollfind(REGION, PATTERN)
        if m:
            return EXISTS(REGION,PATTERN,m)
        else:
            return False
        if lastitem:

            #if REGION.exists(lastpattern):
            if gda_utils.FIND(REGION,lastpattern,1,70,True):
                m=REGION.getLastMatch()
                if m:
                    print "SCROLL:if REGION.exists(lastpattern):"

                    try:
                        m.click()
                    except:
                        print "Error:m.click()"
                    dotyperepeat(m,Key.DOWN,6)
                    m.click()
                    return EXISTS(REGION,PATTERN)
            else:
                print "SCROLL:else:"
                dotyperepeat(lastpattern,Key.DOWN,5)
                try:
                    lastpattern.click()
                except:
                    print "End of song list: %s" % PATTERN.getFilename()
                    return False
                return EXISTS(REGION,PATTERN)
    return False

################################################
#
#
#
################################################                
def resetsonglist(REGION,PATTERN):
    print "resetsonglist >>>"
    #global lastitem
    #global lastpattern    
    #if REGION.exists(PATTERN):
    if gda_utils.FIND(REGION,PATTERN):
        item=REGION.getLastMatch()    
        if item:
            item.doubleClick()
            wait(1)
            item.type(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"],Key.UP)
            item.type(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"],Key.UP)
            item.type(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"],Key.UP)
    print "resetsonglist <<<"          
################################################
# this is obsolete
#
#
################################################
def getsongbeatsregion(region):
    print "getsongbeatsregion>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    beatsr = None
    #if not region.exists(Pattern("music_btn_addtovideo.png").similar(0.98)): #  music_btn_addtovideo
    if not gda_utils.FIND(region,Pattern("music_btn_addtovideo.png").similar(0.69)):
        print "ERROR get song beats region: music_btn_addtovideo not found"
        print "getsongbeatsregion<<<<<<<<<<<<<<<<<<<<<<"
        return None
    m=region.getLastMatch()
    #m.highlight(1)
    m1=m.above(153)
    #m1.highlight(1)
    m2=m1.left(280)
    #m2.highlight(1)

    if m2 and gda_utils.FIND(m2,Pattern("editor_img.00timescale.png").similar(0.98)):
        m3=m2.getLastMatch()
        #m3.highlight(1)
        rx=m3.getX()
        ry=m2.getY()
        rw=(region.getW()-(rx-region.getX()))
        rh=m2.getH()-42
        #print "gda=%s" % str(region)
        #print "add=%s" % str(m)
        #print "above150=%s" % str(m1)
        #print "left400=%s" % str(m2)
        #print "00scale=%s" % str(m3)
        #print "%d,%d,%d,%d" % (rx,ry,rw,rh)
        beatsr=Region(rx,ry,rw,rh)
        #beatsr.highlight(1)
    else:
        print "ERROR get song beats region: time count zero >:00< not found to create beats region" 
    print "getsongbeatsregion<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    return beatsr

################################################
#
#
#
################################################
def getbeatsfilename(png,duration,beatsdir):
    rc= False
    newname = "_musicbeats_%d.png" % duration
    beats = png.replace(".png",newname)
    imgpath = os.path.join(beatsdir, beats)
    if os.path.isfile(imgpath):
        rc = True
    return rc,imgpath

################################################
#
#
#
################################################
def savebeatsscreenshot(region,imgpath):
    rc = False
    print "savebeatsscreenshot >>>>>>>>>>>>>>>>"
    found = False

    beatsr = getsongbeatsregion(region)
    if not beatsr:
        print "FAILED savebeatsscreenshot region not found"
        print "savebeatsscreenshot <<<<<<<<<<<<<<<<<"
        return False
    #newname = "_musicbeats_%d.png" % duration
    #beats = png.replace(".png",newname)
    beatsr.highlight(1)
    #wait(2)

    #imagepath=ImagePath.getBundlePath()
    #imagepath=imgdir
    fpath = capture(beatsr)
    print "%s >>> MOVE >>> %s" % (fpath,imgpath)
    #imgpath = os.path.join(imagepath, beats)        
    shutil.move(fpath, imgpath)
    wait(5.0)
    if os.path.isfile(imgpath):
        print "SAVED: %s" % imgpath
        rc = True
    else:
        print "FAILED file not found: %s" % imgpath
    print "savebeatsscreenshot <<<<<<<<<<<<<<<<<"
    return rc
    
################################################
#
#
#
################################################
def verifybeatsscreenshot(region,imgpath):
    rc = False
    print "verifybeatsscreenshot >>>>>>>>>>>>>>>>"
    found = False

    beatsr = getsongbeatsregion(region)
    if not beatsr:
        print "FAILED verifybeatsscreenshot region not found"
        print "verifybeatsscreenshot <<<<<<<<<<<<<<<<<"
        return False
    #newname = "_musicbeats_%d.png" % duration
    #beats = png.replace(".png",newname)
    beatsr.highlight(1)
    
    ftest=capture(beatsr)

    f=Finder(imgpath)
    p = gda_utils.getPattern(ftest,0.95)
    print "PATTERN=%s" % str(p)    
    f.find(p)
    if f.hasNext():
        print "verifybeatsscreenshot FOUND<<<<<<<<<<<<<<<<<"
        return True
    print "verifybeatsscreenshot FAIL<<<<<<<<<<<<<<<<<"
    return False

################################################
#
#
#
################################################
def resetscrolltotop(region):
    #if region.exists(gda_utils.d_gda_settings["MUSIC_LIST_ITEM_UNSELECTED"]): # music_img_unselected
    if gda_utils.FIND(region,gda_utils.d_gda_settings["MUSIC_LIST_ITEM_UNSELECTED"]):
        m = region.getLastMatch()
        if m:
            m.click()
            m.keyDown(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"])
            m.type(Key.UP)
            m.keyUp(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"])
            wait(1)
            #if region.exists(Pattern("song_THENIGHTWEDANCED.png").similar(0.98)): # music_img_unselected
            
            if gda_utils.FIND(region,gda_utils.d_gda_settings["FIRST_SONG"]):
                return True
        else:
            print "ERROR resetscrolltotop: music_img_unselected.png not found"
    else:
        print "ERROR resetscrolltotop: music_img_unselected.png not found"
    return False

################################################
#
#
#
################################################
def eval_duration(testduration,t15,t30,t60):
    if testduration == 15:
        return t15
    elif testduration == 30:
        return t30
    elif testduration == 60:
        return t60

################################################
#
#
#
################################################
def testmusic_init(gda_music):
    fsong = gda_utils.getPattern(gda_music.getFirstSongItem(),0.69)
    gda_utils.d_gda_settings["FIRST_SONG"]=fsong
    gda_utils.d_gda_settings["MUSIC_LIST_ITEMS_LOCKED"]=False #select plus account music
    print "FIRST_SONG=%s" % str(gda_utils.d_gda_settings["FIRST_SONG"])
    lsong = gda_utils.getPattern(gda_music.getLastSongItem(),0.69)
    gda_utils.d_gda_settings["LAST_SONG"]=lsong
    print "LAST_SONG=%s" % str(gda_utils.d_gda_settings["LAST_SONG"])
    gda_utils.d_gda_settings["MUSIC_LIST_ITEM_UNSELECTED"] = Pattern("music_img_unselected.png").similar(0.69) #music_img_unselected
    gda_utils.d_gda_settings["MUSIC_LIST_ITEM_LOCKED_UNSELECTED"] = Pattern("music_img_locked-unselected.png").similar(0.68)  #gda_utils.d_gda_settings["MUSIC_LIST_ITEMS_LOCKED"]=True
    print "MUSIC_LIST_ITEM_UNSELECTED=%s" % str(gda_utils.d_gda_settings["MUSIC_LIST_ITEM_UNSELECTED"])
################################################
#
#
#
################################################
#def selectsong(REGION,png,do_play=True):
#    if EXISTS(REGION,Pattern(png).similar(0.80)):
################################################
#
#
#
################################################        
def setnextsong(REGION,png):
    rc=False
    rx=REGION.getX()+20
    ry=REGION.getY()+30
    rw=200
    rh=100
    r1=Region(rx,ry,rw,rh)
    r1.highlight(1)
    if gda_utils.FIND(r1,Pattern("music_btn_music-selected.png").similar(0.71)):
        if png:
            if EXISTS(REGION,Pattern(png).similar(0.69)):
                wait(5)
                addtovideo(REGION)
                return True
    return rc
                

    
################################################
# Music selection and beats chart preview screen.
# Iterate all songs from GDA_music.sortedsonglist
# Assumes the proper duration is set in view screen
# regression flag true validates and false records 
# new song beats charts
# Auto finds in record mode the last song and continues
# validates the song list, new, removed songs and sort order.
# sets song list scroll to top and detects the last 
# song based on the sorted list
################################################
def testsongs(ap,r,duration,regression=True,testmode="music"):
    failed=[]
    passed=[]
    if not r:
        r=getGDARegion()
        if not r:
            print "Error: Invalid region"
            return
    set_MUSIC_SCREEN_regions(r)
    gda_utils.failexit=10
    msongs = GDA_music()
    if not msongs:
        print "Failed testsongs: msongs = GDA_music()"
        return False
    testmusic_init(msongs)
    png=object
    counter = 0
    lastpng = None
    print str(r)
    if regression:
        resetscrolltotop(r)
    #getsongbeatsregion(r)
    #return
    imgdir = os.path.join(gda_utils.d_gda_settings["HOME"], "gda_music_images")
    loopstart=False
    while png:
        try:
            #if counter>10:
            #    break
            title, png, t15, t30, t60 = msongs.getsortednextsong()
            counter += 1
            
            if not png:
                print "%d. Song in list is not Found" % counter
                break
            lastpng = png
            
            found,imgpath = getbeatsfilename(png,duration,imgdir)
            # |-regression-|-png found-|--action-----|
            # |------------|-----------|-------------|
            # |   true     | true      | can verify  |
            # |   true     | false     |  skip       |
            # |   false    | true      |  skip       |
            # |   false    | false     |do screenshot|
            
            if not found: #or loopstart:
                print "============================================================================="
                print "%d. TEST: 15s=%d 30s=%d 60s=%d PNG:%s TITLE:%s" % (counter,t15,t30,t60, png, title)
                print "============================================================================="    
                
                #loopstart = False # find first item for scrolling
                if EXISTS(r,Pattern(png).similar(0.80)):
                    twait = eval_duration(duration,t15,t30,t60)
                
                    wait((duration+10))
                    if not regression:
                        if not savebeatsscreenshot(r,imgpath):
                            print "FAILED save beats screenshot:###########################################################################"
                            failed.append(imgpath)
                    else:
                        print "FAILED beats screenshot regression test:###########################################################################"
                        failed.append(imgpath)
                    #break
                else:
                    print "FAILED to find MUSIC title: %s ###########################################################################" % png
                    exit(1)
            else:
                if regression:
                    print "============================================================================="
                    print "%d. REGRESSION TEST: 15s=%d 30s=%d 60s=%d PNG:%s TITLE:%s" % (counter,t15,t30,t60, png, title)
                    print "============================================================================="
                    if EXISTS(r,Pattern(png).similar(0.80)):
                        twait = eval_duration(duration,t15,t30,t60)
                        wait((duration+10))
                        if not verifybeatsscreenshot(r,imgpath):
                            failed.append(imgpath)
                            print "TEST FAILED: %s" % imgpath
                            print "###########################################################################"
                        else:
                            passed.append(str(imgpath))
                            print "TEST PASSED: %s" % str(imgpath)
                            print "============================================================================="
                    else:
                        print "FAILED to find MUSIC title: %s ###########################################################################" % png
                        exit(1)                            
                else:
                    print "%d. SKIP TEST: 15s=%d 30s=%d 60s=%d PNG:%s TITLE:%s" % (counter,t15,t30,t60, png, title)
        except Exception as e:
            print "testsongs #################################################################"
            print "FAILED: At png %s>>%s" % (lastpng,png)
            print "ERROR: %s" % str(e)
            print "testsongs #################################################################"
            exit(1)
        
    resetscrolltotop(r)

################################################
#
#
#
################################################         
def getGDARegion():
    ap=switchApp("Quik")
    if not ap:
        print "Error: APP"
        return None,None
    r = ap.focusedWindow()
    if not r:
        print "Error: Window"
        return None,ap
    r.highlight(2)
    return r,ap

################################################
#
#
#
################################################ 
def getunselectedsongicon():
    r=gda_utils.getregion("MUSIC","MUSICLIST")
    if not r:
        print "ERROR: MUSIC-MUSICLIST region not found"
        return None
    
    icon=gda_utils.d_gda_settings["MUSIC_LIST_ITEM_UNSELECTED"]
    if gda_utils.d_gda_settings["MUSIC_LIST_ITEMS_LOCKED"]==True:
        icon=gda_utils.d_gda_settings["MUSIC_LIST_ITEM_LOCKED_UNSELECTED"]
    return gda_utils.EXISTS2(r,icon ,5)
################################################
#
#
#
################################################ 
def getsongitemregion(songMATCH):
    rx=songMATCH.getX()-55
    ry=songMATCH.getY()-10
    rw=410
    rh=50
    r=Region(rx,ry,rw,rh)
    return r

################################################
#
#
#
################################################ 
def goto_top_songlist():
    m2=getunselectedsongicon()
    if not m2:
        return False
    wait(1)
    m2.doubleClick()
    wait(0.5)
    m2.keyDown(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"])
    wait(0.5)
    m2.type(Key.UP)
    m2.keyUp(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"])
    wait(1)
    m2.keyDown(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"])
    wait(0.5)
    m2.type(Key.UP)
    m2.keyUp(gda_utils.d_gda_settings["PLATFORM_KEY_CTRL"])
    wait(1)
    m2=gda_utils.EXISTS3("MUSIC","MUSICLIST",gda_utils.d_gda_settings["FIRST_SONG"],5)
    if m2:
        return True
    return False

###########################################
# finds the song item region, plays song, adds to video
# GUI goes back to CREATE screen
###########################################
def selectsong_addtovideo(REGION,png,retrycount=0, playsong=1,song_similarity=0.59):
    rc=False
    print "selectsong_addtovideo >>>>> %s" % png
    if gda_utils.d_gda_settings["isMac"]=="True":
        song_similarity=0.80
    elif gda_utils.d_gda_settings["isWindows"]=="True":
        song_similarity=0.52 #asus vivo
    p=gda_utils.PATTERN(png,song_similarity)
    songitem=findsongregion(p) #return the song title song item region
    
    if not songitem:
        print "FAILED: song %s is not found in list." % png
        print "return back to CREATE screen"
        mback=gda_utils.EXISTS3("MUSIC","BOTTOM",Pattern("music_btn_back.png").similar(0.69))
        if mback:
            mback.click()
            print "selectsong_addtovideo: song region NOT FOUND <<<<<"
            return rc
    print "song region found"
    songitem.highlight(1)
    wait(1)
    #songitem.mouseMove(p)
    #wait(2)
    #we need the song region to highlight to show blue play button
    #songitem.highlight(2)
    if gda_utils.CLICK2(songitem,Pattern("music_btn_play-selected.png").similar(0.50),10,True):
        r=gda_utils.getregion("MUSIC","BOTTOM")
        #r.highlight(1)
        wait(playsong)
        r.click(Pattern("music_btn_addtovideo.png").similar(0.69))
        print "selectsong_addtovideo: OK <<<<<"
        rc=True
#        else:
#            print "selectsong_addtovideo: ADD TO VIDEO button NOT FOUND <<<<<"
#        if r and gda_utils.CLICK2(r,Pattern("music_btn_addtovideo.png").similar(0.69).targetOffset(1,1),5):
#            print "selectsong_addtovideo: OK <<<<<"
#            rc=True
#        else:
#            print "selectsong_addtovideo: ADD TO VIDEO button NOT FOUND <<<<<"
    else: # no play button found, have song region but no play must be partial covered
        songitem.click()
        songitem.type(Key.DOWN)
        wait(1)
#        songitem=findsongregion(p)
#        if gda_utils.CLICK2(songitem,Pattern("music_btn_play-unselected.png").similar(0.69),10,True):#try non selected
#            r=gda_utils.getregion("MUSIC","BOTTOM")
            #r.highlight(1)
#            r.click(Pattern("music_btn_addtovideo.png").similar(0.69))
#            print "selectsong_addtovideo: OK <<<<<"
#            rc=True
#        else:
        print "selectsong_addtovideo: song region PLAY icon button NOT FOUND <<<<<"
        retrycount += 1
        if retrycount>3:
            return False
            #songitem.click()
            #songitem.type(Key.DOWN)
            #songitem.type(Key.DOWN)
            #songitem.type(Key.DOWN)
            # need new song region after scroll
        return selectsong_addtovideo(REGION,png,retrycount)
    return rc
################################################
# with songPATTERN will find through the song list
# auto detects the last song and reset to top and continues searching
# will exit after 1 full iteration
# starts at current song list position
################################################     
def findsongregion(songPATTERN,endcount=0,loopcount=0,count=0):
    count+=1
    print "%d findsongregion >>>>" % count
    rsonglist=gda_utils.getregion("MUSIC","MUSICLIST")
    
    if not rsonglist:
        print "ERROR: MUSIC-MUSICLIST region not found"
        print "%d findsongregion <<<<" % count
        return None
    #r.highlight(1)
    m1=gda_utils.EXISTS2(rsonglist,songPATTERN,5)
    if m1: # song is visible in list
        wait(1)
        m1.click()
        wait(1)
        m1.click()
#        m1.type(Key.DOWN)#assume at bottom of list should bump up 1 so the whole region can show with the play button
#        wait(1)
        m1=gda_utils.EXISTS2(rsonglist,songPATTERN,5)
        if m1:
            m2=getsongitemregion(m1)
            if m2:
                #m2.highlight(1)
                print "%d findsongregion <<<<" % count
                return m2
            else:
                m1.click()
                m1.type(Key.DOWN)
                return findsongregion(songPATTERN,endcount,loopcount,count)
        else:
            return findsongregion(songPATTERN,endcount,loopcount,count)

    else: # do scroll and check if at end of list then repeat from top
        if loopcount>1:
            print "ERROR: failed to find song item after 1 full iteration"
            print "%d findsongregion <<<<" % count
            return None
        m2=getunselectedsongicon()       
        if m2:
            m2.click()
            m2.type(Key.DOWN)
            m2.type(Key.DOWN)
            m2.type(Key.DOWN)
            m2.type(Key.DOWN)
            m2.type(Key.DOWN)
            m2.type(Key.DOWN)
            m1=gda_utils.EXISTS2(rsonglist,gda_utils.d_gda_settings["LAST_SONG"],5)
            if m1:
                endcount+=1
                if endcount>1:
                    if not goto_top_songlist():
                        print "ERROR: failed to reset to top of song list. stuck at end of list"
                        print "%d findsongregion <<<<" % count
                        return None
                    loopcount+=1
                    endcount=0
            return findsongregion(songPATTERN,endcount,loopcount,count)
        else:
            print "ERROR: failed to find unselected song item"
            print "%d findsongregion <<<<" % count
            return None            

        
######################################
# Assumes automation window size Mac{x35,y35,w1280, h836}
# for windows using Autoit we need to identify the inner region w,h relative to mac and set the win size accordingly
# Win,Mac window container border widths are different
# this is global region list for more accurate image query
######################################
def set_MUSIC_SCREEN_regions(REGION):
    print "==============================="
    print "IMAGE PATHS"
    imgPath = getImagePath() # get the list
    # to loop through
    for p in imgPath:
        print p
    print "==============================="
    if gda_utils.d_gda_settings["isWindows"]=="True":
        set_MUSIC_SCREEN_Win_regions(REGION)
        return True
    elif gda_utils.d_gda_settings["isMac"]=="True":
        set_MUSIC_SCREEN_Mac_regions(REGION)
        return True
    else:
        print "ERROR: Invalid platform not Mac or Win"
    return False

################################################
#
#
#
################################################
def set_MUSIC_SCREEN_Win_regions(REGION):    
    screenregion="MUSIC"
    subregion="MUSICLIST"
    rx=REGION.getX()
    ry=REGION.getY()+168
    rw=470
    rh=640
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    subregion="TITLE"
    rx=REGION.getX()+ 5
    ry=REGION.getY()+110
    rw=460
    rh=60
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    subregion="BOTTOM"
    rx=REGION.getX()+8
    ry=REGION.getY()+REGION.getH()-60
    rw=REGION.getW()-8
    rh=60
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    subregion="TOP"
    rx=REGION.getX()
    ry=REGION.getY()+48#+REGION.getH()-80
    rw=REGION.getW()
    rh=60
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    #return
    subregion="PLAYER"
    rx=REGION.getX()+470
    ry=REGION.getY()+120
    rw=REGION.getW()-480
    rh=REGION.getH()-330
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)

    subregion="BEATS"
    rx=REGION.getX()+480
    ry=REGION.getY()+REGION.getH()-180
    rw=REGION.getW()-510
    rh=60    
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    
    subregion="MENU"
    rx=REGION.getX()+5
    ry=REGION.getY()+30
    rw=300
    rh=16    
    r=Region(rx,ry,rw,rh)
    #r.highlight(10)
    gda_utils.add_region(screenregion,subregion,r)
    
################################################
#
#
#
################################################    
def set_MUSIC_SCREEN_Mac_regions(REGION):
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
    screenregion="MUSIC"
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
    subregion="TITTLE"
    rx=REGION.getX()
    ry=REGION.getY() + 69 + 22 #relative from top
    rw=642
    rh=52
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)
    
    #--------------------------------------------
    subregion="MUSICLIST"
    rx=REGION.getX()
    ry=REGION.getY() + 148 #relative from top
    rw=642
    rh=612
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)

    #--------------------------------------------
    subregion="PLAYER"
    rx=REGION.getX()+646
    ry=REGION.getY() + 106 #relative from top
    rw=620
    rh=398
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)

    #--------------------------------------------
    subregion="SELECTEDTITLE"
    rx=REGION.getX() + 644
    ry=REGION.getY() + REGION.getH() - 342 #relative from bottom
    rw=615
    rh=52
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)

    #--------------------------------------------
    subregion="BEATS"
    rx=REGION.getX() + 644
    ry=REGION.getY() + REGION.getH() - 288 #relative from bottom
    rw=630
    rh=208
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)

    #--------------------------------------------
    subregion="BOTTOM"
    rx=REGION.getX()
    ry=REGION.getY() + REGION.getH() - 77 #relative from bottom
    rw=1280
    rh=77
    r=Region(rx,ry,rw,rh)
    r.highlight(h1)
    gda_utils.add_region(screenregion,subregion,r)

################################################
#
#
#
################################################
def findsongs(ap,r):
    if not r:
        r,ap = getGDARegion()#this works only on mac, TODO: optimize for win
    if not r:
        print "Error: Invalid region"
        return
    
    EXISTS(r,Pattern("song_THENIGHTWEDANCED.png").similar(0.98)) #song_THENIGHTWEDANCED
    EXISTS(r,Pattern("song_AFTERGLOW.png").similar(0.98)) # song_AFTERGLOW
    EXISTS(r,Pattern("song_BRINGIT.png").similar(0.98)) # song_BRINGIT
    EXISTS(r,Pattern("song_COMETHRU.png").similar(0.98)) # song_COMETHRU
    EXISTS(r,Pattern("song_DAFTCRUNK.png").similar(0.98)) # song_DAFTCRUNK
    EXISTS(r,Pattern("song_FEELTHELOVE.png").similar(0.98)) # song_FEELTHELOVE
    EXISTS(r,Pattern("song_GUILTYMAN.png").similar(0.98)) # song_HIDEANDFREAK
    EXISTS(r,Pattern("song_HIDEANDFREAK.png").similar(0.98)) # song_HIDEANDFREAK  
    EXISTS(r,Pattern("song_RAINDOWN.png").similar(0.98)) # song_RAINDOWN
    EXISTS(r,Pattern("song_RISEUP.png").similar(0.98)) # song_RISEUP            
    EXISTS(r,Pattern("song_AWONDERFULSACRIFICE.png").similar(0.98)) # song_AWONDERFULSACRIFICE
    EXISTS(r,Pattern("song_AINTNOWAY.png").similar(0.98)) # song_AINTNOWAY
    EXISTS(r,Pattern("song_ALLIKNOW.png").similar(0.98)) # song_ALLIKNOW
    EXISTS(r,Pattern("song_AMAZEBALLS.png").similar(0.98)) # song_AMAZEBALLS
    EXISTS(r,Pattern("song_AMIGOS4LIFE.png").similar(0.98)) # song_AMIGOS4LIFE
    EXISTS(r,Pattern("song_BFF.png").similar(0.98)) # song_BFF
    EXISTS(r,Pattern("song_BIPOLAR.png").similar(0.98)) # song_BIPOLAR
    EXISTS(r,Pattern("song_BIGBOY.png").similar(0.98)) # song_BIGBOY
    EXISTS(r,Pattern("song_BITEME.png").similar(0.98)) # song_BITEME
    EXISTS(r,Pattern("song_BLAME.png").similar(0.98)) # song_BLAME
    EXISTS(r,Pattern("song_BLINDEDBYTHESUN.png").similar(0.98)) # song_BLINDEDBYTHESUN
    EXISTS(r,Pattern("song_BLOODFEUD.png").similar(0.98)) # song_BLOODFEUD
    EXISTS(r,Pattern("song_BRINGMEBACKTOLIFE.png").similar(0.98)) # song_BRINGMEBACKTOLIFE
    EXISTS(r,Pattern("song_BURYMYLOVE.png").similar(0.98)) # song_BURYMYLOVE
    EXISTS(r,Pattern("song_CARRYMEBACKHOME.png").similar(0.98)) # song_CARRYMEBACKHOME
    EXISTS(r,Pattern("song_CHOKINCHICKENS.png").similar(0.98)) # song_CHOKINCHICKENS
    EXISTS(r,Pattern("song_COLDFEET.png").similar(0.98)) # song_COLDFEET
    EXISTS(r,Pattern("song_COMBATREADY.png").similar(0.98)) # song_COMBATREADY
    EXISTS(r,Pattern("song_CRANKIT.png").similar(0.98)) # song_CRANKIT
    EXISTS(r,Pattern("song_DJBLOWUPTHESPEAKERS.png").similar(0.98)) # song_DJBLOWUPTHESPEAKERS
    EXISTS(r,Pattern("song_DARKFADER.png").similar(0.98)) # song_DARKFADER
    EXISTS(r,Pattern("song_DEADANDGONE.png").similar(0.98)) # song_DEADANDGONE
    EXISTS(r,Pattern("song_DOYOUFEELALIVE.png").similar(0.98)) # song_DOYOUFEELALIVE
    EXISTS(r,Pattern("song_DOPEDELUXE.png").similar(0.98)) # song_DOPEDELUXE
    EXISTS(r,Pattern("song_DROPPINDIMES.png").similar(0.98)) # song_DROPPINDIMES
    EXISTS(r,Pattern("song_EVERYTHING.png").similar(0.98)) # song_EVERYTHING
    EXISTS(r,Pattern("song_FEELSLIKEIMADEIT.png").similar(0.98)) # song_FEELSLIKEIMADEIT
    EXISTS(r,Pattern("song_FIFTEENWAYS.png").similar(0.98)) # song_FIFTEENWAYS
    EXISTS(r,Pattern("song_FRETCOLLECTOR.png").similar(0.98)) # song_FRETCOLLECTOR
    EXISTS(r,Pattern("song_GETTINGBUZZED.png").similar(0.98)) # song_GETTINGBUZZED
    EXISTS(r,Pattern("song_GLASSDARKLY.png").similar(0.98)) # song_GLASSDARKLY
    EXISTS(r,Pattern("song_GLOCKNROLL.png").similar(0.98)) # song_GLOCKNROLL
    EXISTS(r,Pattern("song_GODWILLCUTYOUDOWN.png").similar(0.98)) # song_GODWILLCUTYOUDOWN
    EXISTS(r,Pattern("song_GOOD4THAHOOD.png").similar(0.98)) # song_GOOD4THAHOOD
    EXISTS(r,Pattern("song_HALLOWEDGROUND.png").similar(0.98)) # song_HALLOWEDGROUND
    EXISTS(r,Pattern("song_HEAVYWEATHER.png").similar(0.98)) # song_HEAVYWEATHER
    EXISTS(r,Pattern("song_HEROESDRESSINBLACK.png").similar(0.98)) # song_HEROESDRESSINBLACK
    EXISTS(r,Pattern("song_HOLDYOURHEADUP.png").similar(0.98)) # song_HOLDYOURHEADUP
    EXISTS(r,Pattern("song_HUNDREDDOLLAGIRLZ.png").similar(0.98)) # song_HUNDREDDOLLAGIRLZ
    EXISTS(r,Pattern("song_IDAREYOU.png").similar(0.98)) # song_IDAREYOU
    EXISTS(r,Pattern("song_INAROW.png").similar(0.98)) # song_INAROW
    EXISTS(r,Pattern("song_INTHAMAISON.png").similar(0.98)) # song_INTHAMAISON
    EXISTS(r,Pattern("song_ITSOURS.png").similar(0.98)) # song_ITSOURS
    EXISTS(r,Pattern("song_JOYRIDE.png").similar(0.98)) # song_JOYRIDE
    EXISTS(r,Pattern("song_JUSTALITTLE.png").similar(0.98)) # song_JUSTALITTLE
    EXISTS(r,Pattern("song_KEEPTHEFAITHALIVE.png").similar(0.98)) # song_KEEPTHEFAITHALIVE
    EXISTS(r,Pattern("song_KILLINFLOOR.png").similar(0.98)) # song_KILLINFLOOR
    EXISTS(r,Pattern("song_KNUCKLEDRAGGER.png").similar(0.98)) # song_KNUCKLEDRAGGER
    EXISTS(r,Pattern("song_LIGHTEMUP.png").similar(0.98)) # song_LIGHTEMUP
    EXISTS(r,Pattern("song_MEADOWMIND.png").similar(0.98)) # song_MEADOWMIND
    EXISTS(r,Pattern("song_MOONSHINEANDGASOLINE.png").similar(0.98)) # song_MOONSHINEANDGASOLINE
    EXISTS(r,Pattern("song_NEWDAY.png").similar(0.98)) # song_NEWDAY
    EXISTS(r,Pattern("song_NOTLOOKINBACK.png").similar(0.98)) # song_NOTLOOKINBACK
    EXISTS(r,Pattern("song_NUCLEAR.png").similar(0.98)) # song_NUCLEAR
    EXISTS(r,Pattern("song_ONTHEDL.png").similar(0.98)) # song_ONTHEDL
    EXISTS(r,Pattern("song_ONEOFAKIND.png").similar(0.98)) # song_ONEOFAKIND
    EXISTS(r,Pattern("song_PALESAND.png").similar(0.98)) # song_PALESAND
    EXISTS(r,Pattern("song_PARTYWILLCOMEALIVE.png").similar(0.98)) # song_PARTYWILLCOMEALIVE
    EXISTS(r,Pattern("song_PUNCHING.png").similar(0.98)) # song_PUNCHING
    EXISTS(r,Pattern("song_PUSHUPTHEBEAT.png").similar(0.98)) # song_PUSHUPTHEBEAT
    EXISTS(r,Pattern("song_REASONS.png").similar(0.98)) # song_REASONS
    EXISTS(r,Pattern("song_ROCKYOURWORLD.png").similar(0.98)) # song_ROCKYOURWORLD
    EXISTS(r,Pattern("song_RUSHES.png").similar(0.98)) # song_RUSHES
    EXISTS(r,Pattern("song_SCREENDOORSLAM.png").similar(0.98)) # song_SCREENDOORSLAM
    EXISTS(r,Pattern("song_SHAKE.png").similar(0.98)) # song_SHAKE
    EXISTS(r,Pattern("song_SHAKEITOUT.png").similar(0.98)) # song_SHAKEITOUT
    EXISTS(r,Pattern("song_SMOKINFIRE.png").similar(0.98)) # song_SMOKINFIRE
    EXISTS(r,Pattern("song_SOUNDBOI.png").similar(0.98)) # song_SOUNDBOI
    EXISTS(r,Pattern("song_STRANGECONDITION.png").similar(0.98)) # song_STRANGECONDITION
    EXISTS(r,Pattern("song_STRINGOFTRUTH.png").similar(0.98)) # song_STRINGOFTRUTH
    EXISTS(r,Pattern("song_SUGARGIRL.png").similar(0.98)) # song_SUGARGIRL
    EXISTS(r,Pattern("song_SURGE.png").similar(0.98)) # song_SURGE
    EXISTS(r,Pattern("song_SWINGOVER.png").similar(0.98)) # song_SWINGOVER
    EXISTS(r,Pattern("song_TALIGADO.png").similar(0.98)) # song_TALIGADO
    EXISTS(r,Pattern("song_THEBOARDERLANDS.png").similar(0.98)) # song_THEBORDERLANDS
    EXISTS(r,Pattern("song_THERIODEAL.png").similar(0.98)) # song_THERIODEAL
    EXISTS(r,Pattern("song_THRILLSWITCH.png").similar(0.98)) # song_THRILLSWITCH
    EXISTS(r,Pattern("song_THUNDERDROME.png").similar(0.98)) # song_THUNDERDOME
    EXISTS(r,Pattern("song_TOYDIVISION.png").similar(0.98)) # song_TOYDIVISION
    EXISTS(r,Pattern("song_TRYSOHARD.png").similar(0.98)) # song_TRYSOHARD
    EXISTS(r,Pattern("song_TWERKINPROGRESS.png").similar(0.98)) # song_TWERKINPROGRESS
    EXISTS(r,Pattern("song_WALKINTALL.png").similar(0.98)) # song_WAIKINTALL
    EXISTS(r,Pattern("song_WANTEDMAN.png").similar(0.98)) # song_WANTEDMAN
    EXISTS(r,Pattern("song_WHATWESTARTED.png").similar(0.98)) # song_WHATWESTARTED
    EXISTS(r,Pattern("song_WHITEGIRLS.png").similar(0.98)) # song_WHITEGIRLS
    EXISTS(r,Pattern("song_WHITEWASHEDTOMB.png").similar(0.98)) # song_WHITEWASHEDTOMB
    EXISTS(r,Pattern("song_WHYDOI.png").similar(0.98)) # song_WHYDOI
    EXISTS(r,Pattern("song_YANGBANG.png").similar(0.98)) # song_YANGBANG
    EXISTS(r,Pattern("song_ZEROHOUR.png").similar(0.98)) # song_ZEROHOUR
    EXISTS(r,Pattern("song_ZOMBIEDROP.png").similar(0.98)) # song_ZOMBIEDROP
                
########################################################
# List of all the songs text images
#
#
########################################################
def music_img_list():
    find(Pattern("music_img_selected.png").similar(0.98)) # music_img_selected.png
    find(Pattern("music_img_unselected.png").similar(0.98)) # music_img_unselected
    find(Pattern("music_img_playing.png").similar(0.98)) # music_img_playing
    find(Pattern("music_btn_play-selected.png").similar(0.98)) # music_btn_play-selected.png
    find(Pattern("music_btn_play-unselected.png").similar(0.98)) # music_btn_play-unselected.png
    find(Pattern("music_btn_songplaying.png").similar(0.98)) #  music_btn_songplaying
    find(Pattern("music_btn_back.png").similar(0.69)) # music_btn_back
    find(Pattern("music_btn_musiclist.png").similar(0.69))# music_btn_musiclist
    find(Pattern("music_btn_addtovideo.png").similar(0.69))#  music_btn_addtovideo
    find(Pattern("song_THENIGHTWEDANCED.png").similar(0.98)) #song_THENIGHTWEDANCED
    find(Pattern("song_AFTERGLOW.png").similar(0.98)) # song_AFTERGLOW
    find(Pattern("song_BRINGIT.png").similar(0.98)) # song_BRINGIT
    find(Pattern("song_COMETHRU.png").similar(0.98)) # song_COMETHRU
    find(Pattern("song_DAFTCRUNK.png").similar(0.98)) # song_DAFTCRUNK
    find(Pattern("song_FEELTHELOVE.png").similar(0.98)) # song_FEELTHELOVE
    find(Pattern("song_GUILTYMAN.png").similar(0.98)) # song_HIDEANDFREAK
    find(Pattern("song_HIDEANDFREAK.png").similar(0.98)) # song_HIDEANDFREAK  
    find(Pattern("song_RAINDOWN.png").similar(0.98)) # song_RAINDOWN
    find(Pattern("song_RISEUP.png").similar(0.98)) # song_RISEUP
    find(Pattern("song_AWONDERFULSACRIFICE.png").similar(0.98)) # song_AWONDERFULSACRIFICE
    find(Pattern("song_AINTNOWAY.png").similar(0.98)) # song_AINTNOWAY
    find(Pattern("song_ALLIKNOW.png").similar(0.98)) # song_ALLIKNOW
    find(Pattern("song_AMAZEBALLS.png").similar(0.98)) # song_AMAZEBALLS
    find(Pattern("song_AMIGOS4LIFE.png").similar(0.98)) # song_AMIGOS4LIFE
    find(Pattern("song_BFF.png").similar(0.98)) # song_BFF
    find(Pattern("song_BIPOLAR.png").similar(0.98)) # song_BIPOLAR
    find(Pattern("song_BIGBOY.png").similar(0.98)) # song_BIGBOY
    find(Pattern("song_BITEME.png").similar(0.98)) # song_BITEME
    find(Pattern("song_BLAME.png").similar(0.98)) # song_BLAME
    find(Pattern("song_BLINDEDBYTHESUN.png").similar(0.98)) # song_BLINDEDBYTHESUN
    find(Pattern("song_BLOODFEUD.png").similar(0.98)) # song_BLOODFEUD
    find(Pattern("song_BRINGMEBACKTOLIFE.png").similar(0.98)) # song_BRINGMEBACKTOLIFE
    find(Pattern("song_BURYMYLOVE.png").similar(0.98)) # song_BURYMYLOVE
    find(Pattern("song_CARRYMEBACKHOME.png").similar(0.98)) # song_CARRYMEBACKHOME
    find(Pattern("song_CHOKINCHICKENS.png").similar(0.98)) # song_CHOKINCHICKENS
    find(Pattern("song_COLDFEET.png").similar(0.98)) # song_COLDFEET
    find(Pattern("song_COMBATREADY.png").similar(0.98)) # song_COMBATREADY
    find(Pattern("song_CRANKIT.png").similar(0.98)) # song_CRANKIT
    find(Pattern("song_DJBLOWUPTHESPEAKERS.png").similar(0.98)) # song_DJBLOWUPTHESPEAKERS
    find(Pattern("song_DARKFADER.png").similar(0.98)) # song_DARKFADER
    find(Pattern("song_DEADANDGONE.png").similar(0.98)) # song_DEADANDGONE
    find(Pattern("song_DOYOUFEELALIVE.png").similar(0.98)) # song_DOYOUFEELALIVE
    find(Pattern("song_DOPEDELUXE.png").similar(0.98)) # song_DOPEDELUXE
    find(Pattern("song_DROPPINDIMES.png").similar(0.98)) # song_DROPPINDIMES
    find(Pattern("song_EVERYTHING.png").similar(0.98)) # song_EVERYTHING
    find(Pattern("song_FEELSLIKEIMADEIT.png").similar(0.98)) # song_FEELSLIKEIMADEIT
    find(Pattern("song_FIFTEENWAYS.png").similar(0.98)) # song_FIFTEENWAYS
    find(Pattern("song_FRETCOLLECTOR.png").similar(0.98)) # song_FRETCOLLECTOR
    find(Pattern("song_GETTINGBUZZED.png").similar(0.98)) # song_GETTINGBUZZED
    find(Pattern("song_GLASSDARKLY.png").similar(0.98)) # song_GLASSDARKLY
    find(Pattern("song_GLOCKNROLL.png").similar(0.98)) # song_GLOCKNROLL
    find(Pattern("song_GODWILLCUTYOUDOWN.png").similar(0.98)) # song_GODWILLCUTYOUDOWN
    find(Pattern("song_GOOD4THAHOOD.png").similar(0.98)) # song_GOOD4THAHOOD
    find(Pattern("song_HALLOWEDGROUND.png").similar(0.98)) # song_HALLOWEDGROUND
    find(Pattern("song_HEAVYWEATHER.png").similar(0.98)) # song_HEAVYWEATHER
    find(Pattern("song_HEROESDRESSINBLACK.png").similar(0.98)) # song_HEROESDRESSINBLACK
    find(Pattern("song_HOLDYOURHEADUP.png").similar(0.98)) # song_HOLDYOURHEADUP
    find(Pattern("song_HUNDREDDOLLAGIRLZ.png").similar(0.98)) # song_HUNDREDDOLLAGIRLZ
    find(Pattern("song_IDAREYOU.png").similar(0.98)) # song_IDAREYOU
    find(Pattern("song_INAROW.png").similar(0.98)) # song_INAROW
    find(Pattern("song_INTHAMAISON.png").similar(0.98)) # song_INTHAMAISON
    find(Pattern("song_ITSOURS.png").similar(0.98)) # song_ITSOURS
    find(Pattern("song_JOYRIDE.png").similar(0.98)) # song_JOYRIDE
    find(Pattern("song_JUSTALITTLE.png").similar(0.98)) # song_JUSTALITTLE
    find(Pattern("song_KEEPTHEFAITHALIVE.png").similar(0.98)) # song_KEEPTHEFAITHALIVE
    find(Pattern("song_KILLINFLOOR.png").similar(0.98)) # song_KILLINFLOOR
    find(Pattern("song_KNUCKLEDRAGGER.png").similar(0.98)) # song_KNUCKLEDRAGGER
    find(Pattern("song_LIGHTEMUP.png").similar(0.98)) # song_LIGHTEMUP
    find(Pattern("song_MEADOWMIND.png").similar(0.98)) # song_MEADOWMIND
    find(Pattern("song_MOONSHINEANDGASOLINE.png").similar(0.98)) # song_MOONSHINEANDGASOLINE
    find(Pattern("song_NEWDAY.png").similar(0.98)) # song_NEWDAY
    find(Pattern("song_NOTLOOKINBACK.png").similar(0.98)) # song_NOTLOOKINBACK
    find(Pattern("song_NUCLEAR.png").similar(0.98)) # song_NUCLEAR
    find(Pattern("song_ONTHEDL.png").similar(0.98)) # song_ONTHEDL
    find(Pattern("song_ONEOFAKIND.png").similar(0.98)) # song_ONEOFAKIND
    find(Pattern("song_PALESAND.png").similar(0.98)) # song_PALESAND
    find(Pattern("song_PARTYWILLCOMEALIVE.png").similar(0.98)) # song_PARTYWILLCOMEALIVE
    find(Pattern("song_PUNCHING.png").similar(0.98)) # song_PUNCHING
    find(Pattern("song_PUSHUPTHEBEAT.png").similar(0.98)) # song_PUSHUPTHEBEAT
    find(Pattern("song_REASONS.png").similar(0.98)) # song_REASONS
    find(Pattern("song_ROCKYOURWORLD.png").similar(0.98)) # song_ROCKYOURWORLD
    find(Pattern("song_RUSHES.png").similar(0.98)) # song_RUSHES
    find(Pattern("song_SCREENDOORSLAM.png").similar(0.98)) # song_SCREENDOORSLAM
    find(Pattern("song_SHAKE.png").similar(0.98)) # song_SHAKE
    find(Pattern("song_SHAKEITOUT.png").similar(0.98)) # song_SHAKEITOUT
    find(Pattern("song_SMOKINFIRE.png").similar(0.98)) # song_SMOKINFIRE
    find(Pattern("song_SOUNDBOI.png").similar(0.98)) # song_SOUNDBOI
    find(Pattern("song_STRANGECONDITION.png").similar(0.98)) # song_STRANGECONDITION
    find(Pattern("song_STRINGOFTRUTH.png").similar(0.98)) # song_STRINGOFTRUTH
    find(Pattern("song_SUGARGIRL.png").similar(0.98)) # song_SUGARGIRL
    find(Pattern("song_SURGE.png").similar(0.98)) # song_SURGE
    find(Pattern("song_SWINGOVER.png").similar(0.98)) # song_SWINGOVER
    find(Pattern("song_TALIGADO.png").similar(0.98)) # song_TALIGADO
    find(Pattern("song_THEBOARDERLANDS.png").similar(0.98)) # song_THEBORDERLANDS
    find(Pattern("song_THERIODEAL.png").similar(0.98)) # song_THERIODEAL
    find(Pattern("song_THRILLSWITCH.png").similar(0.98)) # song_THRILLSWITCH
    find(Pattern("song_THUNDERDROME.png").similar(0.98)) # song_THUNDERDOME
    find(Pattern("song_TOYDIVISION.png").similar(0.98)) # song_TOYDIVISION
    find(Pattern("song_TRYSOHARD.png").similar(0.98)) # song_TRYSOHARD
    find(Pattern("song_TWERKINPROGRESS.png").similar(0.98)) # song_TWERKINPROGRESS
    find(Pattern("song_WALKINTALL.png").similar(0.98)) # song_WAIKINTALL
    find(Pattern("song_WANTEDMAN.png").similar(0.98)) # song_WANTEDMAN
    find(Pattern("song_WHATWESTARTED.png").similar(0.98)) # song_WHATWESTARTED
    find(Pattern("song_WHITEGIRLS.png").similar(0.98)) # song_WHITEGIRLS
    find(Pattern("song_WHITEWASHEDTOMB.png").similar(0.98)) # song_WHITEWASHEDTOMB
    find(Pattern("song_WHYDOI.png").similar(0.98)) # song_WHYDOI
    find(Pattern("song_YANGBANG.png").similar(0.98)) # song_YANGBANG
    find(Pattern("song_ZEROHOUR.png").similar(0.98)) # song_ZEROHOUR
    find(Pattern("song_ZOMBIEDROP.png").similar(0.98)) # song_ZOMBIEDROP
    
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------    
    
#m = GDA_music()
#m.testclass()
#testsongs()                
    
################################################
#
#
#
################################################    
def test_music_15(gpa,gpr):
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: CAPTURE GDA_MUSIC_TESTS 15"
    print "++++++++++++++++++++++++++++++++++"    
    testsongs(gpa,gpr,6, False)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("CAPTURE GDA_MUSIC_TESTS 15")
################################################
#
#
#
################################################
def test_music_30(gpa,gpr):
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: CAPTURE GDA_MUSIC_TESTS 30"
    print "++++++++++++++++++++++++++++++++++"    
    testsongs(gpa,gpr,30, False)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("CAPTURE GDA_MUSIC_TESTS 30")
################################################
#
#
#
################################################
def test_music_60(gpa,gpr):
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: CAPTURE GDA_MUSIC_TESTS 60"
    print "++++++++++++++++++++++++++++++++++"    
    testsongs(gpa,gpr,60, False)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("CAPTURE GDA_MUSIC_TESTS 60")
################################################
#
#
#
################################################
def record_moments_beats(gpa,gpr):
    print "++++++++++++++++++++++++++++++++++"
    print "RUN TEST: CAPTURE GDA_MUSIC_MOMENTS & BEATS"
    print "++++++++++++++++++++++++++++++++++"
    #gda_create_tests.select_moment_to_music(gpr)
    #testsongs(gpa,gpr,6, False)
    gda_utils.putDictToFile(gda_utils.d_similarity)    
    gda_utils.printreport("CAPTURE GDA_MUSIC_TESTS 15")
    
def selectNonPremiumMusic(REGION,song,action="close"):
    rc=False
    png=Pattern(song).similar(0.69)
    #selectsong_addtovideo(REGION,png,retrycount=0, playsong=1,song_similarity=0.59):
    rsong=selectsong_addtovideo(REGION,png,1,0.69)
    if rsong:
        wait(5)
        pop=Pattern("popup_txt_unlockthistrack.png").similar(0.69)
        mpop=gda_utils.EXISTS2(REGION,pop)
        if mpop:
            mpop.highlight(1)
            ptry=Pattern("popup_txt_TRYGOPROPLUS.png").similar(0.69)
            mtry=gda_utils.EXISTS2(REGION,ptry)
            if mtry:
                if action=="close":
                    mtry.highlight(1)
                    mclose=mpop.above(20)
                    mclose.highlight(1)
                    mclose.click()
                    rc=True
                elif action=="try":
                    mtry.click()
                    rc=True
            #pclose=Pattern("popup_txt_close.png").similar(0.69)
    return rc
      
def generate_Testrail_songs_regression_suite():
    msongs = GDA_music()
    testlist=[]
    testnames=[" - 1.Select Song",
               " - 2.Moments Select Max 60",
               " - 3.Output MP4 60 Sec",
               " - 4.Output MP4 30 Sec",
               " - 5.Output MP4 15 Sec",
               " - 6.MP4 in Edits-Scene Detect-60 Sec",
               " - 7.MP4 in Edits-Scene Detect-30 Sec",
               " - 8.MP4 in Edits-Scene Detect-15 Sec",
               " - 9.MP4 in Edits-Song Analysis-60 Sec",
               " - 10.MP4 in Edits-Song Analysis-30 Sec",
               " - 11.MP4 in Edits-Song Analysis-15 Sec"]

    for song in msongs.sortedsonglist:
        name = song.replace(".png","").replace("song_","")
        for test in testnames:
            tr = "%s%s"  % (name, test)
            testlist.append(tr)
    sout = ""
    for test in testlist:
        sout+="%s\n" % test
    gda_utils.filewrite("/Automation/songs_testrail_suite.txt",sout)
    #print sout
######################################
# Simple music selection analytics test:
# select each song in list and try to add music
# The popup dialog will block the song
# First attempt will close dialog
# Second attempt will try to go to browser, browser tab is ignored so they accumulate
# Mara validates the analytics
######################################
def test_analytics(song="song_AMIGOS4LIFE.png"):
    gda_utils.GetEnvInfo()
    gpa,gpr=gda_utils.AppStart("GoPro Quik")
    if not gpr:
        return
    set_MUSIC_SCREEN_regions(gpr)
    msongs=GDA_music()
    testmusic_init(msongs)
    gda_utils.d_gda_settings["MUSIC_LIST_ITEMS_LOCKED"]=True #Assume select NON-plus account music list
    resultlist=[]
    id = msongs.findsortedsongindex(song)
    pclose=0
    ptry=0
    fclose=0
    ftry=0
    counter=0
    for i in range(id,len(msongs.sortedsonglist),1):
        counter+=1
        png = msongs.sortedsonglist[i]
        resultlist.append("=====================================")
        print "====================================="
        msg= "%d. %d=TEST SONG %s" % (counter,i,png)
        resultlist.append(msg)
        print msg
        if selectNonPremiumMusic(gpr,png,"close"):
            msg= "%d. PASSED: Close, %s" % (counter,png)
            pclose+=1
        else:
            msg= "%d. FAILED: Close, %s" % (counter,png)
            fclose+=1
        resultlist.append(msg)
        
        if selectNonPremiumMusic(gpr,png,"try"):
            msg= "%d. PASSED: Try, %s" % (counter,png)
            ptry+=1
        else:
            msg= "%d. FAILED: Try, %s" % (counter,png)
            ftry+=1
        resultlist.append(msg)
        msg= "Counts: PASSED Tests [close=%d, try=%d]" % (pclose,ptry)
        resultlist.append(msg)
        msg= "Counts: FAILED Tests [close=%d, try=%d]" % (fclose,ftry)
        resultlist.append(msg)
        print "====================================="
        for s in resultlist:
            print s
            
######################################
# for debugging in sikuli ide
# 
# 
######################################
def test_module():
    gda_utils.d_gda_settings["NO-TestRail"]=True
    gda_utils.GetEnvInfo()
    gpa,gpr=gda_utils.AppStart("GoPro Quik")
    set_MUSIC_SCREEN_regions(gpr)
    return
    msongs=GDA_music()
    testmusic_init(msongs)
    findsongregion(Pattern("song_RISEUP.png").similar(0.69))

def test1():
    generate_Testrail_songs_regression_suite()
            
######################################
# for debugging in sikuli ide
# 
# KEEP THIS COMMENTED when checking in to GIT
######################################    
test_module()    
#test_analytics("song_AMIGOS4LIFE.png")    
#test1()