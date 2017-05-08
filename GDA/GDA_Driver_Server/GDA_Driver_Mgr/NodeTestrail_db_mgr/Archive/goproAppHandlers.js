/**
 * Created by keithfisher on 4/18/14.
 */




var TestRail = require("./../TestRail");
var logger = require('./../logger');
var log=logger.LOG;
var utils = require('./../Utils');
//var testrail=new TestRail();

var GoPro_TestMgr = {
    GP_Test_ID: -1,
    GP_TestRunID: 0,
    GP_Done: false,
    GP_RetryCount: 0,
    GP_TestStepCount: 0,
    GP_CAMERA: "BAWA",
    GP_CurrentTestName: "Test_GeneralSettings_BAWA_NTSC_NoProtune",
    GP_TextQualifier1: "Test_",
    GP_TextQualifier2: "All_",
    GP_TextQualifier3: "_",
    GP_ReportPath: "/Automation/ios/TestResults/Node/TestResults_ios",
    GP_ErrorMsg: "",
    GP_TestProperties: [],
    GP_TestRuns: [],
    Testrail : {},
    /*    TestTest: function (post) {
     this.Test_ID++;
     return this.Test_ID + "TestTest" + post;
     },*/
    GP_Init: function(){
        this.Reset();
        this.ReportTestList();

    },
    GP_EvalCameraName: function(CameraName){
        var camname = CameraName.toUpperCase();
        var rc = false;
        if(camname === "BAWA")
            rc=true;
        else if(camname === "ULUWATU")
            rc = true;
        else if(camname === "TODOS")
            rc = true;
        else if(camname === "SHORES")
            rc = true;
        else if(camname === "BLACKS")
            rc = true;
        else if(camname === "HERO2")
            rc = true;
        else if(camname === "HAWAII")
            rc = true;
        else if(camname === "BACKDOOR")
            rc = true;

        return rc;
    },
    GP_IsIndex: function(testIndex){
        var rc=false;
        try {
            var num = Number(testIndex);
            if(num >= 0  && num < this.GP_TestList.length)
                rc=true;
        }
        catch(err){
            rc=false;
        }
        return rc;
    },
    GP_GetTestName: function(testIndex){
        var tname = "";
        if(this.IsIndex(testIndex)){
            try{
                var tnum = Number(testIndex);
                tname =  this.GP_TestList[tnum];
            }
            catch(err){
                console.log(err);
                tname = "";
            }

        }

        return tname;
    },
    GP_GetTestIndex: function(){
        log.info("GetTestIndex");
        var tstr =String(this.GP_Test_ID);
        log.info("GetTestIndex:"+tstr);
        return tstr;
    },
    GP_ReportTestList: function(){

        log.info("###################################");
        log.info("ReportTestList");
        log.info("Run These Tests");
        try {
            for (var i = 0; i < this.GoPro_TestMgr.GP_TestList.length; i++) {
                log.info(this.GoPro_TestMgr.GP_TestList[i]);

            }
        }
        catch(err){
            log.info("ReportTestList:"+err);
        }
        log.info("###################################");
    },
    GP_SetReportPath: function (reportPath) {
        if (reportpath === undefined || reportPath.length === 0) {
            reportpath = TestProperties["ReportPath"];
        }
        else {
            this.GP_TestProperties["ReportPath"] = reportPath;
        }
        reportPath = this.GP_TestProperties["ReportPath"];
        if (reportPath.length === 0)
            return;
        this.GP_ReportPath = reportPath;
        //log.info("SetReportPath:"+this.ReportPath);

    },
    GP_Reset: function () {

        this.GP_TestStepCount=0;
        this.GP_Test_ID = -1;
        this.GP_TestRunID++;
        this.GP_CurrentTestName = "";
        //log.info("Reset:");
        this.GP_TestProperties["TestRunStatus"] = "START";
        console.log(this.GP_Test_ID.toString());
        log.info("Reset:" + this.GP_TestRunID.toString()+"."+this.GP_Test_ID.toString());
    },

    GP_getTestCount: function () {
        this.GP_TestList.length;
        log.info("getTestCount:" + this.GP_TestList.length);
    },
    GP_SetTestID: function (testid) {
        var tid;
        try {
            tid = Number(testid);
            if (tid > 0 && tid < this.GP_TestList.length)
                this.GP_Test_ID = tid;
            else
                this.GP_ErrorMsg = "SetTestID:testid out of range of TestList";
        }
        catch (err) {
            this.GP_ErrorMsg = err;
        }
        log.info("SetTestID:" + this.GP_Test_ID.toString());
        return this.GP_Test_ID;
    },
    /**
     * @return {string}
     */
    GP_ReportStatus: function (TestrunID, Testname, passfail, comment) {
        this.GP_TestStepCount++;
        var testtype="TestStep";
       // if(this.TestStepCount==1)
       //     testtype="TestCase";
         if(this.GP_TestStepCount==0)
            testtype="####";
        //comment = UtilFN.StrReplace(comment,"."," ");
        var msg = passfail + " - " + this.GP_TestRunID.toString()+"."+this.Test_ID.toString()+"."+ this.TestStepCount+"."+TestrunID + " - " + testtype+" - " + Testname + " - " + comment;
        console.log("ReportStatus:" + msg);
        //log.info(msg.replace(/\./g,' '));
//        if(passfail.toUpperCase().indexOf("FAIL")>=0)
//            log.info(msg);
//        else if(passfail.toUpperCase().indexOf("PASS")>=0)
//            this.info(msg);
//        else
            log.info(msg);

/*        if(passfail.toUpperCase().indexOf("FAIL")>-1){
            if(this.RetryCount>1){
                this.RetryCount = 0;
            }
            else{
                this.RetryCount++;
                this.Test_ID--;//decrement index so NextTest() will rerun the test name
            }

        }
        else//passed cancel retry
            this.RetryCount = 0;*/

        return "ReportStatus";
    },
    UseTestRail: false,

    /********************************************
     * GP_GetTestName
     * Info: make sure testrail has been initialized with the runid prior to
     * @param testindex
     * @returns {*}
     * @constructor
     */
    GP_GetTestName: function(testindex){
        if(this.UseTestRail && testrail.Ready){
            testrail.GetTestCaseInfo()
        }
        else
            return this.GP_TestList[testindex];
    },
    /**
     * @return {string}
     */

    GP_NextTest: function () {
        var testname = "";

        this.GP_Test_ID++;
        this.GP_TestStepCount=0;
        if (this.GP_Test_ID >= this.GP_TestList.length) {
            //this.Reset();
            this.GP_TestProperties["TestRunStatus"] = "DONE";
            return "DONE";
        }

        for (var i = this.GP_Test_ID; i < this.GP_TestList.length; i++) {
            try {
                testname = this.GP_GetTestName(i);
                console.log("NextTest:" + i.toString() + "-" + this.GP_CAMERA + "-->" + testname);
                if (testname.length > 0) {
                    var nn = testname.toUpperCase().indexOf(this.GP_CAMERA.toUpperCase());
                    if (nn < 0) {
                        console.log("NextTest:SKIP-" + testname);
                        //log.info("NextTest:SKIP-" + testname);
                        continue;
                    }
                }
                /*            if (TextQualifier1.length > 0) {
                 if (testtname.indexOf(TextQualifier1) < 0)
                 continue;
                 }

                 if (TextQualifier2.length > 0) {
                 if (testtname.indexOf(TextQualifier2) < 0)
                 continue;
                 }

                 if (TextQualifier3.length > 0) {
                 if (testtname.indexOf(TextQualifier3) < 0)
                 continue;
                 }*/

                this.GP_CurrentTestName = testname;

                this.GP_TestProperties["CurrentTestName"] = this.CurrentTestName;
                this.GP_Test_ID = i;
                this.GP_Done = false;
                //log.category=this.CAMERA;
                log.category = this.TestProperties["DeviceName"];
                log.info("NextTest TestCase:" + this.GP_Test_ID.toString()+" - "+this.GP_CurrentTestName);
                this.GP_TestProperties["TestRunStatus"] = "RUNNING";

            }
            catch(err){
                log.info("NextTest:ERROR:" + this.GP_Test_ID.toString()+" - "+testname+" - "+err);

            }
            return testname;
        }
        log.info("NextTest:End of tests:" + this.GP_Test_ID.toString()+" - "+this.GP_CurrentTestName);
        this.GP_Reset();
        this.GP_Done = true;
        return "DONE";
    },

    //TestRail obj indexed by testclient GP_Test_ID
    //this.TestRuns[GP_Test_ID]=TestRail obj
    TestRuns: [],

    GP_TestList: [
        /* HERO2 TEST */

        "Settings_GeneralSettings_HERO2_NTSC_Protune",
        "Settings_HERO2_NTSC_Protune_1080-30 T_WideFOV",
        "Settings_HERO2_NTSC_Protune_1080-30 T_MediumFOV",
        "Settings_HERO2_NTSC_Protune_1080-25 T_WideFOV",
        "Settings_HERO2_NTSC_Protune_1080-25 T_MediumFOV",
        "Settings_HERO2_NTSC_Protune_1080-24 T_WideFOV",
        "Settings_HERO2_NTSC_Protune_1080-24 T_MediumFOV",
        "Settings_HERO2_NTSC_Protune_960-48 T_WideFOV",
        "Settings_HERO2_NTSC_Protune_720-60 T_WideFOV",

        "Settings_HERO2_NTSC_1080-30/25_WideFOV",
        "Settings_HERO2_NTSC_1080-30/25_MediumFOV",
        "Settings_HERO2_NTSC_1080-30/25_NarrowFOV",
        "Settings_HERO2_NTSC_960-48/50_WideFOV",
        "Settings_HERO2_NTSC_960-30/25_WideFOV",
        "Settings_HERO2_NTSC_720-60/50_WideFOV",
        "Settings_HERO2_NTSC_720-30/25_WideFOV",
        "Settings_HERO2_NTSC_WVGA-120/100_WideFOV",
        "Settings_HERO2_NTSC_WVGA-60/50_WideFOV",

        "Settings_HERO2_PAL_1080-30/25_WideFOV",
        "Settings_HERO2_PAL_1080-30/25_MediumFOV",
        "Settings_HERO2_PAL_1080-30/25_NarrowFOV",
        "Settings_HERO2_PAL_960-48/50_WideFOV",
        "Settings_HERO2_PAL_960-30/25_WideFOV",
        "Settings_HERO2_PAL_720-60/50_WideFOV",
        "Settings_HERO2_PAL_720-30/25_WideFOV",
        "Settings_HERO2_PAL_WVGA-120/100_WideFOV",
        "Settings_HERO2_PAL_WVGA-60/50_WideFOV",

        "Settings_GeneralSettings_HERO2_PAL_Protune",
        "Settings_HERO2_PAL_Protune_1080-30 T_WideFOV",
        "Settings_HERO2_PAL_Protune_1080-30 T_MediumFOV",
        "Settings_HERO2_PAL_Protune_1080-25 T_WideFOV",
        "Settings_HERO2_PAL_Protune_1080-25 T_MediumFOV",
        "Settings_HERO2_PAL_Protune_1080-24 T_WideFOV",
        "Settings_HERO2_PAL_Protune_1080-24 T_MediumFOV",
        "Settings_HERO2_PAL_Protune_960-48 T_WideFOV",
        "Settings_HERO2_PAL_Protune_720-60 T_WideFOV",

        "Settings_GeneralSettings_HERO2_PAL_Protune",
        "Settings_All_HERO2_960Res_PAL_Protune",
        "Settings_All_HERO2_1080Res_PAL_Protune",
        "Settings_All_HERO2_720Res_PAL_Protune",
        "Settings_GeneralSettings_HERO2_NTSC_Protune",
        "Settings_All_HERO2_960Res_NTSC_Protune",
        "Settings_All_HERO2_1080Res_NTSC_Protune",
        "Settings_All_HERO2_720Res_NTSC_NoProtune",
        "Settings_GeneralSettings_HERO2_PAL_NoProtune",
        "Settings_All_HERO2_960Res_PAL_NoProtune",
        "Settings_All_HERO2_1080Res_PAL_NoProtune",
        "Settings_All_HERO2_720Res_PAL_NoProtune",
        "Settings_All_HERO2_WVGARes_PAL_NoProtune",
        "Settings_GeneralSettings_HERO2_NTSC_NoProtune",
        "Settings_All_HERO2_960Res_NTSC_NoProtune",
        "Settings_All_HERO2_1080Res_NTSC_NoProtune",
        "Settings_All_HERO2_720Res_NTSC_NoProtune",
        "Settings_All_HERO2_WVGARes_NTSC_NoProtune",

        /**/


        /* SHORES TEST */
        "Settings_GeneralSettings_SHORES_NTSC",

        "Settings_SHORES_NTSC_960Res_30FPS",
        "Settings_SHORES_NTSC_960Res_30FPS_LoopingVideo",
        "Settings_SHORES_NTSC_1080Res_30FPS",
        "Settings_SHORES_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_SHORES_NTSC_720Res_60FPS",
        "Settings_SHORES_NTSC_720Res_60FPS_LoopingVideo",
        "Settings_SHORES_NTSC_720Res_30FPS",
        "Settings_SHORES_NTSC_720Res_30FPS_LoopingVideo",
        "Settings_SHORES_NTSC_WVGARes_60FPS",
        "Settings_SHORES_NTSC_WVGARes_60FPS_LoopingVideo",

        "Settings_GeneralSettings_SHORES_PAL",
        "Settings_SHORES_PAL_960Res_25FPS",
        "Settings_SHORES_PAL_960Res_25FPS_LoopingVideo",
        "Settings_SHORES_PAL_1080Res_25FPS",
        "Settings_SHORES_PAL_1080Res_25FPS_LoopingVideo",
        "Settings_SHORES_PAL_720Res_50FPS",
        "Settings_SHORES_PAL_720Res_50FPS_LoopingVideo",
        "Settings_SHORES_PAL_720Res_25FPS",
        "Settings_SHORES_PAL_720Res_25FPS_LoopingVideo",
        "Settings_SHORES_PAL_WVGARes_50FPS_WideFOV",
        "Settings_SHORES_PAL_WVGARes_50FPS_LoopingVideo",

        "Settings_GeneralSettings_SHORES_PAL_NoProtune",
        "Settings_All_SHORES_960Res_PAL_NoProtune",
        "Settings_All_SHORES_1080Res_PAL_NoProtune",
        "Settings_All_SHORES_720Res_PAL_NoProtune",
        "Settings_All_SHORES_WVGARes_PAL_NoProtune",
        "Settings_GeneralSettings_SHORES_NTSC_NoProtune",
        "Settings_All_SHORES_960Res_NTSC_NoProtune",
        "Settings_All_SHORES_1080Res_NTSC_NoProtune",
        "Settings_All_SHORES_720Res_NTSC_NoProtune",
        "Settings_All_SHORES_WVGARes_NTSC_NoProtune",

        /**/

        /* BLACKS TEST */

        "Settings_GeneralSettings_BLACKS_NTSC_Protune",
        "Settings_BLACKS_NTSC_Protune_1080Res_30FPS_WideFOV",
        "Settings_BLACKS_NTSC_Protune_1080Res_30FPS_MediumFOV",
        "Settings_BLACKS_NTSC_Protune_1080Res_24FPS_WideFOV",
        "Settings_BLACKS_NTSC_Protune_1080Res_24FPS_MediumFOV",
        "Settings_BLACKS_NTSC_Protune_960Res_48FPS_WideFOV",
        "Settings_BLACKS_NTSC_Protune_960Res_30FPS_WideFOV",
        "Settings_BLACKS_NTSC_Protune_720Res_60FPS_WideFOV",

        "Settings_BLACKS_NTSC_1080Res_30FPS_WideFOV",
        "Settings_BLACKS_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_1080Res_30FPS_MediumFOV",
        "Settings_BLACKS_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_1080Res_30FPS_NarrowFOV",
        "Settings_BLACKS_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_1080Res_24FPS_WideFOV",
        "Settings_BLACKS_NTSC_1080Res_24FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_1080Res_24FPS_MediumFOV",
        "Settings_BLACKS_NTSC_1080Res_24FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_1080Res_24FPS_NarrowFOV",
        "Settings_BLACKS_NTSC_1080Res_24FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_960Res_48FPS_WideFOV",
        "Settings_BLACKS_NTSC_960Res_48FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_960Res_30FPS_WideFOV",
        "Settings_BLACKS_NTSC_960Res_30FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_720Res_60FPS_WideFOV",
        "Settings_BLACKS_NTSC_720Res_60FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_720Res_30FPS_WideFOV",
        "Settings_BLACKS_NTSC_720Res_30FPS_LoopingVideo",
        "Settings_BLACKS_NTSC_WVGARes_120FPS_WideFOV",
        "Settings_BLACKS_NTSC_WVGARes_120FPS_LoopingVideo",

        "Settings_BLACKS_PAL_1080Res_25FPS_WideFOV",
        "Settings_BLACKS_PAL_1080Res_25FPS_LoopingVideo",
        "Settings_BLACKS_PAL_1080Res_25FPS_MediumFOV",
        "Settings_BLACKS_PAL_1080Res_25FPS_LoopingVideo",
        "Settings_BLACKS_PAL_1080Res_25FPS_NarrowFOV",
        "Settings_BLACKS_PAL_1080Res_25FPS_LoopingVideo",
        "Settings_BLACKS_PAL_1080Res_24FPS_WideFOV",
        "Settings_BLACKS_PAL_1080Res_24FPS_LoopingVideo",
        "Settings_BLACKS_PAL_1080Res_24FPS_MediumFOV",
        "Settings_BLACKS_PAL_1080Res_24FPS_LoopingVideo",
        "Settings_BLACKS_PAL_1080Res_24FPS_NarrowFOV",
        "Settings_BLACKS_PAL_1080Res_24FPS_LoopingVideo",
        "Settings_BLACKS_PAL_960Res_50FPS_WideFOV",
        "Settings_BLACKS_PAL_960Res_50FPS_LoopingVideo",
        "Settings_BLACKS_PAL_960Res_25FPS_WideFOV",
        "Settings_BLACKS_PAL_960Res_25FPS_LoopingVideo",
        "Settings_BLACKS_PAL_720Res_50FPS_WideFOV",
        "Settings_BLACKS_PAL_720Res_50FPS_LoopingVideo",
        "Settings_BLACKS_PAL_720Res_25FPS_WideFOV",
        "Settings_BLACKS_PAL_720Res_25FPS_LoopingVideo",
        "Settings_BLACKS_PAL_WVGARes_100FPS_WideFOV",
        "Settings_BLACKS_PAL_WVGARes_100FPS_LoopingVideo",

        "Settings_BLACKS_PAL_Protune_1080Res_25FPS_WideFOV",
        "Settings_BLACKS_PAL_Protune_1080Res_25FPS_MediumFOV",
        "Settings_BLACKS_PAL_Protune_1080Res_24FPS_WideFOV",
        "Settings_BLACKS_PAL_Protune_1080Res_24FPS_MediumFOV",
        "Settings_BLACKS_PAL_Protune_960Res_50FPS_WideFOV",
        "Settings_BLACKS_PAL_Protune_960Res_25FPS_WideFOV",
        "Settings_BLACKS_PAL_Protune_720Res_50FPS_WideFOV",

        "Settings_GeneralSettings_BLACKS_PAL_Protune",
        "Settings_All_BLACKS_960Res_PAL_Protune",
        "Settings_All_BLACKS_1080Res_PAL_Protune",
        "Settings_All_BLACKS_720Res_PAL_Protune",
        "Settings_GeneralSettings_BLACKS_NTSC_Protune",
        "Settings_All_BLACKS_960Res_NTSC_Protune",
        "Settings_All_BLACKS_1080Res_NTSC_Protune",
        "Settings_All_BLACKS_720Res_NTSC_NoProtune",
        "Settings_GeneralSettings_BLACKS_PAL_NoProtune",
        "Settings_All_BLACKS_960Res_PAL_NoProtune",
        "Settings_All_BLACKS_1080Res_PAL_NoProtune",
        "Settings_All_BLACKS_720Res_PAL_NoProtune",
        "Settings_All_BLACKS_WVGARes_PAL_NoProtune",
        "Settings_GeneralSettings_BLACKS_NTSC_NoProtune",
        "Settings_All_BLACKS_960Res_NTSC_NoProtune",
        "Settings_All_BLACKS_1080Res_NTSC_NoProtune",
        "Settings_All_BLACKS_720Res_NTSC_NoProtune",
        "Settings_All_BLACKS_WVGARes_NTSC_NoProtune",

        /**/

        /* TODOS TEST */

        "Settings_GeneralSettings_TODOS_NTSC_Protune",
        "Settings_TODOS_NTSC_Protune_1440Res_48FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_1440Res_30FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_1440Res_24FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_4K CinRes_12FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_4KRes_15FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_2.7K CinRes_24FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_2.7KRes_30FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_60FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_60FPS_MediumFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_60FPS_NarrowFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_48FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_48FPS_MediumFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_48FPS_NarrowFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_30FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_30FPS_MediumFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_30FPS_NarrowFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_24FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_24FPS_MediumFOV",
        "Settings_TODOS_NTSC_Protune_1080Res_24FPS_NarrowFOV",
        "Settings_TODOS_NTSC_Protune_960Res_100FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_720Res_120FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_720Res_120FPS_NarrowFOV",
        "Settings_TODOS_NTSC_Protune_720Res_60FPS_WideFOV",
        "Settings_TODOS_NTSC_Protune_720Res_60FPS_MediumFOV",
        "Settings_TODOS_NTSC_Protune_720Res_60FPS_NarrowFOV",

        "Settings_TODOS_NTSC_1440Res_48FPS_WideFOV",
        "Settings_TODOS_NTSC_1440Res_48FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1440Res_30FPS_WideFOV",
        "Settings_TODOS_NTSC_1440Res_30FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1440Res_24FPS_WideFOV",
        "Settings_TODOS_NTSC_1440Res_24FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1440Res_24FPS_PhotoVideo",
        "Settings_TODOS_NTSC_4K CinRes_12FPS_WideFOV",
        "Settings_TODOS_NTSC_4K CinRes_12FPS_LoopingVideo",
        "Settings_TODOS_NTSC_4KRes_15FPS_WideFOV",
        "Settings_TODOS_NTSC_4KRes_15FPS_LoopingVideo",
        "Settings_TODOS_NTSC_2.7K CinRes_24FPS_WideFOV",
        "Settings_TODOS_NTSC_2.7K CinRes_24FPS_LoopingVideo",
        "Settings_TODOS_NTSC_2.7K CinRes_24FPS_MediumFOV",
        "Settings_TODOS_NTSC_2.7K CinRes_24FPS_LoopingVideo",
        "Settings_TODOS_NTSC_2.7KRes_30FPS_WideFOV",
        "Settings_TODOS_NTSC_2.7KRes_30FPS_LoopingVideo",
        "Settings_TODOS_NTSC_2.7KRes_30FPS_MediumFOV",
        "Settings_TODOS_NTSC_2.7KRes_30FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_60FPS_WideFOV",
        "Settings_TODOS_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_60FPS_NarrowFOV",
        "Settings_TODOS_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_60FPS_MediumFOV",
        "Settings_TODOS_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_48FPS_WideFOV",
        "Settings_TODOS_NTSC_1080Res_48FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_48FPS_MediumFOV",
        "Settings_TODOS_NTSC_1080Res_48FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_48FPS_NarrowFOV",
        "Settings_TODOS_NTSC_1080Res_48FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_30FPS_WideFOV",
        "Settings_TODOS_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_30FPS_MediumFOV",
        "Settings_TODOS_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_30FPS_NarrowFOV",
        "Settings_TODOS_NTSC_1080Res_30FPS_PhotoVideo",
        "Settings_TODOS_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_24FPS_WideFOV",
        "Settings_TODOS_NTSC_1080Res_24FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_24FPS_MediumFOV",
        "Settings_TODOS_NTSC_1080Res_24FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_24FPS_NarrowFOV",
        "Settings_TODOS_NTSC_1080Res_24FPS_LoopingVideo",
        "Settings_TODOS_NTSC_1080Res_24FPS_PhotoVideo",
        "Settings_TODOS_NTSC_960Res_100FPS_WideFOV",
        "Settings_TODOS_NTSC_960Res_100FPS_LoopingVideo",
        "Settings_TODOS_NTSC_960Res_60FPS_WideFOV",
        "Settings_TODOS_NTSC_960Res_60FPS_LoopingVideo",
        "Settings_TODOS_NTSC_960Res_48FPS_WideFOV",
        "Settings_TODOS_NTSC_960Res_48FPS_LoopingVideo",
        "Settings_TODOS_NTSC_720Res_60FPS_WideFOV",
        "Settings_TODOS_NTSC_720Res_60FPS_LoopingVideo",
        "Settings_TODOS_NTSC_720Res_60FPS_MediumFOV",
        "Settings_TODOS_NTSC_720Res_60FPS_LoopingVideo",
        "Settings_TODOS_NTSC_720Res_60FPS_NarrowFOV",
        "Settings_TODOS_NTSC_720Res_60FPS_PhotoVideo",
        "Settings_TODOS_NTSC_720Res_60FPS_LoopingVideo",
        "Settings_TODOS_NTSC_720Res_120FPS_WideFOV",
        "Settings_TODOS_NTSC_720Res_120FPS_LoopingVideo",
        "Settings_TODOS_NTSC_720Res_120FPS_NarrowFOV",
        "Settings_TODOS_NTSC_720Res_120FPS_LoopingVideo",
        "Settings_TODOS_NTSC_WVGARes_240FPS_WideFOV",
        "Settings_TODOS_NTSC_WVGARes_240FPS_LoopingVideo",


        "Settings_TODOS_PAL_1440Res_48FPS_WideFOV",
        "Settings_TODOS_PAL_1440Res_48FPS_LoopingVideo",
        "Settings_TODOS_PAL_1440Res_30FPS_WideFOV",
        "Settings_TODOS_PAL_1440Res_30FPS_LoopingVideo",
        "Settings_TODOS_PAL_1440Res_24FPS_WideFOV",
        "Settings_TODOS_PAL_1440Res_24FPS_LoopingVideo",
        "Settings_TODOS_PAL_1440Res_24FPS_PhotoVideo",
        "Settings_TODOS_PAL_4K CinRes_12FPS_WideFOV",
        "Settings_TODOS_PAL_4K CinRes_12FPS_LoopingVideo",
        "Settings_TODOS_PAL_4KRes_15FPS_WideFOV",
        "Settings_TODOS_PAL_4KRes_15FPS_LoopingVideo",
        "Settings_TODOS_PAL_2.7K CinRes_24FPS_WideFOV",
        "Settings_TODOS_PAL_2.7K CinRes_24FPS_LoopingVideo",
        "Settings_TODOS_PAL_2.7K CinRes_24FPS_MediumFOV",
        "Settings_TODOS_PAL_2.7K CinRes_24FPS_LoopingVideo",
        "Settings_TODOS_PAL_2.7KRes_30FPS_WideFOV",
        "Settings_TODOS_PAL_2.7KRes_30FPS_LoopingVideo",
        "Settings_TODOS_PAL_2.7KRes_30FPS_MediumFOV",
        "Settings_TODOS_PAL_2.7KRes_30FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_60FPS_WideFOV",
        "Settings_TODOS_PAL_1080Res_60FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_60FPS_NarrowFOV",
        "Settings_TODOS_PAL_1080Res_60FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_60FPS_MediumFOV",
        "Settings_TODOS_PAL_1080Res_60FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_48FPS_WideFOV",
        "Settings_TODOS_PAL_1080Res_48FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_48FPS_MediumFOV",
        "Settings_TODOS_PAL_1080Res_48FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_48FPS_NarrowFOV",
        "Settings_TODOS_PAL_1080Res_48FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_30FPS_WideFOV",
        "Settings_TODOS_PAL_1080Res_30FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_30FPS_MediumFOV",
        "Settings_TODOS_PAL_1080Res_30FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_30FPS_NarrowFOV",
        "Settings_TODOS_PAL_1080Res_30FPS_PhotoVideo",
        "Settings_TODOS_PAL_1080Res_30FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_24FPS_WideFOV",
        "Settings_TODOS_PAL_1080Res_24FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_24FPS_MediumFOV",
        "Settings_TODOS_PAL_1080Res_24FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_24FPS_NarrowFOV",
        "Settings_TODOS_PAL_1080Res_24FPS_LoopingVideo",
        "Settings_TODOS_PAL_1080Res_24FPS_PhotoVideo",
        "Settings_TODOS_PAL_960Res_100FPS_WideFOV",
        "Settings_TODOS_PAL_960Res_100FPS_LoopingVideo",
        "Settings_TODOS_PAL_960Res_60FPS_WideFOV",
        "Settings_TODOS_PAL_960Res_60FPS_LoopingVideo",
        "Settings_TODOS_PAL_960Res_48FPS_WideFOV",
        "Settings_TODOS_PAL_960Res_48FPS_LoopingVideo",
        "Settings_TODOS_PAL_720Res_60FPS_WideFOV",
        "Settings_TODOS_PAL_720Res_60FPS_LoopingVideo",
        "Settings_TODOS_PAL_720Res_60FPS_MediumFOV",
        "Settings_TODOS_PAL_720Res_60FPS_LoopingVideo",
        "Settings_TODOS_PAL_720Res_60FPS_NarrowFOV",
        "Settings_TODOS_PAL_720Res_60FPS_PhotoVideo",
        "Settings_TODOS_PAL_720Res_60FPS_LoopingVideo",
        "Settings_TODOS_PAL_720Res_120FPS_WideFOV",
        "Settings_TODOS_PAL_720Res_120FPS_LoopingVideo",
        "Settings_TODOS_PAL_720Res_120FPS_NarrowFOV",
        "Settings_TODOS_PAL_720Res_120FPS_LoopingVideo",
        "Settings_TODOS_PAL_WVGARes_240FPS_WideFOV",
        "Settings_TODOS_PAL_WVGARes_240FPS_LoopingVideo",

        "Settings_TODOS_PAL_Protune_1440Res_24FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_1440Res_25FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_1440Res_48FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_4K CinRes_12FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_4KRes_12.5FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_2.7K CinRes_24FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_2.7KRes_25FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_1080Res_50FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_1080Res_50FPS_MediumFOV",
        "Settings_TODOS_PAL_Protune_1080Res_50FPS_NarrowFOV",
        "Settings_TODOS_PAL_Protune_1080Res_48FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_1080Res_48FPS_MediumFOV",
        "Settings_TODOS_PAL_Protune_1080Res_48FPS_NarrowFOV",
        "Settings_TODOS_PAL_Protune_1080Res_25FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_1080Res_25FPS_MediumFOV",
        "Settings_TODOS_PAL_Protune_1080Res_25FPS_NarrowFOV",
        "Settings_TODOS_PAL_Protune_1080Res_24FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_1080Res_24FPS_MediumFOV",
        "Settings_TODOS_PAL_Protune_1080Res_24FPS_NarrowFOV",
        "Settings_TODOS_PAL_Protune_960Res_100FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_720Res_50FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_720Res_50FPS_MediumFOV",
        "Settings_TODOS_PAL_Protune_720Res_50FPS_NarrowFOV",
        "Settings_TODOS_PAL_Protune_720Res_100FPS_WideFOV",
        "Settings_TODOS_PAL_Protune_720Res_100FPS_NarrowFOV",

        "Settings_TODOS_NTSC_Protune_4KCinRes_12FPS_WideFOV",
        "Settings_GeneralSettings_TODOS_PAL_Protune",
        "Settings_All_TODOS_960Res_PAL_Protune",
        "Settings_All_TODOS_4KCinRes_PAL_Protune",
        "Settings_All_TODOS_4KRes_PAL_Protune",
        "Settings_All_TODOS_27KCinRes_PAL_Protune",
        "Settings_All_TODOS_27KRes_PAL_Protune",
        "Settings_All_TODOS_1440Res_PAL_Protune",
        "Settings_All_TODOS_1080Res_PAL_Protune",
        "Settings_All_TODOS_720Res_PAL_Protune",
        "Settings_GeneralSettings_TODOS_NTSC_Protune",
        "Settings_All_TODOS_960Res_NTSC_Protune",
        "Settings_All_TODOS_4KCinRes_NTSC_Protune",
        "Settings_All_TODOS_4KRes_NTSC_Protune",
        "Settings_All_TODOS_27KCinRes_NTSC_Protune",
        "Settings_All_TODOS_27KRes_NTSC_Protune",
        "Settings_All_TODOS_1440Res_NTSC_Protune",
        "Settings_All_TODOS_1080Res_NTSC_Protune",
        "Settings_All_TODOS_720Res_NTSC_NoProtune",
        "Settings_GeneralSettings_TODOS_PAL_NoProtune",
        "Settings_All_TODOS_960Res_PAL_NoProtune",
        "Settings_All_TODOS_4KCinRes_PAL_NoProtune",
        "Settings_All_TODOS_4KRes_PAL_NoProtune",
        "Settings_All_TODOS_27KCinRes_PAL_NoProtune",
        "Settings_All_TODOS_27KRes_PAL_NoProtune",
        "Settings_All_TODOS_1440Res_PAL_NoProtune",
        "Settings_All_TODOS_1080Res_PAL_NoProtune",
        "Settings_All_TODOS_720Res_PAL_NoProtune",
        "Settings_All_TODOS_WVGARes_PAL_NoProtune",
        "Settings_GeneralSettings_TODOS_NTSC_NoProtune",
        "Settings_All_TODOS_960Res_NTSC_NoProtune",
        "Settings_All_TODOS_4KCinRes_NTSC_NoProtune",
        "Settings_All_TODOS_4KRes_NTSC_NoProtune",
        "Settings_All_TODOS_27KCinRes_NTSC_NoProtune",
        "Settings_All_TODOS_27KRes_NTSC_NoProtune",
        "Settings_All_TODOS_1440Res_NTSC_NoProtune",
        "Settings_All_TODOS_1080Res_NTSC_NoProtune",
        "Settings_All_TODOS_720Res_NTSC_NoProtune",
        "Settings_All_TODOS_WVGARes_NTSC_NoProtune",

        /**/

        /* ULUWATU TEST*/
        "Settings_GeneralSettings_ULUWATU_NTSC",
        //"Settings_ULUWATU_SettingSelect|Video Resolution|WVGA",
        "Settings_ULUWATU_NTSC_960Res_60FPS_WideFOV",
        "Settings_ULUWATU_NTSC_960Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_960Res_30FPS_WideFOV",
        "Settings_ULUWATU_NTSC_960Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_1080Res_60FPS_WideFOV",
        "Settings_ULUWATU_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_1080Res_60FPS_MediumFOV",
        "Settings_ULUWATU_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_1080Res_60FPS_NarrowFOV",
        "Settings_ULUWATU_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_1080Res_30FPS_WideFOV",
        "Settings_ULUWATU_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_1080Res_30FPS_MediumFOV",
        "Settings_ULUWATU_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_1080Res_30FPS_NarrowFOV",
        "Settings_ULUWATU_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_120FPS_WideFOV",
        "Settings_ULUWATU_NTSC_720Res_120FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_120FPS_MediumFOV",
        "Settings_ULUWATU_NTSC_720Res_120FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_120FPS_NarrowFOV",
        "Settings_ULUWATU_NTSC_720Res_120FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_60FPS_WideFOV",
        "Settings_ULUWATU_NTSC_720Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_60FPS_MediumFOV",
        "Settings_ULUWATU_NTSC_720Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_60FPS_NarrowFOV",
        "Settings_ULUWATU_NTSC_720Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_30FPS_WideFOV",
        "Settings_ULUWATU_NTSC_720Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_30FPS_MediumFOV",
        "Settings_ULUWATU_NTSC_720Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_720Res_30FPS_NarrowFOV",
        "Settings_ULUWATU_NTSC_720Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_WVGARes_120FPS_WideFOV",
        "Settings_ULUWATU_NTSC_WVGARes_120FPS_LoopingVideo",
        "Settings_ULUWATU_NTSC_WVGARes_60FPS_WideFOV",
        "Settings_ULUWATU_NTSC_WVGARes_60FPS_LoopingVideo",

        "Settings_GeneralSettings_ULUWATU_PAL",
        "Settings_ULUWATU_PAL_960Res_60FPS_WideFOV",
        "Settings_ULUWATU_PAL_960Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_960Res_30FPS_WideFOV",
        "Settings_ULUWATU_PAL_960Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_1080Res_60FPS_WideFOV",
        "Settings_ULUWATU_PAL_1080Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_1080Res_60FPS_MediumFOV",
        "Settings_ULUWATU_PAL_1080Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_1080Res_60FPS_NarrowFOV",
        "Settings_ULUWATU_PAL_1080Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_1080Res_30FPS_WideFOV",
        "Settings_ULUWATU_PAL_1080Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_1080Res_30FPS_MediumFOV",
        "Settings_ULUWATU_PAL_1080Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_1080Res_30FPS_NarrowFOV",
        "Settings_ULUWATU_PAL_1080Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_120FPS_WideFOV",
        "Settings_ULUWATU_PAL_720Res_120FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_120FPS_MediumFOV",
        "Settings_ULUWATU_PAL_720Res_120FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_120FPS_NarrowFOV",
        "Settings_ULUWATU_PAL_720Res_120FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_60FPS_WideFOV",
        "Settings_ULUWATU_PAL_720Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_60FPS_MediumFOV",
        "Settings_ULUWATU_PAL_720Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_60FPS_NarrowFOV",
        "Settings_ULUWATU_PAL_720Res_60FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_30FPS_WideFOV",
        "Settings_ULUWATU_PAL_720Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_30FPS_MediumFOV",
        "Settings_ULUWATU_PAL_720Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_720Res_30FPS_NarrowFOV",
        "Settings_ULUWATU_PAL_720Res_30FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_WVGARes_120FPS_WideFOV",
        "Settings_ULUWATU_PAL_WVGARes_120FPS_LoopingVideo",
        "Settings_ULUWATU_PAL_WVGARes_60FPS_WideFOV",
        "Settings_ULUWATU_PAL_WVGARes_60FPS_LoopingVideo",

        "Settings_GeneralSettings_ULUWATU_PAL_NoProtune",
        "Settings_All_ULUWATU_960Res_PAL_NoProtune",
        "Settings_All_ULUWATU_1080Res_PAL_NoProtune",
        "Settings_All_ULUWATU_720Res_PAL_NoProtune",
        "Settings_All_ULUWATU_WVGARes_PAL_NoProtune",
        "Settings_GeneralSettings_ULUWATU_NTSC_NoProtune",
        "Settings_All_ULUWATU_960Res_NTSC_NoProtune",
        "Settings_All_ULUWATU_1080Res_NTSC_NoProtune",
        "Settings_All_ULUWATU_720Res_NTSC_NoProtune",
        "Settings_All_ULUWATU_WVGARes_NTSC_NoProtune",

        /* BAWA TEST */


        "Settings_GeneralSettings_BAWA_NTSC_Protune",
        "Settings_BAWA_NTSC_Protune_1440Res_24FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1440Res_30FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1440Res_48FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_4K 17:9Res_12FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_4KRes_15FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_2.7K 17:9Res_24FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_2.7K 17:9Res_24FPS_MediumFOV",
        "Settings_BAWA_NTSC_Protune_2.7KRes_30FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080 SuperViewRes_60FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080 SuperViewRes_48FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080 SuperViewRes_24FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080 SuperViewRes_30FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_60FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_60FPS_MediumFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_60FPS_NarrowFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_48FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_48FPS_MediumFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_48FPS_NarrowFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_30FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_30FPS_MediumFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_30FPS_NarrowFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_24FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_24FPS_MediumFOV",
        "Settings_BAWA_NTSC_Protune_1080Res_24FPS_NarrowFOV",
        "Settings_BAWA_NTSC_Protune_960Res_100FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_960Res_60FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_720 SuperViewRes_60FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_720 SuperViewRes_100FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_720Res_60FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_720Res_60FPS_MediumFOV",
        "Settings_BAWA_NTSC_Protune_720Res_60FPS_NarrowFOV",
        "Settings_BAWA_NTSC_Protune_720Res_120FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_720Res_120FPS_NarrowFOV",

        "Settings_BAWA_NTSC_1440Res_48FPS_WideFOV",
        "Settings_BAWA_NTSC_1440Res_30FPS_WideFOV",
        "Settings_BAWA_NTSC_1440Res_30FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1440Res_24FPS_WideFOV",
        "Settings_BAWA_NTSC_1440Res_24FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1440Res_24FPS_PhotoVideo",
        "Settings_BAWA_NTSC_4K 17:9Res_12FPS_WideFOV",
        "Settings_BAWA_NTSC_4KRes_15FPS_WideFOV",
        "Settings_BAWA_NTSC_2.7K 17:9Res_24FPS_WideFOV",
        "Settings_BAWA_NTSC_2.7K 17:9Res_24FPS_MediumFOV",
        "Settings_BAWA_NTSC_2.7KRes_30FPS_WideFOV",
        "Settings_BAWA_NTSC_2.7KRes_30FPS_MediumFOV",
        "Settings_BAWA_NTSC_1080 SuperViewRes_60FPS_WideFOV",
        "Settings_BAWA_NTSC_1080 SuperViewRes_48FPS_WideFOV",
        "Settings_BAWA_NTSC_1080 SuperViewRes_30FPS_WideFOV",
        "Settings_BAWA_NTSC_1080 SuperViewRes_30FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080 SuperViewRes_24FPS_WideFOV",
        "Settings_BAWA_NTSC_1080 SuperViewRes_24FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_60FPS_WideFOV",
        "Settings_BAWA_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_60FPS_MediumFOV",
        "Settings_BAWA_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_60FPS_NarrowFOV",
        "Settings_BAWA_NTSC_1080Res_60FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_48FPS_WideFOV",
        "Settings_BAWA_NTSC_1080Res_48FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_48FPS_MediumFOV",
        "Settings_BAWA_NTSC_1080Res_48FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_48FPS_NarrowFOV",
        "Settings_BAWA_NTSC_1080Res_48FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_30FPS_WideFOV",
        "Settings_BAWA_NTSC_1080Res_30FPS_PhotoVideo",
        "Settings_BAWA_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_30FPS_MediumFOV",
        "Settings_BAWA_NTSC_1080Res_30FPS_PhotoVideo",
        "Settings_BAWA_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_30FPS_NarrowFOV",
        "Settings_BAWA_NTSC_1080Res_30FPS_PhotoVideo",
        "Settings_BAWA_NTSC_1080Res_30FPS_LoopingVideo",
        "Settings_BAWA_NTSC_1080Res_24FPS_WideFOV",
        "Settings_BAWA_NTSC_1080Res_24FPS_MediumFOV",
        "Settings_BAWA_NTSC_1080Res_24FPS_NarrowFOV",
        "Settings_BAWA_NTSC_1080Res_24FPS_PhotoVideo",
        "Settings_BAWA_NTSC_960Res_100FPS_WideFOV",
        "Settings_BAWA_NTSC_960Res_60FPS_WideFOV",
        "Settings_BAWA_NTSC_960Res_60FPS_LoopingVideo",
        "Settings_BAWA_NTSC_960Res_48FPS_WideFOV",
        "Settings_BAWA_NTSC_960Res_48FPS_LoopingVideo",
        "Settings_BAWA_NTSC_720 SuperViewRes_48FPS_WideFOV",
        "Settings_BAWA_NTSC_720 SuperViewRes_60FPS_WideFOV",
        "Settings_BAWA_NTSC_720 SuperViewRes_100FPS_WideFOV",
        "Settings_BAWA_NTSC_720Res_60FPS_WideFOV",
        "Settings_BAWA_NTSC_720Res_60FPS_MediumFOV",
        "Settings_BAWA_NTSC_720Res_60FPS_NarrowFOV",
        "Settings_BAWA_NTSC_720Res_120FPS_WideFOV",
        "Settings_BAWA_NTSC_720Res_120FPS_NarrowFOV",
        "Settings_BAWA_NTSC_WVGARes_240FPS_WideFOV",
        "Settings_BAWA_NTSC_720 SuperViewRes_48FPS_LoopingVideo",
        "Settings_BAWA_NTSC_720 SuperViewRes_60FPS_LoopingVideo",
        "Settings_BAWA_NTSC_720Res_60FPS_PhotoVideo",
        "Settings_BAWA_NTSC_720Res_60FPS_LoopingVideo",

        "Settings_BAWA_PAL_1440Res_24FPS_WideFOV",
        "Settings_BAWA_PAL_1440Res_24FPS_LoopingVideo",
        "Settings_BAWA_PAL_1440Res_24FPS_PhotoVideo",
        "Settings_BAWA_PAL_1440Res_25FPS_WideFOV",
        "Settings_BAWA_PAL_1440Res_25FPS_LoopingVideo",
        "Settings_BAWA_PAL_1440Res_48FPS_WideFOV",
        "Settings_BAWA_PAL_4K 17:9Res_12FPS_WideFOV",
        "Settings_BAWA_PAL_4KRes_12.5FPS_WideFOV",
        "Settings_BAWA_PAL_2.7K 17:9Res_24FPS_WideFOV",
        "Settings_BAWA_PAL_2.7K 17:9Res_24FPS_MediumFOV",
        "Settings_BAWA_PAL_27KRes_25FPS_WideFOV",
        "Settings_BAWA_PAL_1080 SuperViewRes_50FPS_WideFOV",
        "Settings_BAWA_PAL_1080 SuperViewRes_48FPS_WideFOV",
        "Settings_BAWA_PAL_1080 SuperViewRes_24FPS_WideFOV",
        "Settings_BAWA_PAL_1080 SuperViewRes_24FPS_LoopingVideo",
        "Settings_BAWA_PAL_1080SuperViewRes_25FPS_WideFOV",
        "Settings_BAWA_PAL_1080 SuperViewRes_25FPS_LoopingVideo",
        "Settings_BAWA_PAL_1080Res_50FPS_WideFOV",
        "Settings_BAWA_PAL_1080Res_50FPS_MediumFOV",
        "Settings_BAWA_PAL_1080Res_50FPS_NarrowFOV",
        "Settings_BAWA_PAL_1080Res_50FPS_LoopingVideo",
        "Settings_BAWA_PAL_1080Res_48FPS_WideFOV",
        "Settings_BAWA_PAL_1080Res_48FPS_MediumFOV",
        "Settings_BAWA_PAL_1080Res_48FPS_NarrowFOV",
        "Settings_BAWA_PAL_1080Res_48FPS_LoopingVideo",
        "Settings_BAWA_PAL_1080Res_25FPS_WideFOV",
        "Settings_BAWA_PAL_1080Res_25FPS_MediumFOV",
        "Settings_BAWA_PAL_1080Res_25FPS_NarrowFOV",
        "Settings_BAWA_PAL_1080Res_25FPS_LoopingVideo",
        "Settings_BAWA_PAL_1080Res_25FPS_PhotoVideo",
        "Settings_BAWA_PAL_1080Res_24FPS_WideFOV",
        "Settings_BAWA_PAL_1080Res_24FPS_MediumFOV",
        "Settings_BAWA_PAL_1080Res_24FPS_NarrowFOV",
        "Settings_BAWA_PAL_1080Res_24FPS_LoopingVideo",
        "Settings_BAWA_PAL_1080Res_24FPS_PhotoVideo",
        "Settings_BAWA_PAL_960Res_100FPS_WideFOV",
        "Settings_BAWA_PAL_960Res_50FPS_WideFOV",
        "Settings_BAWA_PAL_960Res_50FPS_LoopingVideo",
        "Settings_BAWA_PAL_960Res_48FPS_WideFOV",
        "Settings_BAWA_PAL_960Res_48FPS_LoopingVideo",
        "Settings_BAWA_PAL_720 SuperViewRes_100FPS_WideFOV",
        "Settings_BAWA_PAL_720 SuperViewRes_50FPS_WideFOV",
        "Settings_BAWA_PAL_720 SuperViewRes_50FPS_LoopingVideo",
        "Settings_BAWA_PAL_720 SuperViewRes_48FPS_WideFOV",
        "Settings_BAWA_PAL_720 SuperViewRes_48FPS_LoopingVideo",
        "Settings_BAWA_PAL_720Res_50FPS_WideFOV",
        "Settings_BAWA_PAL_720Res_50FPS_MediumFOV",
        "Settings_BAWA_PAL_720Res_50FPS_NarrowFOV",
        "Settings_BAWA_PAL_720Res_50FPS_LoopingVideo",
        "Settings_BAWA_PAL_720Res_50FPS_PhotoVideo",
        "Settings_BAWA_PAL_720Res_100FPS_WideFOV",
        "Settings_BAWA_PAL_720Res_100FPS_NarrowFOV",
        "Settings_BAWA_PAL_WVGARes_240FPS_WideFOV",

        "Settings_BAWA_PAL_Protune_1440Res_24FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1440Res_25FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1440Res_48FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_4K 17:9Res_12FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_4KRes_12.5FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_2.7K 17:9Res_24FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_2.7K 17:9Res_24FPS_MediumFOV",
        "Settings_BAWA_PAL_Protune_2.7KRes_25FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_2.7KRes_25FPS_MediumFOV",
        "Settings_BAWA_PAL_Protune_1080 SuperViewRes_50FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1080 SuperViewRes_48FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1080 SuperViewRes_24FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1080 SuperViewRes_25FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1080Res_50FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1080Res_50FPS_MediumFOV",
        "Settings_BAWA_PAL_Protune_1080Res_50FPS_NarrowFOV",
        "Settings_BAWA_PAL_Protune_1080Res_48FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1080Res_48FPS_MediumFOV",
        "Settings_BAWA_PAL_Protune_1080Res_48FPS_NarrowFOV",
        "Settings_BAWA_PAL_Protune_1080Res_25FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1080Res_25FPS_MediumFOV",
        "Settings_BAWA_PAL_Protune_1080Res_25FPS_NarrowFOV",
        "Settings_BAWA_PAL_Protune_1080Res_24FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_1080Res_24FPS_MediumFOV",
        "Settings_BAWA_PAL_Protune_1080Res_24FPS_NarrowFOV",
        "Settings_BAWA_PAL_Protune_960Res_100FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_960Res_50FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_720 SuperViewRes_50FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_720 SuperViewRes_100FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_720Res_50FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_720Res_50FPS_MediumFOV",
        "Settings_BAWA_PAL_Protune_720Res_50FPS_NarrowFOV",
        "Settings_BAWA_PAL_Protune_720Res_100FPS_WideFOV",
        "Settings_BAWA_PAL_Protune_720Res_100FPS_NarrowFOV",

        "Testx_BAWA_NTSC_Protune_1440Res_24FPS_WideFOV",
        "Settings_BAWA_NTSC_Protune_4K179Res_12FPS_WideFOV",
        "Settings_GeneralSettings_BAWA_PAL_Protune",
        "Settings_All_BAWA_960Res_PAL_Protune",
        "Settings_All_BAWA_4K179Res_PAL_Protune",
        "Settings_All_BAWA_4KRes_PAL_Protune",
        "Settings_All_BAWA_27K179Res_PAL_Protune",
        "Settings_All_BAWA_27KRes_PAL_Protune",
        "Settings_All_BAWA_1440Res_PAL_Protune",
        "Settings_All_BAWA_1080SuperViewRes_PAL_Protune",
        "Settings_All_BAWA_1080Res_PAL_Protune",
        "Settings_All_BAWA_720SuperViewRes_PAL_Protune",
        "Settings_All_BAWA_720Res_PAL_Protune",
        "Settings_GeneralSettings_BAWA_NTSC_Protune",
        "Settings_All_BAWA_960Res_NTSC_Protune",
        "Settings_All_BAWA_4K179Res_NTSC_Protune",
        "Settings_All_BAWA_4KRes_NTSC_Protune",
        "Settings_All_BAWA_27K179Res_NTSC_Protune",
        "Settings_All_BAWA_27KRes_NTSC_Protune",
        "Settings_All_BAWA_1440Res_NTSC_Protune",
        "Settings_All_BAWA_1080SuperViewRes_NTSC_Protune",
        "Settings_All_BAWA_1080Res_NTSC_Protune",
        "Settings_All_BAWA_720SuperViewRes_NTSC_NoProtune",
        "Settings_All_BAWA_720Res_NTSC_NoProtune",
        "Settings_GeneralSettings_BAWA_PAL_NoProtune",
        "Settings_All_BAWA_960Res_PAL_NoProtune",
        "Settings_All_BAWA_4K179Res_PAL_NoProtune",
        "Settings_All_BAWA_4KRes_PAL_NoProtune",
        "Settings_All_BAWA_27K179Res_PAL_NoProtune",
        "Settings_All_BAWA_27KRes_PAL_NoProtune",
        "Settings_All_BAWA_1440Res_PAL_NoProtune",
        "Settings_All_BAWA_1080SuperViewRes_PAL_NoProtune",
        "Settings_All_BAWA_1080Res_PAL_NoProtune",
        "Settings_All_BAWA_720SuperViewRes_PAL_NoProtune",
        "Settings_All_BAWA_720Res_PAL_NoProtune",
        "Settings_All_BAWA_WVGARes_PAL_NoProtune",
        "Settings_GeneralSettings_BAWA_NTSC_NoProtune",
        "Settings_All_BAWA_720SuperViewRes_NTSC_NoProtune",
        "Settings_All_BAWA_960Res_NTSC_NoProtune",
        "Settings_All_BAWA_4K179Res_NTSC_NoProtune",
        "Settings_All_BAWA_4KRes_NTSC_NoProtune",
        "Settings_All_BAWA_27K179Res_NTSC_NoProtune",
        "Settings_All_BAWA_27KRes_NTSC_NoProtune",
        "Settings_All_BAWA_1440Res_NTSC_NoProtune",
        "Settings_All_BAWA_1080SuperViewRes_NTSC_NoProtune",
        "Settings_All_BAWA_1080Res_NTSC_NoProtune",
        "Settings_All_BAWA_720Res_NTSC_NoProtune",
        "Settings_All_BAWA_WVGARes_NTSC_NoProtune"

        /************************/

    ]
}

/*

function EvalRunTest(test_name){
    var rc = false;
    try{
        LOG("EvalRunTest: "+test_name,"logMessage");
        eval(test_name);
        rc=true;
    }
    catch(err){
        LOG("EvalRunTest:Error: Invalid Name - "+err,"logMessage");
        rc=false;
    }
    return rc;
}
*/


/*
function EvalTestName(test_name){
    var fail=0;
    var rc=false;
    ErrorMsg="";
    LOG("Eval CURRENT_SCRIPT_NAME: "+CURRENT_SCRIPT_NAME,"logMessage");

    if(CURRENT_SCRIPT_NAME.indexof("Settings")>0){
        LOG("Test START: "+test_name,"logMessage");
        Nav_Home_Connect();
        Nav_Preview_Settings();
        if(!EvalRunTest(test_name)){
            LOG("EvalTestName: "+test_name,"logMessage");
            LOG("START TEST: "+test_name,"logMessage");

            fail += EvalProtunes(test_name);
            fail += EvalNTSCPAL(test_name)


            fail += EvalVideoResolution(test_name);
            fail += EvalFPS(test_name);
            fail += EvalFOV(test_name);
            fail += EvalLooping(test_name);
            fail += EvalPhotoVideo(test_name);


            TestReportStatus(fail,test_name,ErrorMsg);

        }
        Nav_Settings_Done();
        LOG("Test DONE: "+test_name,"logMessage");
    }
    else
        LOG("Eval Failed: CURRENT_SCRIPT_NAME:Settings -  "+CURRENT_SCRIPT_NAME,"logMessage");
}
*/


/********************************************
 *
 * @return {string}
 * @return {string}
 */
function GoProTestMgr(sessionresponse, postData) {
    //console.log("GoProTestMgr postData:" + postData);
    var dataitems = postData.split("&");//"%7C"
    var result="";// = [];


    try {
        switch(dataitems[0]) {
            case "/LoadRunID":///LoadRunID&10563&bawa
                //load the specfied testrail runid suite of tests
                console.log(dataitems[0]);
                if (dataitems.length > 1) {
                    console.log("RunID="+dataitems[1]);//10563
                    //this.GoPro_TestMgr.Testrail=new TestRail();
                    TestRail.TestRail.GetTestSuite(sessionresponse,dataitems[1]);
                }
                if (dataitems.length > 2) {
                    console.log("Camera="+dataitems[2]);//bawa
                    TestRail.TestRail.GP_CAMERA=dataitems[2].toUpperCase();
                }

                //sessionresponse.end();
                break;
            case "/NextTest"://GoProTestMgr/NextTest
                console.log(dataitems[0]);
                console.log(TestRail.TestRail.GP_CAMERA);
                var test =TestRail.TestRail.GetNextTest(TestRail.TestRail.GP_CAMERA);
                if(test == null){
                    sessionresponse.write("{'Test':null,'CAMERA':'"+TestRail.TestRail.GP_CAMERA+"','Error': 'Test Not Found'}");
                }
                else{
                    sessionresponse.write(JSON.stringify(test));
                }
                //sessionresponse.write("{'Test':'"+dataitems[0]+"','CAMERA':'"+GoPro_TestMgr.GP_CAMERA+"'}");

                sessionresponse.end();
/*                if (dataitems.length > 1) {
                    if(this.GoPro_TestMgr.GP_EvalCameraName(dataitems[1].toUpperCase()))
                        this.GoPro_TestMgr.GP_CAMERA = dataitems[1].toUpperCase();
                    else
                        console.log("ERROR: Invalid Camera Name:" + dataitems[1].toUpperCase());
                    console.log("NextTest:CAMERA " + this.GoPro_TestMgr.GP_CAMERA);
                    result = this.GoPro_TestMgr.GP_NextTest();
                    console.log("NextTest:" + result);
                }*/
                break;
            case "/ReportStatus"://GoProTestMgr/ReportStatus&runid&caseid&statusid&version&comment
                var testrunID, caseid, statusid, comment,elapse, version;
                var datainfo="";
                for(var i=0;i<dataitems.length;i++)
                    datainfo+=dataitems[i]+"|";
                console.log("ReportStatus dataitems:"+datainfo);
                if (dataitems.length > 2) {
                    try {
                        testrunID = dataitems[1];
                        caseid = dataitems[2];
                        statusid = dataitems[3];//1=passes,2=blocked,3=N/A,4=retest,5=fail
                        if (dataitems.length > 3)
                            comment = dataitems[4];//base64
                        if (dataitems.length > 4)
                            elapse=dataitems[5];
                        if (dataitems.length > 5)
                            version=dataitems[6];

                        console.log("ReportStatus:Params - 1 " + caseid + " - 3 "+statusid+ " - 2 "+comment+ " - 4 "+elapse+ " - 5 "+version);
                        TestRail.TestRail.ReportStatus(sessionresponse,testrunID, caseid, statusid, comment,elapse,version);
                    }
                    catch(err){
                        console.log("ReportStatus:ERROR" + err);
                    }

                    console.log("ReportStatus Done:" + result);
                }
                else
                    this.GoPro_TestMgr.GP_ErrorMsg = "Invalid number of parameters";
                break;

            case "/Reset"://GoProTestMgr/NextTest

                if(this.GoPro_TestMgr.GP_EvalCameraName(dataitems[1].toUpperCase()))
                    this.GoPro_TestMgr.GP_CAMERA = dataitems[1].toUpperCase();
                else
                    console.log("ERROR: Invalid Camera Name:" + dataitems[1].toUpperCase());
                this.GoPro_TestMgr.GP_Reset();
                break;
            case "/SetTestID"://GoProTestMgr/NextTest
                //"add_result_for_case/"+runID+"/"+CaseID
                //{"status_id" : 1,"comment" : "mycomment", "elapsed": 15.3, "version" : "1.2.3"}

                if (dataitems.length > 1) {
                    this.GoPro_TestMgr.GP_SetTestID(dataitems[1]);
                    result=this.GoPro_TestMgr.GP_Test_ID;
                    console.log("SetTestID:" + result);
                }
                else
                    this.GoPro_TestMgr.GP_ErrorMsg = "Invalid number of parameters";
                break;
            case "/getTestCount":
                result = this.GoPro_TestMgr.GP_getTestCount();
                console.log("GP_getTestCount:"+result);
                return "TestCount:"+result;
                break;
            case "/SetReportPath":
                this.GoPro_TestMgr.GP_ReportPath = "";
                if (dataitems.length > 1) {
                    var pathitems;// = new Array();
                    pathitems = dataitems[1].split("+");
                    var newpath=pathitems.join("/");
//                    var pitem;
//                    for(pitem in pathitems)
//                        newpath += "/"+pitem;
                    this.GoPro_TestMgr.GP_ReportPath = newpath;
                    this.GoPro_TestMgr.GP_TestProperties["ReportPath"]=this.GoPro_TestMgr.GP_ReportPath;
                    console.log("GP_SetReportPath:"+this.GoPro_TestMgr.GP_ReportPath );
                }
                result=this.GoPro_TestMgr.GP_ReportPath;
                console.log("GP_SetReportPath:"+result);
                break;
            case "/SetPropertyData":
                if (dataitems.length > 2) {
                    this.GoPro_TestMgr.GP_TestProperties[dataitems[1]]=dataitems[2];
                    result=dataitems[1]+"="+this.GoPro_TestMgr.GP_TestProperties[dataitems[1]];
                    console.log("GP_SetPropertyData:"+result);
                    //log.info("SetPropertyData:"+result );
                }
                break;
            case "/GetPropertyData":
                if (dataitems.length > 1) {
                    result=dataitems[1]+"="+this.GoPro_TestMgr.GP_TestProperties[dataitems[1]];
                    console.log("GP_GetPropertyData:"+result);
                    //log.info("GetPropertyData:"+result );
                }
                break;
            case "/GetTestIndex":
                console.log("GetTestIndex:>");
                if (dataitems.length > 0) {
                    result = this.GoPro_TestMgr.GP_GetTestIndex();
                    console.log("GP_GetTestIndex:"+result);
                    //log.info("GetPropertyData:"+result );
                }
                break;
            case "/GetTestName":
                console.log("GetTestName:>");
                if (dataitems.length > 1) {
                    result = this.GoPro_TestMgr.GP_GetTestName(this.GoPro_TestMgr.GP_GetTestName(dataitems[1]));
                    console.log("GP_GetTestID:"+result);
                    //log.info("GetPropertyData:"+result );
                }
                break;
            default :
                sessionresponse.write("NOT FOUND:"+dataitems[0]);
                sessionresponse.end();
                break;
        }

        //console.log("Current Test:"+this.GoPro_TestMgr.GP_Test_ID+" - "+ this.GoPro_TestMgr.GP_CurrentTestName);
        //console.log("Result:"+result);


    } catch (err) {

        if(err.name)
            console.log("ERROR:GoProTestMgr=" + err.name);
        if (err.message )
            console.log("ERROR:GoProTestMgr=" + err.message);

        console.log("ERROR:GoProTestMgr=" + err);
        result=err;
        sessionresponse.write(err);

        if(this.GoPro_TestMgr.GP_ErrorMsg.length>0) {
            console.log("ERROR:GoProTestMgr=" + this.GoPro_TestMgr.GP_ErrorMsg);
            log.error("GetPropertyData:"+this.GoPro_TestMgr.GP_ErrorMsg+result );

        }
        sessionresponse.end();
    }

    return result;
}
/*if(GoPro_TestMgr===undefined  || GoPro_TestMgr===null)
    this.GoPro_TestMgr=new GoPro_TestMgr();
GoPro_TestMgr.Reset();*/
log.info("###################################");
log.info("Node Server Startup");
//log.info("Run These Tests");

log.info("###################################");

exports.GoProTestMgr = GoProTestMgr;
exports.GoPro_TestMgr=this.GoPro_TestMgr;
