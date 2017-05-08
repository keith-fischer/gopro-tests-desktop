import sqlite3
import os
import utils

class GDA_SQLLiteReader():
    def __init__(self, settings):#,dbpath=None,jpath=None):
        self.settings=settings

        if 'mediadbpath' not in self.settings:
            print "missing media db path"
            return

        if 'dbjsonpath' not in self.settings:
            print "missing output json media db path"
            return

        self.mediadata=[]
        self.ok=False
        self.tbls={"media":"media","mediaupload":"media_uploaded","media_derives":"media_derivatives"}
        self.cols={"createdate":"creation_date",}
        if not os.path.exists(self.settings['mediadbpath']):
            print "Error: Invalid db path: %s" % self.settings['mediadbpath']
            return
        self.conn = sqlite3.connect(self.settings['mediadbpath'])
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM {tn}'. format(tn=self.tbls["media"]))
        #self.cursor.execute('SELECT * FROM {tn} WHERE {cn}={dn}'.format(tn=self.tbls["media"], cn=self.cols["createdate"], dc="dog"))
        self.mediarows=self.cursor.fetchall()
        self.media_id={}
        self.media_names = list(map(lambda x: x[0], self.cursor.description))
        mediaididx=self.media_names.index("media_id")
        mediafilenameidx=self.media_names.index("filename")
        for i in range(0,len(self.mediarows)):
            media={}
            for ii in range(0,len(self.mediarows[i])):
                media[self.media_names[ii]]=self.mediarows[i][ii]
            row=self.mediarows[i]
            medid=row[mediaididx]
            drows,dnames=self.getderivatives(medid)
            uprows,upnames=self.getmediauploadstatus(medid)
            id=upnames.index("upload_status")
            media["upload_status"]=None
            if len(uprows)>0:
                media["upload_status"]=uprows[0][id]
            fname=row[mediafilenameidx]
            derives=""
            derivatives=[]
            if drows:
                for ii in range(0,len(drows)):

                    derive={}
                    for iii in range(0,len(drows[ii])):
                        derive[dnames[iii]]=drows[ii][iii]
                        d = "%s:%s," % (dnames[iii],drows[ii][iii])
                        derives+=d
                    derivatives.append(derive)
            print "%d %s %s" % (i,fname,derives)
            media["derivatives"]=derivatives
            self.mediadata.append(media)
        self.conn.close()
        ut=utils.Utils()
        ut.json_save(self.settings['dbjsonpath'],self.mediadata)
    def getmediauploadstatus(self,mediaid):
        c=self.conn.cursor()
        c.execute('SELECT * FROM {tn} WHERE {cn}={dn}'.format(tn=self.tbls["mediaupload"],cn="media_id",dn=mediaid))
        row=c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        return row,names
    def getderivatives(self,mediaid):
        c=self.conn.cursor()
        c.execute('SELECT * FROM {tn} WHERE {cn}={dn}'.format(tn=self.tbls["media_derives"],cn="media_id",dn=mediaid))
        row=c.fetchall()
        names = list(map(lambda x: x[0], c.description))
        return row,names

def testsqlreader():
    settings={}
    settings['mediadbpath']="/Users/keithfisher/Library/Application Support/com.GoPro.goproapp.GoProMediaService/Databases/media.db"
    #db="/Users/keithfisher/Library/Application Support/com.GoPro.goproapp.GoProMediaService/Databases/media.db"
    settings['dbjsonpath']="/Users/keithfisher/Downloads/gda_sqlitedb.json"
    sqllt=GDA_SQLLiteReader(settings)


#testsqlreader()