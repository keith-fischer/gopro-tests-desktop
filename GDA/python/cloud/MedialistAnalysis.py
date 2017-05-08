
import utils

class MediaDataAnalysis():
    #client_updated_at|updated_at|captured_at|upload_completed_at|created_at
    # "client_updated_at": "2016-10-24T18:17:57Z",
    # "updated_at": "2016-10-24T18:18:21Z"
    # "captured_at": "2016-10-21T16:53:31Z"
    # "upload_completed_at": "2016-10-22T00:21:35Z"
    # "created_at": "2016-10-22T00:07:38Z"
    # derived items
    #1"updated_at": "2016-10-22T00:21:32Z"
    # "created_at": "2016-10-22T00:21:08Z"
    #2"updated_at": "2016-10-22T00:22:05Z"
    # "created_at": "2016-10-22T00:21:08Z"
    #3"updated_at": "2016-10-22T00:21:55Z"
    # "created_at": "2016-10-22T00:21:08Z"
    #4"updated_at": "2016-10-22T00:21:29Z"
    # "created_at": "2016-10-22T00:21:08Z"
    #5"updated_at": "2016-10-22T00:21:17Z"
    # "created_at": "2016-10-22T00:21:08Z"
    #6"updated_at": "2016-10-22T00:21:56Z"
    # "created_at": "2016-10-22T00:08:11Z"
    #7"updated_at": "2016-10-22T00:20:56Z"
    # "created_at": "2016-10-22T00:21:11Z"
    keys={'client_updated_at'}
    def __init__(self,settings):
        self.utils=utils.Utils()
        if 'jsonpath' not in settings:
            print "Error: No cloud json path"
            return
        if 'dbjsonpath' not in settings:
            print "Error: No sqllitedb json path"
            return

        self.cloud=self.utils.json_load(settings['jsonpath'])
        self.ok=False
        if self.cloud and len(self.cloud)>2:
            self.db = self.utils.json_load(settings['dbjsonpath'])
            if self.db and len(self.db) > 2:
                self.ok = self.analyze()
            else:
                print "Failed to load quik sql db json: %s" % settings['dbjsonpath']
        else:
            print "Failed to load cloud account json: %s" % settings['jsonpath']
            return

    def getderivatives(self,item,field):
        derlist=""
        if field in item:
            for deritem in item[field]:
                if "label" in deritem:
                    derlist+=deritem["label"]+"|"
        return derlist

    def analyze(self):

        medialist=self.cloud['medialist']
        gumi={}
        foundmatch=0
        passed=0
        fail=0
        nomatch=0
        notready=0
        for i in range(0,len(medialist)):
            match={}
            mitem = medialist[i]
            labels=self.getderivatives(mitem,"derivativeList")
            msg="No GUMI"
            if "source_gumi" in mitem:
                id=self.finditembyfieldanddata(self.db,"gumi",mitem["source_gumi"])
                if not id:
                    nomatch+=1
                    fail+=1
                    msg="No GUMI Match"
                    print "%d. %s\t\t%s | status:%s | client:%s | type:%s | composition:%s | derivativelabels:%s" % (i, msg, mitem['filename'], mitem['ready_to_view'], mitem['content_source'], mitem['type'], mitem['composition'],labels)
                    continue
                foundmatch+=1
                match["cloud"]=mitem
                match["db"]=self.db[id]
                gumi[mitem["source_gumi"]]=match
                msg="Found GUMI Match"
                if "ready_to_view" in mitem:
                    if mitem['ready_to_view'] <> "ready":
                        msg="Failed: Found GUMI, but Not Available in Cloud"
                        notready+=1
                        fail+=1
                    else:
                        msg="PASSED"
                        passed+=1
                else:
                    msg = "Failed: Found GUMI, but Not Available in Cloud"
                    notready += 1
                    fail += 1
            print "%d. %s\t\t%s | status:%s | client:%s | type:%s | composition:%s | derivativelabels:%s" % (i,msg,mitem['filename'],mitem['ready_to_view'],mitem['content_source'],mitem['type'],mitem['composition'],labels)
        matchcount= len(gumi)
        print "Matched found=%d" % matchcount
        if matchcount>0:
            self.ok=True
        print "==============================================="
        print "GUMI MATCH COUNT=%d    (count of media in sql db and found in cloud account by gumi)" % matchcount
        print "NO GUMI MATCH COUNT=%d   (count of media in cloud by gumi and NOT found in sql db)" % nomatch
        print "CLOUD MEDIA NOT READY=%d   (count of media in sql db and found in cloud by gumi, but not available as ready in cloud account)" % notready
        print "---------------------------------"
        print "PASSED: %d" % passed
        print "FAILED: %d" % fail
        print "==============================================="
        return self.ok


    def finditembyfieldanddata(self,itemslist,fieldname,flddata):
        for i in range(0,len(itemslist)):
            item=itemslist[i]
            if fieldname in item:
                if item[fieldname]==flddata:
                    return i
        return None



def test_MediaDataAnalysis():
    settings={}

    settings['dbjsonpath'] = "/Users/keithfisher/Downloads/gda_sqlitedb1.json"
    settings['jsonpath']="/Users/keithfisher/Downloads/autogda00_prod1.json"
    md=MediaDataAnalysis(settings)
    if md.ok:
        print "Done"
    else:
        print "Failed"


#test_MediaDataAnalysis()
