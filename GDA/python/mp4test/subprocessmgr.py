#!/bin/python
import subprocess
import os
import sys
import datetime
import psutil as ps
import psutil
import time
from threading import Timer,Thread,Event
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
import logging

#sys.path.append('/Automation/gopro-tests-desktop/GDA/python/testrail')
import client_testrail_test

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
#################################################
# scenedetect song process invocation cmd's are are added to startproc
# if runprocs is called then the event procs run timer starts
# event timer will check the cpu usage and start a scenedetect process from the startproc[0]
# startproc items get moved to runprocs
# completed runprocs get moved to doneprocs

class MovingAvg:
    def __init__(self,size):
        self.size=size
        self.numlist=[]
        self.moving_avg=-1

    def getAvg(self,newvalue):
        self.numlist.append(newvalue)
        while len(self.numlist)>self.size:
            self.numlist.pop(0)
        total=sum(self.numlist)
        self.moving_avg=total/len(self.numlist)
        return self.moving_avg

class SubProcMgr:
    _settings = {}
    startprocs = []
    runprocs = []
    doneprocs = []
    failprocs = []
    maxcpu = 80  # dont start new processes when cpu % is maxed
    rampdelaysecs = 30  # ramp additional processes every n seconds until maxed
    autorun = True
    runevent = BackgroundScheduler()
    runmax = 500
    moving_avg=MovingAvg(10)
    def __init__(self):
        SubProcMgr.runevent = BackgroundScheduler()
        SubProcMgr.runevent.add_job(SubProcMgr.runproc,'interval', seconds=SubProcMgr.rampdelaysecs)
        SubProcMgr.runevent.start()
        #logging.basicConfig()
    def addproc(self,mp4,csv,root):
        procitem = SubProcMgr.ProcItem(mp4,csv,root)
        self.startprocs.append(procitem)
        if SubProcMgr.runevent:
            job=SubProcMgr.runevent.get_jobs()
            # if len(job)==0:
            #     SubProcMgr.stopprocs()
            #     SubProcMgr.runevent.start()

    @staticmethod
    def getjobcount():
        rc=0
        if SubProcMgr.runevent:
            job=SubProcMgr.runevent.get_jobs()
            return len(job)
        return rc

    @staticmethod
    def isjobsdone():
        rc=False
        n=SubProcMgr.getjobcount()
        if n==0:
            return True
        return rc

    @staticmethod
    def stopprocs():
        rc = False
        # this will stop the scheduler
        if SubProcMgr.runevent: # and SubProcMgr.autorun==False:
            SubProcMgr.runevent.remove_all_jobs()
            SubProcMgr.runevent.shutdown()
            rc = True
        return rc

    @staticmethod
    def runproc():
        if len(SubProcMgr.startprocs)==0 and len(SubProcMgr.runprocs)==0:
            SubProcMgr.stopprocs()
            return
        rc=False #SubProcMgr.stopprocs()  # kill scheduler
        cpu_percent = round(psutil.cpu_percent(), 1)
        cpu_percent=SubProcMgr.moving_avg.getAvg(cpu_percent)
        print "CPU:%d" % cpu_percent
        if len(SubProcMgr.startprocs)>0 and cpu_percent<SubProcMgr.maxcpu:
            runcmd=SubProcMgr.startprocs.pop(0)
            runcmd.subproc = subprocess.Popen(runcmd.fullproc, stdout=subprocess.PIPE, shell=True,cwd=runcmd.root)
            runcmd.starttime = datetime.datetime.now()
            SubProcMgr.runprocs.append(runcmd)
        if len(SubProcMgr.runprocs)>0:
            i=-1
            while(len(SubProcMgr.runprocs)>0):
                i+=1
                if i>=len(SubProcMgr.runprocs):
                    break

                try:
                    print "%d:%d" % (i,len(SubProcMgr.runprocs))
                    proc=SubProcMgr.runprocs[i].subproc
                    proc.poll()

                    if proc.returncode==None:
                        runproc=SubProcMgr.runprocs[i]
                        runproc.passfail=False
                        endtime = datetime.datetime.now()
                        diff = (endtime - runproc.starttime).total_seconds()
                        if diff < SubProcMgr.runmax:
                            print "running %s" % runproc.mp4
                            continue
                        else: #stuck process
                            runproc = SubProcMgr.runprocs.pop(i)
                            runproc.endtime = endtime
                            runproc.durationsec = diff
                            runproc.stdout, runproc.stderr = runproc.subproc.communicate()

                            if runproc.stderr==None or len(str(runproc.stderr)) == 0:
                                runproc.passfail = True
                                SubProcMgr.doneprocs.append(runproc)

                            else:
                                SubProcMgr.failprocs.append(runproc)
                                try:
                                    runproc.subproc.terminate()
                                    print "Failed & Killed %s" % runproc.mp4
                                except:
                                    print "Failed & Killed %s" % runproc.mp4
                    elif proc.returncode==0: #exit ok
                        runproc=SubProcMgr.runprocs.pop(i)
                        runproc.endtime = datetime.datetime.now()
                        runproc.durationsec = (runproc.endtime-runproc.starttime).total_seconds()
                        runproc.stdout, runproc.stderr = runproc.subproc.communicate()
                        runproc.passfail = True
                        SubProcMgr.doneprocs.append(runproc)
                    else: #non zero exit code
                        runproc=SubProcMgr.runprocs.pop(i)
                        runproc.endtime = datetime.datetime.now()
                        runproc.durationsec = (runproc.endtime-runproc.starttime).total_seconds()
                        runproc.stdout,runproc.stderr = runproc.subproc.communicate()
                        SubProcMgr.failprocs.append(runproc)
                    # else:
                    #     runproc = SubProcMgr.ProcItem(SubProcMgr.runnprocs[i])
                    #     endtime = datetime.datetime.now()
                    #     diff = (endtime - runproc.starttime).total_seconds()
                    #     if diff < 600: #10 minutes
                    #         print "running %s" % runproc.mp4
                    #         continue
                    #     else:
                    #         runproc = SubProcMgr.ProcItem(SubProcMgr.runnprocs.remove(i))
                    #         runproc.endtime = endtime
                    #         runproc.durationsec = diff
                    #         runproc.stdout, runproc.stderr = runproc.subproc.communicate()
                    #         SubProcMgr.failprocs.append(runproc)
                except Exception, e: # SubProcMgr.runnprocs[i].returncode should throw error
                    #need to check if stuck process exceed alotted runtime
                    runproc = SubProcMgr.runprocs[i]
                    endtime = datetime.datetime.now()
                    diff = (endtime-runproc.starttime).total_seconds()
                    if diff< SubProcMgr.runmax:
                        print "running %s" % runproc.mp4
                        continue
                    else:
                        runproc = SubProcMgr.runprocs.pop(i)
                        runproc.endtime = endtime
                        runproc.durationsec = diff
                        runproc.stdout, runproc.stderr = runproc.subproc.communicate()
                        if runproc.stderr==None or len(str(runproc.stderr))==0:
                            SubProcMgr.doneprocs.append(runproc)
                        else:
                            SubProcMgr.failprocs.append(runproc)
                            try:
                                runproc.subproc.terminate()
                                print "Failed & Killed %s" % runproc.mp4
                            except:
                                print "Failed & Killed %s" % runproc.mp4

                    #time.sleep(SubProcMgr.rampdelaysecs)
        # self.autorun = SubProcMgr.runevent(SubProcMgr.runevent)
        # self.autorun.start()
        # while not SubProcMgr.stopFlag.wait(0.5):
        #     if(len(self.startprocs)>0):
        #         cpu_percent = round(psutil.cpu_percent(), 1)
        #         if cpu_percent<SubProcMgr.maxcpu:
        #             runproc=SubProcMgr.ProcItem(SubProcMgr.startprocs[0])
        #             cmd = runproc.fullproc
        #             p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)



    class ProcItem:
        #scenedetect --input 30seckillingfloor.mp4 --output 30seckillingfloor_scenes.csv --detector content --threshold 10 --min-percent 50
        def __init__(self, mp4, csv, root=""):
            self.mp4 = mp4
            self.csv = csv
            self.root=root
            self.subproc=None
            self.passfail = False
            self.stdout = ""
            self.stderr = ""
            self.starttime = None
            self.endtime = None
            self.durationsec=-1
            self.fullproc = "scenedetect --input [[MP4]] --output [[CSV]] --detector content --threshold 10 --min-percent 50 --save-images --min-scene-length 5"
            #    #scenedetect --input /Users/keithfisher/Downloads/edits_Mac4926-160916/songSUGARGIRL15.mp4 --output /Users/keithfisher/Downloads/edits_Mac4926-160916/songSUGARGIRL15.csv --detector content --threshold 10 --min-percent 50

            #self.fullproc = "python testmp4.py [[MP4]]"
            mp4=os.path.join(self.root, self.mp4)
            csv=os.path.join(self.root, self.csv)
            
            self.fullproc = self.fullproc.replace("[[MP4]]",mp4).replace("[[CSV]]",csv)

    # class runevent(Thread):
    #     def __init__(self, event):
    #         Thread.__init__(self)
    #         self.stopped = event
    #
    #     def run(self):    `
    #         while not self.stopped.wait(0.5):
    #             print

    class cpu_percent:
        '''Keep track of cpu usage.'''

        def __init__(self):
            self.last = ps.cpu_times()

        def update(self):
            '''CPU usage is specific CPU time passed divided by total CPU time passed.'''

            last = self.last
            current = ps.cpu_times()

            total_time_passed = sum([current.__dict__.get(key, 0) - last.__dict__.get(key, 0) for key in current.attrs])

            #only keeping track of system and user time
            sys_time = current.system - last.system
            usr_time = current.user - last.user

            self.last = current

            if total_time_passed > 0:
                sys_percent = 100 * sys_time / total_time_passed
                usr_percent = 100 * usr_time / total_time_passed
                return sys_percent + usr_percent
            else:
                return 0


# class RepeatedTimer(object):
#     def __init__(self, interval, function, *args, **kwargs):
#         self._timer     = None
#         self.interval   = interval
#         self.function   = function
#         self.args       = args
#         self.kwargs     = kwargs
#         self.is_running = False
#         self.start()
#
#     def _run(self):
#         self.is_running = False
#         self.start()
#         self.function(*self.args, **self.kwargs)
#
#     def start(self):
#         if not self.is_running:
#             self._timer = Timer(self.interval, self._run)
#             self._timer.start()
#             self.is_running = True
#
#     def stop(self):
#         self._timer.cancel()
#         self.is_running = False


def testsubproc():
    print "Start"
    pp=SubProcMgr()
    for i in range(1,100):
        mp3="abc%s" % str(i)
        pp.addproc(mp3,mp3)
        t=0
    ss=""
    while not pp.isjobsdone():
        sleep(5)
        t+=5
        s=len(pp.startprocs)
        r=len(pp.runprocs)
        st=len(pp.doneprocs)
        f=len(pp.failprocs)
        s1= "waiting for jobs s%d:r%d:st%d:f%d" % (s,r,st,f)
        if s1!=ss:
            ss=s1
            print "%d. %s" % (t,ss)
    for s in pp.doneprocs:
        print s.stdout

    print "FAILED==============="
    for s in pp.failprocs:
        print "%s : %s" % (s.mp4,s.stderr)

#testsubproc()