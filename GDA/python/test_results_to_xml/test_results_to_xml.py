#!/usr/bin/python

import os
import re
import sys
import cgi
import plistlib
from datetime import datetime


def main():
    logfileName = None
    logfile = None
    log = None

    # check commandline args
    if len(sys.argv) < 2:
        print "Usage: %s <*_TestSummaries.plist path> [console output log path]" % sys.argv[0]
        sys.exit(1)
    else:
        filename = sys.argv[1]

    if len(sys.argv) > 2:
        logfileName = sys.argv[2]

    if not os.path.isfile(filename):
        print "%s: summary file %s not found" % (sys.argv[0], filename)
        sys.exit(1)


    testReport = plistlib.readPlist(filename)
    if logfileName is not None:
        if os.path.isfile(logfileName):
            logfile = open(logfileName, "r")
            log = logfile.read()
        else:
            print "%s: Logfile %s not found" % (sys.argv[0], logfileName)
            sys.exit(1)

    runDestination = testReport["RunDestination"]
    targetDev = runDestination["TargetDevice"]
    targetSDK = runDestination["TargetSDK"]

    properties = {
        "targetName": targetDev["Name"],
        "targetArch": targetDev["NativeArchitecture"],
        "targetModelCode": targetDev["ModelCode"],
        "targetModelName": targetDev["ModelName"],
        "targetId": targetDev["Identifier"],
        "targetOSVersion": targetDev["OperatingSystemVersion"],
        "targetOSBuild": targetDev["OperatingSystemVersionWithBuildNumber"],
        "targetSDK": targetSDK["Identifier"],
        "targetSDKName": targetSDK["Name"]
    }

    testSummaries = testReport["TestableSummaries"]
    print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    print "<testsuites>"
    for summary in testSummaries:
        testSuites = summary["Tests"][0]["Subtests"][0]["Subtests"]
        for testSuite in testSuites:
            testSuiteName = testSuite["TestName"]
            testSuiteTests = testSuite["Subtests"]
            regex = re.compile("^Test Suite '%s' started at ([^ \t\r\n]+ [^ \t\r\n]+)\.[0-9]{3}" % testSuiteName, re.MULTILINE)
            ret = regex.search(log)

            if ret is not None:
                stimestamp = ret.groups()[0]
                startDate = datetime.strptime(stimestamp, "%Y-%m-%d %H:%M:%S")
                stimestamp = stimestamp.replace(" ", "T")

            else:
                stimestamp = ""
                startDate = ""

            regex = re.compile("^Test Suite '%s' (passed|failed) at ([^ \t\r\n]+ [^ \t\r\n]+)\.[0-9]{3}" % testSuiteName, re.MULTILINE)
            ret = regex.search(log)

            if ret is not None:
                etimestamp = ret.groups()[1]
            else:
                etimestamp = ""

            endDate = datetime.strptime(etimestamp, "%Y-%m-%d %H:%M:%S")

            elapsedTime = (endDate - startDate).total_seconds()

            numFailures = 0
            for testCase in testSuiteTests:
                if testCase["TestStatus"] != "Success":
                    numFailures += 1

            print "\t<testsuite name=\"%s\" tests=\"%d\" failures=\"%d\" errors=\"0\" skipped=\"0\" time=\"%d\" timestamp=\"%s\">" % (testSuiteName, len(testSuiteTests), numFailures, elapsedTime, stimestamp)
            print "\t\t<properties>"
            for prop in properties:
                print "\t\t\t<property name=\"%s\" value=\"%s\"/>" % (prop, cgi.escape(properties[prop], True))
            print "\t\t</properties>"

            for testCase in testSuite["Subtests"]:
                testCaseName = testCase["TestName"]
                testId = testCase["TestIdentifier"]
                testFailed = testCase["TestStatus"] == "Failure"
                regex = re.compile("^Test Case [^ ]+ %s.. (passed|failed) \(([0-9.]+) seconds\)[^\n]+\n" % testCaseName, re.MULTILINE)
                ret = regex.search(log)
                if ret is not None:
                    tcTime = ret.groups()[1]
                else:
                    tcTime = 0

                if testFailed:
                    regex = re.compile("(Test Case [^ ]+ %s.. started.*?%s.. failed[^\n]+)\n" % (testCaseName, testCaseName), re.DOTALL)
                    ret = regex.search(log)
                    if ret is not None:
                        testFailureLog = ret.groups()[0]
                    else:
                        testFailureLog = "N/A"

                    regex = re.compile(" (Error:[^\n]+)\n")
                    ret = regex.search(testFailureLog)
                    if ret is not None:
                        testFailureError = ret.groups()[0]
                    else:
                        testFailureError = "N/A"

                    print "\t\t<testcase classname=\"%s\" name=\"%s\" time=\"%s\">" % (testId.replace("/", "."), testCaseName, tcTime)
                    failures = testCase["FailureSummaries"]
                    failMessage = ""
                    for failure in failures:
                        failMessage = failMessage + failure["Message"]


                    print "\t\t\t<failure message=\"fail\">%s</failure>" % cgi.escape(failMessage, True)
                    # TODO: query following from logs
                    print "\t\t\t<system-out><![CDATA[%s]]></system-out>" % testFailureLog
                    print "\t\t\t<system-err><![CDATA[%s]]></system-err>" % testFailureError
                    print "\t\t</testcase>"
                else:
                    print "\t\t<testcase classname=\"%s\" name=\"%s\" time=\"%s\"/>" % (testId.replace("/", "."), testCaseName, tcTime)
            print "\t</testsuite>"
    print "</testsuites>"

if (__name__ == "__main__"):
    main()
