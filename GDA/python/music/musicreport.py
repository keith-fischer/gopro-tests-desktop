#!/bin/python
import os
import sys
import platform
from os.path import expanduser
import json

# --------------------------------------------------------------------------
# get platform
# iterare folders
# concatinate found music json
# save json to automation area
# iterate the automation music json
# write user readable report txt file
# --------------------------------------------------------------------------
class processmusic:
    def __init__(self):
        self.musiccount = 0
        self.musicsum_15 = 0
        self.musicsum_30 = 0
        self.musicsum_60 = 0
        self.platform_system = None
        self.platform_release = None
        self.home = None
        self.music_root = None
        self.evalplatform()
        self.automation_root = None
        self.musiclistfile = "GDA_musiclist.json"
        self.musicreportfile = "GDA_musicmoments.txt"
        self.isWin = False
        self.isMac = False
        self.musicreport = "item\tMusic Title\tMax Moment Count 15\tMax Moment Count 30\tMax Moment Count 60\tBeats Per Minute\tGenre\tVer\tVibes\tpngname\tErrors"
        self.evalplatform()
        self.printstuff()
        self.musiclist = []
        self.processmusic()
        self.savemusic()
        self.savereport()


    def printstuff(self):
        print self.platform_system
        print self.platform_release
        print self.home
        print self.music_root

    def evalplatform(self):
        self.platform_system = platform.system() #Darwin = Mac
        self.platform_release = platform.release()
        self.home = expanduser("~")
        if self.platform_system == "Windows":
            self.music_root = "\\AppData\\Local\\GoPro\\Music"
            self.automation_root = "%s\\workspace\\" % self.home
            #self.automation_root = "/Automation/gopro-tests-desktop/GDA/Music_Tests"
            self.isWin = True
        elif self.platform_system == "Darwin":
            self.music_root = "/Library/Application Support/com.GoPro.goproapp.GoProMusicService/Music"
            #self.automation_root = "%s/workspace/" % self.home
            self.automation_root = "/Automation/gopro-tests-desktop/GDA/Music_Tests/"
            self.isMac = True

    def savemusic(self):
        # Writing JSON data
        jpath = self.automation_root+self.musiclistfile
        mdict = {}
        mdict["musiclist"] = self.musiclist
        #m = json.dumps(mdict, 4)
        with open(jpath, 'w') as f:
            json.dump(mdict, f, indent=4)
            f.close()

        if not os.path.isfile(jpath):
            print "Failed to write json:%s" % jpath
        print self.musicreport

    def savereport(self):
        rpath = self.automation_root+self.musicreportfile
        msum = "\tSum\t%s\t%s\t%s\n" % (str(self.musicsum_15), str(self.musicsum_30), str(self.musicsum_60))
        with open(rpath, "w") as text_file:
            text_file.write(msum+self.musicreport)
    def getmusicpngname(self,songname):
        pngname = songname.upper()
        pngname = pngname.replace(" ","")
        pngname = pngname.replace("'", "")
        return "song_" + pngname + ".png"
    def makereport(self,jmusic): #"music_title\tmom_15\tmom_30\tmom_60\tbpm\tgenre\tver\t"
        # "music_title\tmom_15\tmom_30\tmom_60\tbpm\tgenre\tver\t"
        self.musiccount += 1
        momlist = []
        errors = ""
        mmoms = ""
        t15=0
        t30=0
        t60=0
        for m in range(0,len(jmusic["tracks"])):
            tcount = len(jmusic["tracks"][m]["marks"])
            tmsecs=jmusic["tracks"][m]["duration_seconds"]
            tmsecs=round(tmsecs, 0)
            if m < 3:
                if tmsecs >14 and tmsecs <20:
                    self.musicsum_15 += tcount
                    t15=tcount
                elif tmsecs>28 and tmsecs<33:
                    self.musicsum_30 += tcount
                    t30=tcount
                elif tmsecs>58 and tmsecs<63:
                    self.musicsum_60 += tcount
                    t60=tcount

            else:
                errors += "|too many tracks:%s" % str(tcount)

        mmoms += "%s\t%s\t%s\t" % (str(t15),str(t30),str(t60))

        mtitle = str(jmusic["music_title"]["en"]).encode("utf8")
        if not mtitle or len(mtitle)<3:
            errors += "|music_title"
        mpngname = self.getmusicpngname(mtitle)
        mbpm = str(jmusic["beats_per_minute"])
        if not mbpm or len(mbpm) == 0:
            errors += "|beats_per_minute"
        mgenre = jmusic["genre"]
        mver = jmusic["version"]
        if mtitle == "Heroes Dressed in Black":
            print
        vibes = ""
        for vibe in jmusic["vibes"]:
            vibes += "%s|" % vibe

        self.musicreport +="\n%s\t%s\t%s%s\t%s\t%s\t%s\t%s\t%s" % (str(self.musiccount), mtitle, mmoms, mbpm, mgenre, mver,vibes,mpngname,errors)

    def processmusic(self):
        rootdir = "%s/%s" % (self.home, self.music_root)
        self.musiclist = []
        self.musiccount = 0
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                jpath = os.path.join(subdir, file)
                filename, file_extension = os.path.splitext(file)
                if file_extension == ".json":
                    mj = None
                    with open(jpath, 'r') as f:
                        mj = json.load(f)
                    if mj:
                        if 'music_title' in mj:
                            mj['pngsong_name'] = self.getmusicpngname(str(mj['music_title']['en']))
                        #elif 'templates' in mj:
                        #    mj['pngsong_name'] = self.getmusicpngname(str(mj['templates']['title']))
                            self.musiclist.append(mj)
                            self.makereport(mj)
                            print json.dumps(mj)
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
def main(argv):
    p = processmusic()
    print

if __name__ == "__main__":
   main(sys.argv[1:])
