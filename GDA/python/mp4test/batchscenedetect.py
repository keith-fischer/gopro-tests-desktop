import psutil
import os
import psutil as ps
import time

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
############################################
# BATCH SCENE DETECT PROCESSOR
# 1. Iterate song json
#	a. Process args
#	b. get
# 2. Generate song scenes 15,30,60 from exported mp4's
# 3. Validate scene start times with song beats mark timings
# 4. Generate report
############################################
for proc in psutil.process_iter():
    try:
        #print(proc.name())
        if "python" in proc.name().lower():
            #print(proc)
            #print(proc.cmdline())
            if "batchscenedetect.py" in str(proc.cmdline()).lower():
                continue
            if "scenedetect" in str(proc.cmdline()).lower():
                print(proc.cmdline())
                p_dict = proc.as_dict()
                print(str(p_dict))
                print round(psutil.cpu_percent(), 1)
                #print(proc.pid())
                #proc.terminate()
                #print(str(proc))
                #os.kill(proc.pid(), signal.SIGKILL)
    #except psutil.AccessDenied:
    #    continue #print "Permission error or access denied on process"
    except:
        continue

