
import testrail
import json
import random

class TestRail_API():
    def __init__(self, baseuri, projid, login, passward):
        self.ok=False
        self.baseurl=baseuri
        self.projid=projid
        self.login=login
        self.pw=passward
        self.lastresponse=None
        resp = self.get_runs(self.projid)
        if resp and "response" in resp:
            if len(resp["response"])>0:
                self.ok=True
                self.testruns=resp["response"]


    def sendget(self,client,getrequest):
        self.lastresponse ={}
        try:
            self.lastresponse = client.send_get(getrequest)
            #print(str(case))
            return self.lastresponse
        except Exception, e:
            self.lastresponse["error"]= "%s" % str(e)

        return self.lastresponse

    def sendpost(self,client,postrequest,data):
        self.lastresponse = {}
        try:
            self.lastresponse = client.send_post(postrequest,data)
            #print(str(case))
            return self.lastresponse
        except Exception, e:
            self.lastresponse["error"] = "%s" % str(e)
        return self.lastresponse

    def get_api(self,api,proj_id):
        client = testrail.APIClient(self.baseurl)
        client.user = self.login
        client.password = self.pw
        uri="%s/%d" % (api,proj_id)
        self.lastresponse = self.sendget(client, uri)
        return self.lastresponse

    def get_runs(self,proj_id):
        return self.get_api("get_runs",proj_id)
        # client = testrail.APIClient(self.baseurl)
        # client.user = self.login
        # client.password = self.pw
        # uri="get_runs/%d" % projid
        # self.lastresponse = self.sendget(client, uri)
        # return self.lastresponse

    def get_suites(self,proj_id):
        return self.get_api("get_suites", proj_id)
        # client = testrail.APIClient(self.baseurl)
        # client.user = self.login
        # client.password = self.pw
        # uri="get_suites/%d" % projid
        # self.lastresponse = self.sendget(client, uri)
        # return self.lastresponse

    def delete_run(self,suitid,runid):
        client = testrail.APIClient(self.baseurl)
        client.user = self.login
        client.password = self.pw
        uri="delete_run/%d" % runid  #delete_run/:run_id
        runinfo = {}
        runinfo["suite_id"] = suitid
        response = self.sendpost(client, uri,runinfo)
        return response

    def add_result(self,projectid,testid,testrunid,statusid,comment=None,elapsetime=None,version=None):
        # 1Passed
        # 2Blocked
        # 3Untested(not allowed when adding a result)
        # 4Retest
        # 5Failed
        client = testrail.APIClient(self.baseurl)
        client.user = self.login
        client.password = self.pw
        uri = "add_result/%d" % testid  # delete_run/:run_id
        runinfo = {}
        runinfo["run_id"]=testrunid
        runinfo["status_id"] = statusid
        if comment:
            runinfo["comment"] = comment
        if elapsetime:
            runinfo["elapsed"] = elapsetime
        if version:
            runinfo["version"] = version
        # {
        #     "test_id": 102,
        #     "status_id": 1,
        #     "comment": "This test passed",
        #     "elapsed": "5m",
        #     "version": "1.0 RC1"
        # }
        #runinfo["suite_id"] = suitid
        response = self.sendpost(client, uri, runinfo)
        return response

    def add_run(self,projid, suitid, runname="Automation Quik TestRun", rundescription="",milestoneid=None,assignedto=None):
        client = testrail.APIClient(self.baseurl)
        client.user = self.login
        client.password = self.pw
        uri="add_run/%d" % projid
        #"add_run/[[RUN_ID]]"
        runinfo={}
        runinfo["suite_id"] = suitid
        runinfo["name"] = runname
        runinfo["include_all"] = True
        runinfo["description"] = rundescription
        if milestoneid:
            runinfo["milestone_id"] = milestoneid
        if assignedto:
            runinfo["assignedto_id"] = assignedto
        """
        {
            "suite_id": 1,
            "name": "This is a new test run",
            "assignedto_id": 5,
            "include_all": false,
            "case_ids": [1, 2, 3, 4, 7, 8]
        }
         """
        print "add_run %s/%s %s" % (self.baseurl,uri,str(runinfo))
        response = self.sendpost(client, uri, runinfo)
        if response:
            print str(response)
            return response
        print "Error: response is None"
        return None

    def get_tests(self,projid,runid):
        client = testrail.APIClient(self.baseurl)
        client.user = self.login
        client.password = self.pw

        #client.user = 'kfischer@gopro.com'
        #client.password = 'Qwerty1!'
        #sqaautomation1@gopro.com
        #Bro$toke1!
        #https://testrail.gopro.com/index.php?/api/v2/get_tests/31456
        #data = 'get_case/%d&suite_id=%d' % (projid,suiteid)
        uri = 'get_tests/%d' % runid
        print uri
        response = self.sendget(client, uri)
        if "response" in response:
            print "Found %d test cases" % len(response["response"])
            return response["response"]

    # http://docs.gurock.com/testrail-api2/reference-tests
    def get_test(self, projid, testid):
        client = testrail.APIClient(self.baseurl)
        client.user = self.login
        client.password = self.pw

        # client.user = 'kfischer@gopro.com'
        # client.password = 'Qwerty1!'
        # sqaautomation1@gopro.com
        # Bro$toke1!
        # https://testrail.gopro.com/index.php?/api/v2/get_tests/31456
        # data = 'get_case/%d&suite_id=%d' % (projid,suiteid)
        uri = 'get_test/%d' % testid
        print uri
        response = self.sendget(client, uri)
        if "response" in response:
            print "Found %d test cases" % len(response["response"])
            return response["response"]

    # http: // docs.gurock.com / testrail - api2 / reference - results  # get_results
    def get_results(self, projid, testid):
        client = testrail.APIClient(self.baseurl)
        client.user = self.login
        client.password = self.pw

        # client.user = 'kfischer@gopro.com'
        # client.password = 'Qwerty1!'
        # sqaautomation1@gopro.com
        # Bro$toke1!
        # https://testrail.gopro.com/index.php?/api/v2/get_tests/31456
        # data = 'get_case/%d&suite_id=%d' % (projid,suiteid)
        uri = 'get_results/%d' % testid
        print uri
        response = self.sendget(client, uri)
        if "response" in response:
            print "Found %d test cases" % len(response["response"])
            return response["response"]


#unit test
#tests basic testrail api functions for testrun [create,delete,read]
def test_testrail(newrunname,runcomment):
    projid=86
    suiteid=12922
    sectionid=11
    runid=31456
    login="sqaautomation1@gopro.com"
    pw="Bro$toke1!"
    #url="http://127.0.0.1:8081/testrail/"
    url="https://testrail.gopro.com"
    tr=TestRail_API(url,projid,login,pw)
    deleteruns=["Quik-Mac-2.1.0.5265_osx10.12","Quik-Mac-2.1.0.5265_osx10.12-2","This is a new test run"]
    # testrun=test_testrail(projid,runid)
    # for test in testrun:
    #     print test["title"]
    runlist=tr.get_runs(projid)
    testruninfo = None
    if "response" in runlist:
        for run in runlist["response"]:
            if run["name"] == newrunname:
                testruninfo = run
                continue
            if run["name"] in deleteruns:
                tr.delete_run(suiteid,run["id"])
    if not testruninfo:
        response = tr.add_run(projid,suiteid,newrunname,runcomment)
        if "response" in response:
            testruninfo=response["response"]
    if not testruninfo:
        print "Error: No test run info"
        return
    runid=testruninfo["id"]

    testrun=tr.get_tests(projid,runid)
    rnd=[1,1,1,1,1,5,1,2,4,5,1,1,1,1,1,1,1]
    counter=0
    for test in testrun:
        counter += 1
        print "%d. %s" % (counter,test["title"])
        statusid=rnd[random.randrange(0,len(rnd),1)]
        comment="%d. Automation status=%d" % (counter,statusid)
        tr.add_result(projid,test["id"],test["run_id"],statusid,comment)


#test_testrail("newsonganalysistest_Mac-210.5300","release candidate2")