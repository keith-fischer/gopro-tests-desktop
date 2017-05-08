import os
import sys
import platform
from os.path import expanduser
import json
import re
# --------------------------------------------------------------------------
class pyprofiler:
    def __init__(self):
        self.rootdir="/Automation/gopro-tests-desktop/GDA/"
        self.filelist = {}
    def find_py_files(self):
        rootdir = self.rootdir

        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(subdir, file)
                    print path
                    fb = os.path.basename(file)
                    nf = {}
                    nf['file'] = fb
                    nf['dir'] = subdir
                    if not fb in self.filelist:
                        self.filelist[fb] = []

                    py=self.readpy(path)
                    py2=re.split(r"(def |class |\tdef |  def |\n)",py)
                    #py2=py.split('[\ndef ][\nclass ]')
                    nf['py']=py2
                    mod_fn, mclass = self.evalpy(py2)
                    nf['class']={}
                    nf['class']['class '+mclass]={}
                    nf['mod_def']=mod_fn

                    self.filelist[fb].append(nf)


        print str(self.filelist)

    def evalpy(self,py):
        mod_fn={}
        mclass={}
        mod_fn={}
        for i in range(0,len(py)):
            line=py[i]

            if line=="class ":
                line2 = py[i + 1]
                mclass["class "+line2]
            if line == "def ":
                line2 = py[i + 1]
                mclass["def " + line2]

        return mod_fn,mclass
    def readpy(self,path):
        with open(path, 'r') as pyfile:
            data = pyfile.read()
        return data

pp=pyprofiler()
pp.find_py_files()
