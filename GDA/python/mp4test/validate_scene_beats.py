

import os
import sys
import datetime
import logging
import csv
import json
import utils
from termcolor import colored
import aggregate_artifacts

class Logger(object):
    def __init__(self, filename="Default.log"):
        if os.path.isfile(filename):
            os.remove(filename)
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)


#####################################################
# load song json
# iterate the mp4 and find all matching csv's and report missing
# iterate & read scene csv, convert to json, add to songs & report json song node
# compare song node marks timings with the scene timings, result in report json song node
# save report json every iteration
#
#####################################################
class ValidateSceneBeats:
    def __init__(self, testname,csvroot,songjsonpath):
        self.done = False
        self.tolerance = 0.9
        self.min_scene_len=0.1
        self.graphposition=120
        self.utils = utils.Utils()
        self.testpass=[]
        self.testfail=[]
        self.failedlist=[]
        self.passedlist=[]
        self.errorlist = []
        self.csvroot = csvroot
        self.songjsonpath=songjsonpath
        self.songjson = None
        self.testname = testname
        self.report = []
        self.songs = {}
        self.loadsongsjson()
        self.Process_songs_beats_scenes()

    def loadsongsjson(self):
        rc=False
        self.songjson = self.utils.json_load(self.songjsonpath)
        if not self.songjson:
            logging.ERROR("Cant continue without the song data, songjson")
        else:
            rc=True

        return rc

    def convert_csv_json(self, csvpath):
        # Open the CSV
        jcsv = None
        if not os.path.isfile(csvpath):
            logging.INFO("Failed convert_csv_json, invalid path:%s" % csvpath)
            return jcsv
        try:
            f = open(csvpath, 'rU')
            # Change each fieldname to the appropriate field name. I know, so difficult.
            reader = csv.DictReader(f, fieldnames=("Scene Number","Frame Number (Start)","Timecode","Start Time (seconds)","Length (seconds)"))
            # Parse the CSV into JSON

            scsv = json.dumps([row for row in reader])
            jcsv=json.loads(scsv)

        except Exception, e:
            logging.ERROR("Error: convert_csv_json")
            logging.ERROR(str(e))
        return jcsv

    def findsong(self,songname):
        d_song = {}
        for i in range(0,len(self.songjson["songs"])):
            node = self.songjson["songs"][i]
            if "png" in node:
                if str(node["png"]) == songname:
                    d_song = self.songjson["songs"][i]
                    return i, d_song
        return -1, None

    def setsongnode(self,id,song):
        self.songjson["songs"][id]=song

    def savesongs(self):
        rc=False
        if not self.utils.json_save(self.songjsonpath, self.songjson):
            logging.INFO("Failed savesongs:%s" % self.songjsonpath)
        else:
            rc = True
        return rc

    ################################
    # load iterate gda_create_tests_record
    #
    #
    ################################
    def Process_songs_beats_scenes(self):
        self.loadcsvscenedata()
        self.verifybeats()

    def verifybeats(self):
        failbeats=[]
        errorlist=[]
        testcount = 0 #testcount - len(failbeats)=PASSED
        for i in range(0, len(self.songjson['songs'])):
            testcount+=1
            song=self.songjson['songs'][i]
            songmarks=self.getmarks(song)
            if not songmarks or len(songmarks)==0:
                failbeats.append(song)
                continue
            song['testmarks']=songmarks

            failedlist,passedlist,errorlist=self.eval_scenes_to_mp3marks(song)
            if len(failedlist)==0:
                if len(errorlist)==0:
                    self.testpass.append(song['png'])
                else:
                    skip=0
                    error=0
                    for err in errorlist:
                        if "SKIPPING" in err:
                            skip+=1
                        else:
                            error+=1
                    if error==0 and skip>0:
                        self.testpass.append(song['png'])
                    else:
                        self.testfail.append(song['png'])
            else:
                self.testfail.append(song['png'])

            self.failedlist.extend(failedlist)
            self.passedlist.extend(passedlist)
            self.errorlist.extend(errorlist)
        print"======================================================"
        print"======================================================"
        for passed in self.passedlist:
            print passed
        print"======================================================"
        print colored(" S O N G  T E S T S  F A I L E D  D E T A I L S   beats & scene tolerance=%0.1f" % self.tolerance,"red")
        print"======================================================"
        print "MP4 beats Graph: 1 char position = 1 second, '|'=other beat time, '*'=detected scene time, '^'=calculated beat time, '+'=scene & beat in same seconds position"
        print "mp4 seconds: [         111111111122222222223]"
        print "mp4 seconds: [123456789012345678901234567890]"
        print "MP4 Graph:   [...|...|..||||.|.|.|||*|.|....]"
        for err in self.failedlist:
            if "SKIPPING" not in err:
                print err
        print"======================================================"
        print colored(" S O N G  T E S T S  E R R O R S   beats & scene tolerance=%0.1f" % self.tolerance,"yellow")
        print"======================================================"
        print "Graph: 1 char position = 1 second, '|'=beat time"
        print "[...|...|..||||.|.|.|||.|.|....]"
        for err in self.errorlist:
            if "SKIPPING" not in err:
                print err

        print"======================================================"
        print colored(" S O N G  T E S T S  P A S S E D","green")
        print"======================================================"
        id=0
        for p in self.testpass:
            id+=1
            print "%d. TEST PASSED: %s" % (id,p)
        print"======================================================"
        print colored(" S O N G  T E S T S  F A I L E D   beats & scene tolerance=%0.1f" % self.tolerance,"red")
        print"======================================================"
        for p in self.testfail:
            id+=1
            print "%d. TEST FAILED: %s" % (id,p)

        print"======================================================"
        print " T E S T  S U M M A R Y   beats & scene tolerance=%0.1f" % self.tolerance
        print"======================================================"
        p=colored("PASSED","green")
        print "%s TESTS = %d" % (p,len(self.testpass))
        f = colored("FAILED", "red")
        print "%s TESTS = %d" % (f,len(self.testfail))
        print"-----------------------------------------"
        n= len(self.testpass)
        n+=len(self.testfail)
        print "TOTAL SONG TESTS = %d" % n
        self.done=True

    def evalmark(self,sgraph,mark,chr):
        f="%.1f" % mark
        f=int(round(mark))
        m1=(f)-1
        sgraph = sgraph[:m1] + chr + sgraph[(m1+1):]
        return sgraph

    def eval_scenes_to_mp3marks(self,song):
        durlist = ['15', '30', '60']
        failedlist=[]
        passedlist=[]
        errorlist=[]
        self.tolerance = 0.5
        self.min_scene_len=0.1
        for dur in durlist:
            scenekey = "scenes_%s" % dur
            trackkey = "track%s" % dur
            markdif = []
            markgraph = '.' * int(dur)
            beatgraph = '.' * int(dur)
            #get marks for duration
            lastmark=0
            last1=0
            numbs=""
            markscount=0
            beatscount=0
            overlapchar='1'
            lastdiff=0
            for markid in song['testmarks'][trackkey]['testmarks']:
                marktime = markid['music_seconds']
                if lastmark>0:
                    numbs += "%.1f" % (lastmark)
                    #markgraph = self.evalmark(markgraph,marktime,'|')
                    #markgraph = self.evalmark(markgraph, lastmark, '|')
                    diff = lastmark+((marktime-lastmark)/2)
                    numbs += "[%.1f]" % (diff)
                    if lastdiff == diff:
                        beatgraph = self.evalmark(beatgraph, diff, '2')
                    else:
                        beatgraph = self.evalmark(beatgraph, diff, '1')
                    lastdiff = diff
                    markgraph = self.evalmark(markgraph, lastmark, overlapchar)
                    beatscount+=1
                    markscount+=1
                    markdif.append(diff)
                if round(lastmark) == round(marktime):
                    overlapchar = '2'
                else:
                    overlapchar = '1'
                lastmark=marktime
            numbs += "%.1f" % (lastmark)
            markgraph = self.evalmark(markgraph, lastmark, overlapchar)
            markscount+=1
            if len(markdif)>0:
                markcount = -1
                if scenekey in song:
                    if 'scenelist' in song[scenekey]:
                        for scene in song[scenekey]['scenelist']:
                            id = scene["Scene Number"][:2]
                            if not id[:1].isdigit():
                                continue
                            id = int(id)
                            if id > 0:
                                scenetime = float(scene["Start Time (seconds)"])
                                scenelen = float(scene["Length (seconds)"])
                                if scenelen>self.min_scene_len:
                                    markcount += 1
                                    beattest = "FAILED:"
                                    if markcount < len(markdif):
                                        beattime = float(markdif[markcount])
                                        dif = scenetime - beattime
                                        if beattime > scenetime:
                                            dif = beattime - scenetime
                                        if dif <= self.tolerance:
                                            beattest = "PASSED:"
                                            sout = "%s %s-%s: scene:%.2f | beat:%.2f" % (beattest, song['png'], dur, scenetime, beattime)
                                            passedlist.append(sout)
                                        else:
                                            beatgraph1 = self.evalmark(beatgraph, beattime, '+')
                                            if round(beattime)<>round(scenetime):
                                                beatgraph1 = self.evalmark(beatgraph1, beattime, '^')
                                                beatgraph1 = self.evalmark(beatgraph1, scenetime, '*')
                                            sout1 = "%s %s-%s: scene:%.2f | beat:%.2f, Diff:%.2f Exceeds tolerance of %.2f beats=%d marks=%d" % (beattest, song['png'], dur, scenetime, beattime, dif, self.tolerance,beatscount,markscount)
                                            sout2 = "beats[%s] marks[%s] <%s>" % (beatgraph1,markgraph,numbs)
                                            errlen=len(sout1)
                                            if errlen>self.graphposition:
                                                self.graphposition=errlen+5
                                            sout = sout1 + (" " *(self.graphposition-errlen))+sout2
                                            sout = colored(sout, 'red')
                                            failedlist.append(sout)

                                        logging.info(sout)
                                    else:
                                        sout = "ERROR: %s-%s: scene:%d | No matching Scene=Beat item: %d, missing beat calc item=%d marks=%d [%s] <%s>" % (song['png'], dur, scenetime, markcount, len(markdif), markscount, beatgraph, numbs)
                                        sout = colored(sout, 'yellow')
                                        logging.warn(sout)
                                        failedlist.append(sout)
                                else:
                                    sout = "SKIPPING, no eval: %s-%s: Invalid scene length=[%0.3f] beats=%d marks=%d [%s] <%s>" % (song['png'], dur, scenelen, beatscount, markscount, beatgraph, numbs)
                                    sout = colored(sout, 'green')
                                    logging.warn(sout)
                    else:
                        sout = "ERROR: %s-%s: No scenelist data in song[%s] beats=%d marks=%d [%s] <%s>" % (song['png'], dur, scenekey, beatscount, markscount, beatgraph, numbs)
                        sout = colored(sout, 'yellow')
                        errorlist.append(sout)
                        logging.warn(sout)
                else:
                    sout="ERROR: %s-%s: No scenelist data in song[%s] beats=%d marks=%d [%s] <%s>" % (song['png'], dur, scenekey, beatscount, markscount, beatgraph, numbs)
                    sout = colored(sout, 'yellow')
                    errorlist.append(sout)
                    logging.warn(sout)
            else:
                sout="ERROR: %s-%s: No markdiff data: %s beats=%d marks=%d [%s] <%s>" % (song['png'], dur, scenekey, beatscount, markscount, beatgraph, numbs)
                sout = colored(sout, 'yellow')
                errorlist.append(sout)
                logging.warn(colored(sout))
        return failedlist, passedlist,errorlist

    # def evalscene_beatsmarks(self,song):
    #     durlist = ['15','30','60']
    #     tolerance=3
    #     failedlist=[]
    #     passedlist=[]
    #     for dur in durlist:
    #         scenekey = "scenes_%s" % dur
    #         trackkey = "track%s" % dur
    #         markcount=-1
    #         if not scenekey in song:
    #             sout= "Error No scene key: %s-%s %s" %(song['png'],dur, scenekey)
    #             logging.error(sout)
    #             failedlist.append(sout)
    #             continue
    #         for scene in song[scenekey]['scenelist']:
    #             id=scene["Scene Number"][:2]
    #             if not id[:1].isdigit():
    #                 continue
    #             id=int(id)
    #             if id>0:
    #                 scenetime=round(float(scene["Start Time (seconds)"]))
    #                 markcount+=1
    #                 beattest="FAILED:"
    #                 if markcount<len(song['testmarks'][trackkey]['testmarks']):
    #                     marktime=round(float(song['testmarks'][trackkey]['testmarks'][markcount]['music_seconds']))
    #                     dif=scenetime-marktime
    #                     if marktime>scenetime:
    #                         dif=marktime-scenetime
    #                     if dif<=tolerance:
    #                         beattest="PASSED:"
    #                         sout= "%s%s-%s: scene:%d | beat:%d" % (beattest,song['png'],dur,scenetime,marktime)
    #                         passedlist.append(sout)
    #                     else:
    #                         sout= "%s%s-%s: scene:%d | beat:%d" % (beattest,song['png'],dur,scenetime,marktime)
    #                         failedlist.append(sout)
    #
    #                     logging.info(sout)
    #                 else:
    #                     sout= "Error: %s-%s: scene:%d | beat:No mark Index: %d" % (song['png'], dur, scenetime, markcount)
    #                     logging.warn(sout)
    #                     failedlist.append(sout)
    #     return failedlist,passedlist


    def getmarks(self,song):
        songmarks={}
        # if song['png']=="song_HIDEANDFREAK.png":
        #     print
        for track in song['tracks']:
            trackname = ""
            marks = {}
            duration = track['duration_seconds']
            if duration < 20:
                trackname = "track15"
            elif duration < 40:
                trackname = "track30"
            elif duration < 70:
                trackname = "track60"
            else:
                logging.warn("Duration not found")
                return None
            songmarks[trackname]={}
            songmarks[trackname]['testmarks']=track['marks'][len(track['marks'])-1] #get max marks
            #songmarks[trackname]['version'] = track['marks']['version']
            songmarks[trackname]['duration'] = duration
            #songmarks[trackname]['mp3source'] = track['marks']['music_source_file_short_name']
        return songmarks
    def loadcsvscenedata(self):
        faillist=[]
        noscene=[]
        dosave=False
        for i in range(0, len(self.songjson['songs'])):
            if 'scenes' not in self.songjson['songs'][i]:
                noscene.append(self.songjson['songs'][i]['png'])
        if len(noscene) ==0:
            return faillist
        for subdir, dirs, files in os.walk(self.csvroot):
            for file in files:
                filename, file_extension = os.path.splitext(file)
                if file_extension == ".csv":
                    pngname = "song_%s.png" % filename[4:-2]
                    if pngname not in noscene:
                        continue #skip
                    dur=filename[-2:]
                    csvpath = os.path.join(subdir, file)
                    csvjson = self.convert_csv_json(csvpath)
                    if csvjson:
                        id, songjson = self.findsong(pngname)
                        if id>=0 and songjson:
                            scenekey="scenes_%s" % dur
                            songjson[scenekey] = {}
                            songjson[scenekey]["scenelist"]=csvjson
                            songjson[scenekey]["PASSED"] = ""
                            songjson[scenekey]["FAILED"] = ""
                            songjson[scenekey]["csvfile"] = csvpath
                            self.songjson["songs"][id] = songjson
                            dosave = True
                        else:
                            faillist.append(logging.warn("Missing song json node: " + pngname + " "+filename))
                    else:
                        faillist.append(logging.warn("Missing csv: "+filename))
        if dosave:
            self.savesongs()
            self.loadsongsjson()
        return faillist


def test_ValidateSceneBeats():

    sys.stdout = Logger("/Users/autogda/gda_music_images-Mac210_5265_161031/FAILED/gda_music_images-Mac210_5265_161031.log")
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    vsb=ValidateSceneBeats("Mac210_5265_161031","/Users/autogda/Downloads/edits_Mac210_5265_161031","/Users/autogda/gda_music_images-Mac210_5265_161031/gda_create_tests_record.json")
    #csvpath=os.path.join(vsb.csvroot, "songZEROFSGIVEN60.csv")
    #vsb.convert_csv_json(csvpath)
    if vsb.done:
        ag=aggregate_artifacts.Aggregate(vsb.failedlist,"/Users/autogda/Downloads/edits_Mac210_5265_161031","/Users/autogda/gda_music_images-Mac210_5265_161031","/Users/autogda/gda_music_images-Mac210_5265_161031/FAILED")



test_ValidateSceneBeats()