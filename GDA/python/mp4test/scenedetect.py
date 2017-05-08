#!/usr/bin/env python

import sys
import subprocessmgr
import os
from time import sleep

# http://pyscenedetect.readthedocs.io/en/latest/

#
#         PySceneDetect: Python-Based Video Scene Detector
#   ---------------------------------------------------------------
#     [  Site: http://www.bcastell.com/projects/pyscenedetect/   ]
#     [  Github: https://github.com/Breakthrough/PySceneDetect/  ]
#     [  Documentation: http://pyscenedetect.readthedocs.org/    ]
#
# This is a convenience/backwards-compatibility script, and simply provides an
# alternative to running PySceneDetect from source (in addition to the standard
# python -m scenedetect).
#
# Copyright (C) 2012-2016 Brandon Castellano <http://www.bcastell.com>.
#
# PySceneDetect is licensed under the BSD 2-Clause License; see the
# included LICENSE file or visit one of the following pages for details:
#  - http://www.bcastell.com/projects/pyscenedetect/
#  - https://github.com/Breakthrough/PySceneDetect/
#
# This software uses Numpy and OpenCV; see the LICENSE-NUMPY and
# LICENSE-OPENCV files or visit one of above URLs for details.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

# Scene detection details
# SEE class ProcItem in subprocessmgr.py:

# usage: scenedetect.py [-h] [-v] -i VIDEO_FILE [-o SCENE_LIST] [-t intensity]
#                       [-m num_frames] [-p percent] [-b rows] [-s STATS_FILE]
#                       [-d detection_method] [-l] [-q] [-st time] [-dt time]
#                       [-et time] [-df factor] [-fs num_frames] [-si]
#
# arguments:
#   -h, --help            show this help message and exit
#   -v, --version         show version number and license/copyright information
#   -i VIDEO_FILE, --input VIDEO_FILE
#                         [REQUIRED] Path to input video. (default: None)
#   -o SCENE_LIST, --output SCENE_LIST
#                         File to store detected scenes in using the specified
#                         timecodeformat as comma-separated values (.csv). File
#                         will be overwritten if already exists. (default: None)
#   -t intensity, --threshold intensity
#                         8-bit intensity value, from 0-255, to use as the black
#                         level in threshold detection mode, or as the change
#                         tolerance threshold in content-aware detection mode.
#                         (default: 12)
#   -m num_frames, --min-scene-length num_frames
#                         Minimum length, in frames, before another scene cut
#                         can be generated. (default: 15)
#   -p percent, --min-percent percent
#                         Amount of pixels in a frame, from 0-100%, that must
#                         fall under [intensity]. Only applies to threshold
#                         detection. (default: 95)
#   -b rows, --block-size rows
#                         Number of rows in frame to check at once, can be tuned
#                         for performance. Only applies to threshold detection.
#                         (default: 32)
#   -s STATS_FILE, --statsfile STATS_FILE
#                         File to store video statistics data, comma-separated
#                         value format (.csv). Will be overwritten if exists.
#                         (default: None)
#   -d detection_method, --detector detection_method
#                         Type of scene detection method/algorithm to use;
#                         detectors available: [threshold, content]. (default:
#                         threshold)
#   -l, --list-scenes     Output the final scene list in human-readable format
#                         as a table, in addition to CSV. (default: False)
#   -q, --quiet           Suppress all output except for final comma-separated
#                         list of scene cuts. Useful for computing or piping
#                         output directly into other programs/scripts. (default:
#                         False)
#   -st time, --start-time time
#                         Time to seek to in video before performing detection.
#                         Can be given in number of frames (12345), seconds
#                         (number followed by s, e.g. 123s or 123.45s), or
#                         timecode (HH:MM:SS[.nnn]). (default: None)
#   -dt time, --duration time
#                         Time to limit scene detection to (see -st for time
#                         format). Overrides -et. (default: None)
#   -et time, --end-time time
#                         Time to stop scene detection at (see -st for time
#                         format). (default: None)
#   -df factor, --downscale-factor factor
#                         Factor to downscale (shrink) image before processing,
#                         to improve performance. For example, if input video
#                         resolution is 1024 x 400, and factor = 2, each frame
#                         is reduced to 1024/2 x 400/2 = 512 x 200 before
#                         processing. (default: 1)
#   -fs num_frames, --frame-skip num_frames
#                         Number of frames to skip after processing a given
#                         frame. Improves performance at expense of frame
#                         accuracy, and may increase probability of inaccurate
#                         scene cut prediction. If required, values above 1 or 2
#                         are not recommended. (default: 0)
#   -si, --save-images    If set, the first and last frames in each detected
#                         scene will be saved to disk. Images will saved in the
#                         current working directory, using the same filename as
#                         the input but with the scene and frame numbers
#                         appended. (default: False)


def processscenedetect():
    #folder path with all the mp4 files
    rootdir="/Users/keithfisher/Downloads/editsgda_music_images-Songs_Regression_osx1011-i73Ghz16GB-Quik210_5429-HOT-FIX"
    #scenedetect --input /Users/keithfisher/Downloads/edits_Mac4926-160916/songSUGARGIRL15.mp4 --output /Users/keithfisher/Downloads/edits_Mac4926-160916/songSUGARGIRL15.csv --detector content --threshold 10 --min-percent 50

    pp=subprocessmgr.SubProcMgr()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            jpath = os.path.join(subdir, file)
            filename, file_extension = os.path.splitext(file)
            if file_extension == ".mp4":
                csv="%s.csv" % filename
                if not os.path.exists(os.path.join(subdir, csv)):
                    mp3=str(file)
                    #dir=os.path.join(subdir, "")
                    pp.addproc(mp3, csv, subdir)
                else:
                    print "SKIPPING: %s" % csv
    ss = ""
    t=0
    donecount=len(pp.startprocs)
    testrailreport=[]
    while not pp.isjobsdone():
        sleep(5)
        t += 5
        s = len(pp.startprocs)
        r = len(pp.runprocs)
        st = len(pp.doneprocs)
        for p in pp.doneprocs:
            #print str(p)
            s1 = p.csv.replace(".csv","")
            s1 = "%s - MP4 Edits Scene Detect" % s1
            if p.passfail:
                pf = "PASSED: %s" % s1
            else:
                pf = "FAILED: %s" % s1
            if pf not in testrailreport:
                print pf
                testrailreport.append(pf)
        f = len(pp.failprocs)
        if st==donecount:
            break
        s1 = "waiting for jobs s%d:r%d:st%d:f%d" % (s, r, st, f)
        if s1 != ss:
            ss = s1
            print "%d. %s" % (t, ss)
    for s in pp.doneprocs:
        print s.stdout
    if len(pp.failprocs)>0:
        print "FAILED==============="
        for s in pp.failprocs:
            print "%s : %s" % (s.mp4, s.stderr)
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
def main(argv):
    p = processscenedetect()
    print

if __name__ == "__main__":
    main(sys.argv[1:])

