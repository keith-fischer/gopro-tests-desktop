
import os, sys
import hashlib
from shutil import copyfile


# --------------------------------------------------------------------------
# copy rebase mode always overwrites the dstpath files
# compare mode matches the srcpath files with the dstpath SHA files
# --------------------------------------------------------------------------
class MusicChangeTests():
    def __init__(self, mode, srcpath, dstpath):
        self.source_path = srcpath
        self.target_path = dstpath
        if mode == "rebase":
            self.ok = self.processcopy()
        elif mode == "compare":
            self.ok = self.compareMusicCatalog()


    def compareMusicCatalog(self):
        rc = False
        faillist = []
        for subdir, dirs, files in os.walk(self.source_path):
            for file in files:
                src = os.path.join(subdir, file)
                filename, file_extension = os.path.splitext(file)
                dst = os.path.join(self.target_path, filename.upper()+file_extension)
                if file_extension == ".json" or file_extension == ".mp3":
                    SHAa = self.getSHA(src)
                    SHApath = os.path.join(self.target_path,os.path.basename(self.make_SHA_file_name(src)).upper())

                    SHAb = self.readfile(SHApath)
                    if SHAa == SHAb:
                        print "PASSED: %s -  %s" % (filename, SHAa)
                    else:
                        print "FAILED: %s - %s:%s" % (filename, SHAa,SHAb)
                        faillist.append(src)
                        faillist.append(SHAa)
                        faillist.append(SHApath)
                        faillist.append(SHAb)

                else:
                    continue
                print dst
        if len(faillist) > 0:
            for item in faillist:
                print item
        else:
            rc = True
        return rc

    def hash_file(self,filename):
        """"This function returns the SHA-1 hash
        of the file passed into it"""

        # make a hash object
        h = hashlib.sha1()

        # open file for reading in binary mode
        with open(filename, 'rb') as file:
            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                h.update(chunk)

        # return the hex representation of digest
        return h.hexdigest()

    def make_sha_file_name(self,fpath):
        fname = os.path.basename(fpath)
        filename, file_extension = os.path.splitext(fname)
        fdir= os.path.dirname(fpath)
        SHAile = os.path.join(fdir, (filename+".sha"))
        return SHAile

    def getSHA(self,fpath):
        #return hashlib.SHA(fpath).hexdigest()
        return self.hash_file(fpath)

    def readfile(self,path):
        data = None
        with open(path, "r") as text_file:
            data = text_file.read()
        return data

    def savefile(self, path, data):
        with open(path, "w") as text_file:
            text_file.write(data)
            if os.path.isfile(path):
                return True
            else:
                return False

    def processSHAfile(self,fpath):
        SHA = self.getSHA(fpath)
        SHAfile = self.make_SHA_file_name(fpath)
        print "%s - %s" % (os.path.basename(SHAfile), SHA)
        self.savefile(SHAfile, SHAa)

    def processcopy(self):
        rc = False
        filelist = []
        for subdir, dirs, files in os.walk(self.source_path):
            for file in files:
                src = os.path.join(subdir, file)
                filename, file_extension = os.path.splitext(file)
                dst = os.path.join(self.target_path, filename.upper()+file_extension)
                if file_extension == ".json":
                    copyfile(src, dst)
                elif file_extension == ".mp3":
                    copyfile(src, dst)
                else:
                    continue
                print dst
                filelist.append(dst)
        count = 0
        for fpath in filelist:
            if not os.path.isfile(fpath):
                count += 1
                print "%d NOT FOUND %s" % (count, fpath)
            else:
                self.processSHAfile(fpath)

        if count == 0:
            rc = True
        return rc



# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
def main(mode,src, dst):
    if not src:
        src = "/Users/keithfisher/Library/Application Support/com.GoPro.goproapp.GoProMusicService/Music"
    if not dst:
        dst = "/Automation/gopro-tests-desktop/GDA/Quik_Music"
    cm = MusicChangeTests(mode, src, dst)
    if cm.ok:
        print "Done"
    else:
        print "Incomplete"

try:
    if __name__ == "__main__":
       main(sys.argv[1], sys.argv[2], sys.argv[3])

except:
    print "Need params of the source and destination directories"

