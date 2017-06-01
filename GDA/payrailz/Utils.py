import sys
import subprocessmgr
import os
from time import sleep
import datetime
import logging
import csv
import json
import platform
from os.path import expanduser

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

class Utils:
    def __init__(self):
        logging.INFO("init Utils")

    ################################
    # json_load
    # validates file exists
    # return json dict or None
    ################################
    def json_load(self, jpath):
        if not os.path.isfile(jpath):
            logging.INFO("Failed to load json, invalid path:%s" % jpath)
            return None
        try:
            with open(jpath, 'r') as f:
                mj = json.load(f)
                return mj
        except Exception, e:
            logging.ERROR("json_load: Exception")
            logging.ERROR(str(e))
        return None

    ################################
    # json_save
    # validates file output
    # return True or False success
    ################################
    def json_save(self,jpath,jdata):
        rc=False
        # Writing JSON data
        try:
            with open(jpath, 'w') as f:
                json.dump(jdata, f, indent=4)
                f.close()
            if not os.path.isfile(jpath):
                logging.INFO("Failed to write json:%s" % jpath)
            else:
                rc=True
        except Exception, e:
            logging.ERROR("json_save: Exception")
            logging.ERROR(str(e))
        return rc


