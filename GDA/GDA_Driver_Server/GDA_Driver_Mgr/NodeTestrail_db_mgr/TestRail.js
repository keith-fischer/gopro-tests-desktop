/**
 * Created by keithfisher on 4/25/14.
 */
var httpclient = require("./httpclient");
var logger = require('./logger');
//var testClients = require("./Archive/TestRunSession");
var log=logger.LOG;
//Test_Rail=new TestRail();
//Test_Rail.Test_Testrail();
var utils = require('./Utils');
var mongo = require("./mongo");
var mongoUT = require("./mongoUtils");

var TestRail = {
    TestSessions: [],
    TestRail_VARS: [],
    TestRun: [],
    TestIndex: -1,
    Ready:false,
    APIURL: "",
    /************
     * UseLocalCache
     * to be considered later
     * cache to local file until testrail api connectivity is detected
     */
    UseLocalCache: false,
    ErrorMsg: "",
    Login: "qaauto1@gopro.com",
    PW: "sdauto1",
    URLCloud: "https://gopro.testrail.com/index.php?/api/v2/",
	URL: "https://us01-testrail-01v/index.php?/api/v2/",
 /*   TR: rest.service(function (u, p) {
        this.defaults.username = u;
        this.defaults.password = p;
        }, {
            baseURL: URL
        }, {
            update: function (message) {
                return this.post('/statuses/update.json', { data: { status: message } });
        }
    }),
*/
    Init: function () {
        // create a service constructor for very easy API wrappers a la HTTParty...
        //TR = new TR(Login, PW);
       Ready=true;
    },

    /***************************************************************************
     SetURL: With the give testrailapi set the appropriate url with parameters
     ****************************************************************************/
    InitVARS: function(){
        if(this.Ready==true)
            return;
        console.log(">>HTTPRequest httpClient_InitVARS:" );
        this.TestRail_VARS["get_run"] = "/index.php?/api/v2/get_run/[[RUN_ID]]";//gets testrun stats
        //this.TestRail_VARS["TestRailURL"] = "https://gopro.testrail.com";
	    this.TestRail_VARS["TestRailURL"] = "http://us01-testrail-01v/testrail";
        this.TestRail_VARS["get_test"] = "/index.php?/api/v2/get_tests/[[RUN_ID]]";//fetch entire testrun suite
        //"add_result_for_case/"+runID+"/"+CaseID
        //{"status_id" : 1,"comment" : "mycomment", "elapsed": 15.3, "version" : "1.2.3"}
        this.TestRail_VARS["settest_statusid_post"]="{'status_id' : [[status_id]],'comment' : '[[comment]]'}";//, elapsed: '[[elapsed]]', 'version' : '[[version]]'}";
        this.TestRail_VARS["settest_statusid"] = "/index.php?/api/v2/add_result_for_case/[[RUN_ID]]/[[CASE_ID]]";
        console.log("<<HTTPRequest httpClient_InitVARS:" );
        this.Ready=true;
    },
/*
    httpResponseCB_get_run: function(sessionResponse,testrailResponse){
        if(utils.isError(testrailResponse)){
            sessionResponse.write("ERROR: "+testrailResponse);
            sessionResponse.end();
        }
        else{
            this.TestRun=JSON.parse(testrailResponse);
            sessionResponse.write("Found Tests: "+this.TestRun.length.toString());
            sessionResponse.end();
        }
    },
*/

    SetURL: function (testrailcmd,runid,caseid){
        console.log("SetURL:"+testrailcmd + " - " +runid);
        var url=this.TestRail_VARS["TestRailURL"];
        url+=this.TestRail_VARS[testrailcmd];
        if(caseid===undefined)
            url= url.replace("[[RUN_ID]]",runid);
        else
            url= url.replace("[[RUN_ID]]",runid).replace("[[CASE_ID]]",caseid);
        console.log("SetURL:"+url);
        return url;
    },
/*
    SetPostData: function(testrailcmd,statusid, comment,elapsed,version){
        statusid=utils.UtilFN.EvalStrToDefault(statusid,"0");
        comment=utils.UtilFN.EvalStrToDefault(comment,"Automation");
        elapsed=utils.UtilFN.EvalStrToDefault(elapsed,"-1");
        version=utils.UtilFN.EvalStrToDefault(version,"Ver0");
        console.log("SetPostData:"+testrailcmd + " - " +statusid+ " - " +version+ " - " +comment);

        var post=this.TestRail_VARS[testrailcmd];
        //"{'status_id' : [[status_id]],'comment' : [[comment]], 'elapsed': [[elapsed]], 'version' : [[version]]}";
        post= post.replace("[[status_id]]",statusid)
            .replace("[[comment]]",comment)
            .replace("[[elapsed]]",elapsed)
            .replace("[[version]]",version);
        console.log("SetPostData:"+post);
        return post;
    },
*/

     onResponse_get_testrun: function(sessionResponse,data,runid) {
         var res="";
         //sessionResponse.write("TestRail.onResponse_get_test:");
		  console.log("onResponse_get_testrun="+runid);
         try{
		 if(data == undefined || data == null){
			console.log("FAILED: data=null");
		 }
		 else{
			console.log(data);
             TestRail.TestRun=JSON.parse(data);
			 
             res="{'TestCount': "+ TestRail.TestRun.length+"}";
			 console.log(res);
             //var dbname = 'db_BAWAP1Android'; //'db_suite_8554';
             //var collectionName = 'col_BAWAP1Android';//'suite_8554';
			  mongoUT.getTestcaseSteps(sessionResponse,"127.0.0.1","27017",'db_BAWAP1Android','col_BAWAP1Android',data);
         }
		 }
         catch(err){
             res="{'Error': "+ err+"}";
			 sessionResponse.write("TestRail.onResponse_get_test:"+res);
			 sessionResponse.end();
			 console.log("TestRail.onResponse_get_test:"+res);
         }
         //var token=testClients.AddSession(runid,TestRail.TestRun);

         //var testrunlist = JSON.parse(data);
         //returntests = JSON.parse("{\"error\": \"Mongo database connection problem\"}");
         //mongoUT.getTestcaseSteps(sessionResponse,"127.0.0.1","27017",'db_suite_8554','suite_8554',data)
         //mongo.getTestcaseSteps(mongo.doTeststeps,sessionResponse, "",data,runid);
         //sessionResponse.write("TestRail.onResponse_get_test:"+res);
        //sessionResponse.write(returntests); // JSON.stringify(data));
        // console.log("TestRail.onResponse_get_test:"+JSON.stringify(returntests));
        // console.log("TestRail.onResponse_get_test:"+res);
        //sessionResponse.end();

    },

    onResponse_test_status: function(sessionResponse,data) {
        var res="";
        try{
            //TestRail.TestRun=JSON.parse(data);
            res=JSON.stringify(data);//"{'ReportStatus': "+ data+"}";
        }
        catch(err){
            res="{'Error': "+ err+"}";
        }

        console.log(data);
        console.log(res);
        sessionResponse.write(res);
        sessionResponse.end();
    },

    ReportStatus: function(sessionresponse,runid, caseid, statusid, comment,elapsed,version){
        this.InitVARS();
        var urlapi="settest_statusid";
        var url = this.SetURL(urlapi,runid,caseid);
        urlapi="settest_statusid_post";
        //var postdata =this.SetPostData(urlapi,statusid,comment,elapsed,version);
        //console.log("POST:"+postdata);
        var statid=Number(statusid);
        var comm =comment.replace("%20"," ");
        httpclient.HTTPRequest_Post(sessionresponse,url,TestRail.onResponse_test_status,statid,comm,elapsed);
    },

    EvalReport: function(test){
        var resultdata={};
        resultdata['run_id']=test.run_id;
        resultdata['case_id']=test.case_id;
        resultdata['steps']= test['test_results'][0][0]['elements'][0]['steps'];
        resultdata['failstep']=undefined;
        resultdata['cucsteps']="";
        for(stepitem in resultdata['steps']){
            resultdata['cucsteps']+="\n"+utils.UtilFN.getFieldData(resultdata['steps'][stepitem],"keyword","")+
            " "+utils.UtilFN.getFieldData(resultdata['steps'][stepitem],"name","");
            var temp = resultdata['steps'][stepitem]["result"];
            if(temp['status']=="failed"){
                resultdata['failstep'] = resultdata['steps'][stepitem];
                resultdata['failinfo'] = "\nError line "+ resultdata['failstep']['line'] +" - "+ resultdata['failstep']['match']['arguments'][0]['offset'];
                resultdata['failinfo'] += "\nValue = "+resultdata['failstep']['match']['arguments'][0]['val'];
                resultdata['failinfo'] += "\nFile = "+resultdata['failstep']['match']['location'];
                resultdata['failinfo'] += "\nLog: \n" + temp['error_message'];
                break;
            }
        }
        if(resultdata['failstep'] === undefined){
            resultdata['status_id'] = '1';
            resultdata['resultmsg'] = "Reported by automation."
        }
        else{
            resultdata['status_id'] = '5';
            resultdata['resultmsg'] = "\n"+resultdata['cucsteps'] +"\n" + resultdata['failinfo']+"\n"+resultdata['failstep'];
        }

        return resultdata;
    },

    GetTestSuite: function(sessionresponse,runid){
        this.InitVARS();
        var urlapi="get_test";
        var url = this.SetURL(urlapi,runid);
        httpclient.HTTPRequest(sessionresponse,url,TestRail.onResponse_get_testrun,runid);
        TestRail.TestIndex=-1;
    },

    GetNextTest: function(camera){
        var i,test,testname,found;
        console.log("GetNextTest:"+TestRail.TestRun.length);
        TestRail.TestIndex++;
        found=-1;
        test=null;
        for( i = TestRail.TestIndex; i<TestRail.TestRun.length;i++) {


            test=TestRail.TestRun[i];
            console.log(JSON.stringify(test));
            testname=utils.UtilFN.getObjPropData(test,"title").toUpperCase();
            console.log(testname);
            if(testname.length>0){
                found=i;
                break;
            }
/*
            item=i.toString()+" - "+
                getObjPropData(test,"case_id")+"-"+
                getObjPropData(test,"status_id")+"-"+
                getObjPropData(test,"title")+"<br>";
*/

        }
        if(found>-1){
            TestRail.TestIndex=i;
            console.log("GetNextTest:"+test.title);
        }
        else{
            test=null;
            console.log("GetNextTest:NOT FOUND");
        }

        return test;
    },

    //Check if there is connectivity and if the runid is valid
    IsTestRailConnected: function (runid) {
        this.UseLocalCache = true;
        //ping testrail and verify runid is ok.
        //set UseLocalCache=false
        return !this.UseLocalCache;
    },
    GoProTestRailMgr: function(sessionResponse, cmd,data ) {


        //console.log("TestRail Session:" + session);
        //console.log("TestRail postData:" + postData);

        //var dataitems = new Array();
        //dataitems = postData.split("&");

        var result="";// = [];
        this.TestRail.ErrorMsg="";
        try {
            switch(cmd) {
                case "NextTest":

                    break;
                case "TestResult"://http

                    break;
                case "LoadTestRunID"://http get_test

                    break;
                case "TestRunStatus"://http get_runid

                    break;
                /*            case "SetRunID":
                 TestRail.Test_Testrail();
                 break;
                 case "getTestCaseTitle":

                 break;
                 case "getNextTestCase":

                 break;
                 case "getNextTestSuite":

                 break;*/
            }

            //console.log("Current Test:"+this.GoPro_TestMgr.Test_ID+" - "+ this.GoPro_TestMgr.CurrentTestName);
            console.log("Result:"+result);


        } catch (err) {
            console.log("ERR:TestRail=" + err);
            result=err;
            if(this.TestRail.ErrorMsg.length>0)
                console.log("ERR:TestRail=" + this.TestRail.ErrorMsg);
        }

    }

};



/*
function GoProTestRailMgr(response, postData, session) {


    console.log("TestRail Session:" + session);
    console.log("TestRail postData:" + postData);

    var dataitems = new Array();
    dataitems = postData.split("%7C");

    var result="";// = [];
    this.TestRail.ErrorMsg="";
    try {
        switch(dataitems[0]) {
            case "NextTest":

                break;
            case "Reset":

                break;
            case "SetStatusID":

                break;
            case "GetStatusID":

                break;
            case "SetRunID":
                TestRail.Test_Testrail();
                break;
            case "getTestCaseTitle":

                break;
            case "getNextTestCase":

                break;
            case "getNextTestSuite":

                break;
        }

        //console.log("Current Test:"+this.GoPro_TestMgr.Test_ID+" - "+ this.GoPro_TestMgr.CurrentTestName);
        console.log("Result:"+result);


    } catch (err) {
        console.log("ERR:TestRail=" + err);
        result=err;
        if(this.TestRail.ErrorMsg.length>0)
            console.log("ERR:TestRail=" + this.TestRail.ErrorMsg);
    }


    return result;
}
*/

exports.TestRail = TestRail;
