
import os
import sys
import shutil
import glob
from os.path import expanduser

#####################################
#
#
#
########################################
class Aggregate():
    def __init__(self,faillist,scrnshotsdir,editsdir,artifactfolder):
        self.artifactfolder=artifactfolder
        self.editsdir=editsdir
        self.scrnshotsdir = scrnshotsdir
        self.faillist=faillist
        self.home=expanduser("~")
        self.processfaillist()
    def init(self):
        rc=False
        if os.path.isdir(self.editsdir):
            if os.path.isdir(self.artifactfolder):
                return True
            else:
                os.mkdir(self.artifactfolder)
                if os.path.isdir(self.artifactfolder):
                    return True
                else:
                    print "Failed source root dir %s" % self.artifactfolder
        else:
            print "Invalid source root dir %s" % self.editsdir


    def filewrite(self,path,data):
        rc = False
        try:
            with open(path, 'w') as f:
                f.write(data)
                f.close()
            if os.path.isfile(path):
                rc=True
        except Exception, e:
            print path
            print str(e)
        return rc
    #####################################
    # copy file
    #
    #
    ########################################
    def copyfile(self,src,dst):
        rc=False
        try:
            if not os.path.isfile(dst):
                shutil.copy2(src, dst)
                if os.path.isfile(dst):
                    rc=True
                else:
                    print "Failed: %s" % dst
            else:
                print "Skipped: "+ dst
                rc = True
        except Exception, e:
            print src
            print dst
            print str(e)

        return rc

    def makefilelist(self,song,dur,info):
        song2=song.replace("_","")
        #songRAINDOWN60.mp4.Scene-10-IN.jpg
        songdur="%s-%s" % (song,dur)
        outputpath= os.path.join(self.artifactfolder,songdur)
        if not os.path.isdir(outputpath):
            os.mkdir(outputpath)
            if not os.path.isdir(outputpath):
                print "Failed to create song dir %s" % outputpath
        infofile = os.path.join(outputpath, str(songdur + ".txt"))
        if not self.filewrite(infofile, info):
            print "failed write info %s" + infofile

        jsonpath=os.path.join(self.home+"/Library/Application Support/com.GoPro.goproapp.GoProMusicService/Music", song2[4:])
        jsonf="%s.json" % song2[4:]
        jsonpath=os.path.join(jsonpath,jsonf)
        jsondst=os.path.join(outputpath,jsonf)
        if not self.copyfile(jsonpath, jsondst):
            print "Failed" + jsondst
        #/Users/keithfisher/Library/Application Support/com.GoPro.goproapp.GoProMusicService/Music/RainDown
        song3 = "%s%s*" % (song2,dur)

        filter=os.path.join(self.editsdir,song3)

        flist=glob.glob(filter)
        for f in flist:
            fname=os.path.basename(f)
            newpath=os.path.join(outputpath,fname)
            if not self.copyfile(f,newpath):
                print "Failed" + newpath

        #selectedmoments-Video_1-4_15sec_3cnt_song_DOYOUFEELALIVE.png
        song3 = "*_%ssec_*%s.png" % (dur,song)
        filter = os.path.join(self.scrnshotsdir, song3)

        flist = glob.glob(filter)
        for f in flist:
            fname = os.path.basename(f)
            newpath = os.path.join(outputpath, fname)
            self.copyfile(f, newpath)

        # song_DOYOUFEELALIVE_viewbeats_15.png
        # song_DOYOUFEELALIVE_viewmoments_15
        song3 = "%s_*_%s.png" % (song, dur)
        filter = os.path.join(self.scrnshotsdir, song3)

        flist = glob.glob(filter)
        for f in flist:
            fname = os.path.basename(f)
            newpath = os.path.join(outputpath, fname)
            self.copyfile(f, newpath)

    #####################################
    # itrerate fails
    #
    #
    ########################################
    def processfaillist(self):
        if not self.init():
            print "Failed init in aggregate_artifacts.Aggregate"
            return
        #ERROR: song_HALLOWEDGROUND.png-60: scene:59 | No matching Scene=Beat item: 14, missing beat calc item=14 marks=15 [..1..1..1...1....1....1...1.1..1.....1.....1.....1..1.1.....] <1.4[2.7]3.9[5.8]7.8[9.1]10.4[13.1]15.7[18.2]20.7[23.5]26.2[27.4]28.7[29.3]29.9[31.9]33.9[37.8]41.8[44.4]47.0[49.5]52.0[52.7]53.5[54.8]56.1>
        #FAILED: song_HEAVYFOG.png-60: scene:51.89 | beat:53.00, Diff:1.11 Exceeds tolerance of 0.50 beats=14 marks=15           beats[......1...1.1..1...1..1.1.1.1...1..1...1....1......*^.......] marks[...1....1..1.1...1..1...11.1.1....1.1....1....1...........1.] <3.6[6.5]9.4[10.9]12.3[13.3]14.2[16.3]18.3[19.8]21.2[22.9]24.5[25.2]26.0[26.9]27.8[29.0]30.2[32.8]35.4[36.3]37.1[39.7]42.3[44.8]47.3[53.0]58.7>
        print self.artifactfolder
        for failitem in self.faillist:
            item=str(failitem).split(": ")
            if len(item)<3:
                continue
            status=str(item[0])
            song1=str(item[1])
            info=str(item[2])
            ext=".png"
            song1=song1.split(".png-")
            if len(song1) == 2:
                song=str(song1[0])
                dur=str(song1[1])

                print "%s %s-%s  %s" % (status, song, dur, info)
                self.makefilelist(song,dur,failitem)
            else:
                print "error: " + str(song1)
                continue

