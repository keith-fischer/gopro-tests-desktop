################################################
#
# F O R  S I K U L I
# This file should always be in synch to 
# "gopro-tests-desktop/GDA/python/testrail/client_testrail_test.py"
# "gopro-tests-desktop/GDA/sikuli/testrail.sikuli"
#
################################################

#import sys
#import os
import json
#import httplib
#import urllib
import urllib2
#from __builtin__ import True, False
#from java.net import URL


############################################################################
# TestRailClient: simple testrail class manager for easy straightforward impleamentation of test case status
# find testrun and create if not exists from derived testsuite name
# All is referenced by first found name when fetching data from testrail
# params:
# run_name: the test run to fetch the testcase list
# suite_name: The testsuite to derive creating the testruns
# run_mode: when iterrating the testrun list, determinds if passed tests are skipped
# [run_non-passed,run_all,run_retest,run_failed,None] testrail supports: Passed=1,Failed=5,Blocked=,Retest=
# baseuri: the middleware webservice restservertestrail.py normally run local: http://127.0.0.1:8081/testrail
############################################################################
class TestRailClient():
    ###################################
    # default loads appropriate testrun or create new testrun if run_mode is NOT None
    # run_mode="run_non-passed"
    ######################################
    #
    #
    #
    ######################################
    def __init__(self,
                 run_name="Testrun_Quik_Music_Story_Output_Regression",
                 suite_name="Quik_Music_Story_Output_Regression",
                 run_description="",
                 run_mode="run_non-passed",
                 baseuri="http://127.0.0.1:8081/testrail",
                 proj_id=86):
        print "testrail.TestRailClient.__init__ >>>>>>>>>>>>>>>>>>>"
        self.ok = False
        self.run_name = run_name
        self.run_description = run_description
        self.suite_name = suite_name
        self.run_mode = run_mode
        self.baseuri = baseuri
        self.projid = proj_id
        self.suitelist = []
        self.suite = None
        self.suite_id = None
        self.testrun = None
        self.testrunlist = []
        self.testcases = []
        if self.run_mode:
            self.ok = self.testrun_init()
        else:
            self.ok = True
        print "testrail.TestRailClient.__init__ <<<<<<<<<<<<<<<<<<<<<"
    ###################################
    # default loads appropriate testrun or create new testrun if run_mode is NOT None
    ######################################
    #
    #
    #
    ######################################
    def testrun_init(self):
        print "testrail.TestRailClient.testrun_init >>>>>>>>>>>>>>>>>>>"
        rc = False
        # load test run if found or create new testrun with run_name from suite_name
        truns = self.getruns()
        if not truns:
            print "ERROR: TestRailClient.testrun_init"
            print "testrail.TestRailClient.testrun_init ERROR <<<<<<<<<<"
            return rc
        self.testrun = None
        for i in range(0, len(truns["response"]["response"])):
            tname = truns["response"]["response"][i]["name"]
            if self.run_name == tname:
                self.testrun = truns["response"]["response"][i]
                break
        if not self.testrun:
            print "Test run not found: %s" % self.run_name
            # to do create new testrun
            if not self.gettestsuite(self.suite_name):
                print "testrail.TestRailClient.testrun_init ERROR gettestsuite <<<<<<<<<<"
                return rc

            print "Create Testrun"
            tr = self.addrun()
            if "response" in tr and "response" in tr["response"]:
                self.testrun = tr["response"]["response"]
            else:
                print "Error: Testrun not created"
                print str(tr)
        self.testcases = None

        if self.testrun and "id" in self.testrun:
            tests = self.gettests(int(self.testrun["id"]))
            if tests and "response" in tests:
                self.testcases = tests["response"]
            if self.testcases and len(self.testcases) > 0:
                print "testrail.TestRailClient.testrun_init OK ,Found testcount=%d <<<<<<<<<<" % len(self.testcases)
                return True
            else:
                print "testrail.TestRailClient.testrun_init testcases not found"
        print "testrail.TestRailClient.testrun_init <<<<<<<<<<"
        return rc

    ######################################
    # Only does a local search in self.testcases
    # call get_tests to refresh the list
    #
    ######################################
    def find_test_name(self, testname):
        if self.testcases and len(self.testcases) > 0:
            for test in self.testcases:
                if test["title"] == testname:
                    return test
        return None

    ######################################
    # Only does a local search in self.testcases
    # call get_tests to refresh the list
    #
    ######################################
    def find_all_test_contains_name(self, testname):
        testlist=[]
        if self.testcases and len(self.testcases) > 0:
            for test in self.testcases:
                if testname in str(test["title"]):
                    testlist.append(test)
        return testlist
    ####################################################
    # gettestrun(self,run_name)
    # get the test run list from the project and returns the
    # matching testrun name of the testrun item in list
    # rreturn None not found
    ####################################################
    def gettestrun(self, run_name):
        runs = self.getruns()
        if "response" in runs:
            if "response" in runs and "response" in runs["response"]:
                for run_item in runs["response"]["response"]:
                    if run_item['name'] == run_name:
                        return run_item
        return None

    ######################################
    # finds existing test suite for creating test run when calling add_run
    # add_run uses self.suite_id to create the new test run
    #
    ######################################
    def gettestsuite(self, suite_name):
        print "testrail.TestRailClient.gettestsuite >>>>>>>>>>>>>>>>>>>"
        msuites = self.getsuites()
        print "msuites---------------"
        print str(msuites)
        print "msuites---------------"
        if msuites and "response" in msuites and "response" in msuites["response"]:
            for suiteitem in msuites["response"]["response"]:
                print str(suiteitem)
                if suiteitem["name"] == suite_name:
                    self.suite = suiteitem
                    self.suite_id = int(suiteitem["id"])
                    print "testrail.TestRailClient.gettestsuite Found %s <<<<<<<<<<<<<<<<<<" % self.suite
                    return True
        print "testrail.TestRailClient.gettestsuite Not Found <<<<<<<<<<<<<<<<<<"
        return False

    ######################################
    #
    #
    #
    ######################################
    def request(self, data):
        req = urllib2.Request(self.baseuri)
        req.add_header('Content-Type', 'application/json')
        try:
            response = urllib2.urlopen(req, json.dumps(data))
            if response:
                return json.loads(response.read())
        except Exception as e:
            print str(e)

        return None

    ######################################
    #
    #
    #
    ######################################
    def getruns(self):
        data = {}
        data["testrail"] = "testrail"
        data["api"] = "get_runs"
        data["projid"] = self.projid
        return self.request(data)

    ######################################
    #
    #
    #
    ######################################
    def getsuites(self):
        data = {}
        data["testrail"] = "testrail"
        data["api"] = "get_suites"
        data["projid"] = self.projid
        return self.request(data)

    ######################################
    #
    #
    #
    ######################################
    def gettest(self,testid):
        data = {}
        data["testrail"] = "testrail"
        data["api"] = "get_test"
        data["testid"] = testid
        data["projid"] = self.projid
        return self.request(data)

    ######################################
    #
    #
    #
    ######################################
    def getresults(self,testid):
        data = {}
        data["testrail"] = "testrail"
        data["api"] = "get_results"
        data["testid"] = testid
        data["projid"] = self.projid
        return self.request(data)

    ######################################
    #
    #
    #
    ######################################
    def get_tests(self):
        if self.testrun and "id" in self.testrun:
            tc = self.gettests(self.testrun)
            if tc and "response" in tc and "response" in tc["response"]:
                self.testcases = tc["response"]["response"]
                return True
        return False

    def get_test(self,test_id):
        self.test=None
        tc = self.gettest(self.testrun)
        if tc and "response" in tc and "response" in tc["response"]:
            self.test = tc["response"]["response"]
            return self.test
        return None
    ######################################
    #
    #
    #
    ######################################
    def gettests(self, testrunid):
        data = {}
        data["testrail"] = "testrail"
        data["api"] = "get_tests"
        data["projid"] = self.projid
        data["testrunid"] = testrunid
        return self.request(data)

    ######################################
    #
    #
    #
    ######################################
    def addrun(self):
        print "testrail.TestRailClient.addrun >>>>>>>>>>>>"
        data = {}
        if self.suite_id and self.suite_id>0:
            data["testrail"] = "testrail"
            data["api"] = "add_run"
            data["projid"] = self.projid
            data["suite_id"] = self.suite_id
            data["run_name"] = self.run_name
            data["description"] = self.run_description
            print str(data)
            print "testrail.TestRailClient.addrun <<<<<<<<<<<<<<<"
            return self.request(data)
        else:
            e="Invalid self.suite_id"
            print e
            data["error"]=e
            return data

    ######################################
    #
    #
    #
    ######################################
    def setteststatus(self, passfail, testitem, run_id, elapsed=None, comment=None, version=None, defects=None, assignedto_id=None):
        if not passfail or not testitem or not run_id:
            print "Error in setstatus:Invalid parameters passfail or testitem or run_id is None"
        status_id = -1
        if passfail == "passed":
            status_id = 1
        elif passfail == "failed":
            status_id = 5
        elif passfail == "blocked":
            status_id = 2
        elif passfail == "retest":
            status_id = 4
        elif passfail == "untested":
            status_id = 3
        if status_id < 1:
            print "Error in setstatus: Invalid Status_id: %s" % passfail
            return None
        data = {}
        data["api"] = "add_result"
        data["testrail"] = "testrail"
        data["projid"] = self.projid
        data["status_id"] = status_id
        if testitem:
            data["testid"] = testitem
        else:
            print "Error in setstatus: missing test id field: %s" % str(testitem)
            return None
        if run_id:
            data["runid"] = run_id
        else:
            print "Error in setstatus: missing run id field: %s" % str(run_id)
            return None

        if elapsed:
            data["elapsed"] = elapsed

        if comment:
            data["comment"] = comment

        if version:
            data["version"] = version

        if defects:  # must comma seperated list
            data["defects"] = defects

        if assignedto_id:
            data["assignedto_id"] = assignedto_id

        return self.request(data)


# this works
######################################
#
#
#
######################################
def test_testclient2():
    projid = 86
    login = ""
    pw = ""
    baseuri = "http://127.0.0.1:8081/testrail"
    testrail = TestRailClient(baseuri, projid, login, pw)
    jruns = testrail.getruns()
    if jruns:
        print str(jruns)
        # jruns=json.loads(runs)
        if "response" in jruns and "response" in jruns["response"]:

            for r in jruns["response"]["response"]:
                print r['name'] + str(r)
                id = int(r['id'])
                print id
                resp = testrail.gettests(id)
                # print str(resp)
                if "response" in resp:
                    for test in resp["response"]:
                        print test["title"]
        elif "response" in jruns and "error" in jruns["response"]:
            print "Response with error: %s" % jruns["response"]["error"]
        elif "error" in jruns:
            print "Error:%s" % str(jruns)
        else:
            print str(jruns)


######################################
#
#
#
######################################
def test_testclient():
    run_name = "Testrun_Quik_Music_Story_Output_Regression2"
    suite_name = "Quik_Music_Story_Output_Regression"
    run_description = "QA test iteration 2"
    run_mode = "run_non-passed"
    baseuri = "http://127.0.0.1:8081/testrail"
    proj_id = 86

    tr = TestRailClient(run_name, suite_name, run_description, run_mode, baseuri, proj_id)
    if tr and tr.ok:
        print "Tests Found=%d" % (len(tr.testcases))
        for test in tr.testcases:
            print test["title"]
            teststatus = tr.setteststatus("passed", test["id"], test["run_id"], "2s", "debug test")
            print str(teststatus)

    else:
        print "Failed testrail init"

# test_testclient()
