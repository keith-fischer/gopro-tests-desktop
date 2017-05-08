
var settings = require('./settings.js');
settings.expressPort; //this will be equal to 3000 for local env
var counter = 0;

var utils = require('./Utils');
var TestRail = require("./TestRail");
var JSON2 = require('JSON2');
utils.UtilFN.debug = true;
console.log(utils.UtilFN.UtilFN_WhatPlatformMacOrWin());
var CameraTTYpath = "/usr/bin/screen"
var CamTTY = require('./CameraTTY');
var properties={};


/*************************************************
 * CameraTTY
 * set process connection to camera CamTTY
 * keep CamTTY alive and after browser session is closed
 * subsequent browser cmds and to access CamTTY
 * Detect if CamTTY is connected and on failure to kill and restart CamTTY
 * One camera per host
 * Reset camera
 * Reset wifi
 * SetBuffer max_size or none default
 * GetBuffer up to max buffer size
 *
 *
 **************************************************/
function CameraTTY(response, request, urlData, postData, session){
    counter++;
    console.log("CameraTTY Session:" + session);
    console.log("CameraTTY postData:" + postData);
    var appargs = "/dev/tty.SLAB_USBtoUART 115200".split(" ");
    //var arg = new Array();
    var arg = postData.split("?");
    response.writeHead(200, {
        "Content-Type" : "text/html"
    });
    response.write("<p>Session=" + session + ":CameraTTY</p>");
    response.write("<p>"+CameraTTYpath+"<p>");
    response.write("<p>"+appargs+"<p>");
    var util = require('util'),
        spawn = require('child_process').spawn,
        ls = spawn(CameraTTYpath, arg);
    console.log('CameraTTY Session=' + session +' - Spawned child pid: ' + ls.pid);

    var responseOut="";

    ls.stdin.on('data', function (data) {
        console.log('stdin: ' + data);
        responseOut+=data;
        response.write("<p>stdin:"+data+"<p>");
    });

    ls.stdout.on('data', function (data) {
        console.log('stdout: ' + data);
        responseOut+=data;
        response.write("<p>stdout:"+data+"<p>");
    });

    ls.stderr.on('data', function (data) {
        console.log('stderr: ' + data);

        response.writeHead(200, {
         "Content-Type" : "text/html"
         });

         responseOut+=data;
         response.write("<p>stderr: "+data+"<p>");
         //response.write("<p>stderr:" + "CameraTTYpath</p>child process exited with code " );
         //response.end();
         //ls.stdin.end();
         });

         ls.on('exit', function (code) {
         console.log('Session:' + session + '- child process exited with code ' );
         response.write("<p>"+responseOut+"<p>");
         response.write("<p>Session:" + session + " - CameraTTYpath</p>child process exited with code " );
         response.end();
         //ls.stdin.end();
    });
         //return response;
}



/*************************************************
 * parse post data for runid
 * fetch from testrail the complete testrun with runid
 * iterate the testrun and query with case_id
 * if found get the 'custum_steps' and set the testcase custom_steps
 * forward the testrun json into the response
 * example request:  http://127.0.0.1:8888/gettestrun/runid=11891
**************************************************/
function gettestrun(response, request, urlData, postData, session){
    console.log("gettestrun Session:" + session);
    console.log("gettestrun postData:" + postData);
    console.log("gettestrun urlData:" + urlData);
    var cmds = urlData.split("/");
    response.writeHead(200, {"Content-Type": "application/json"});
    var runid = -1;
    if (cmds.length>0){// cmd data found
        for(var cmd in cmds){
            if(cmds[cmd].indexOf("runid=")==0){
                runid = cmds[cmd].split("=")
                if(runid.length > 1) {
                    runid = runid[1];
                    if(runid == "0")
                        runid = "12394"; //cloud 11891  internal 12394
                    //mongoUT.domongotest(response);
                    TestRail.TestRail.GetTestSuite(response,runid);

                }
            }
        }
    }
    else{//invalid data
        var jsonres = JSON.stringify({error: 'No command data'})

        response.writeHead(200, {
                "Content-Type": "application/json",'Content-Length': jsonres.length}
        );

        response.write(jsonres);
        response.end();
    }

}

//http://127.0.0.1:8888/reporttestcase/runid=11891
function reporttestcase(response, request, urlData, postData, session){
    console.log("reporttestcase Session:" + session);
    console.log("reporttestcase postData:" + urlData);

    response.writeHead(200, {"Content-Type": "application/json"});

    if (request.method == 'POST') {// cmd data found
        if(postData !== undefined && postData !== null) {
            //var cleaned =  utils.UtilFN.StrReplace(postData,"\n","");
            //utils.UtilFN.UtilFN_WriteToFile("/automation/appium/lastpostdata.txt", postData);
            //var ss = JSON.stringify(postData);//{"id":2961782,"case_id":539177,"status_id":3,"run_id":11891,"dog":"woof"});
            //var s1 =  ss.replace("[object Object]","");
            var test =  postData;//JSON.parse(ss);
            if (test !== undefined && test !== null) {
                var testresult;
                try {
                    testresult = TestRail.TestRail.EvalReport(test);
                }
                catch(err){
                    var msg = JSON.stringify({error: 'FAILED TestRail.TestRail.EvalReport: No data to report \n'+ err});

                    response.writeHead(200, {
                            "Content-Type": "application/json"}
                    );

                    response.write(msg);
                    response.end();
                    return;
                }
                if(testresult){
                    try{
                        if(testresult['case_id'] === undefined || testresult['run_id'] === undefined || testresult['status_id'] === undefined ){

                            var s = "FAILED Invalid testrail data  case_id="+testresult['case_id'].toString()+" run_id="+testresult['run_id'].toString()+" status_id="+testresult['status_id'].toString();
                            var msg = JSON.stringify({error: s});
                            console.log(msg);
                            response.writeHead(200, {
                                    "Content-Type": "application/json"}
                            );

                            response.write(msg);
                            response.end();
                            return;
                        }
                        else{//valid
                            try {
                                TestRail.TestRail.ReportStatus(response, testresult['run_id'].toString(), testresult['case_id'].toString(), testresult['status_id'].toString(), testresult['resultmsg'], null, "1.2.3");
                                console.log("TESTRAIL: " +   " runid=" + testresult['run_id'].toString() + " caseid=" + testresult['case_id'].toString() + " statusid=" + testresult['status_id'].toString());
                            }
                            catch(err){
                                var msg = JSON.stringify({error: 'FAILED TestRail.TestRail.ReportStatus: \n'+ err});
                                console.log(msg);
                                console.log("TESTRAIL: " +   " runid=" + testresult['run_id'].toString() + " caseid=" + testresult['case_id'].toString() + " statusid=" + testresult['status_id'].toString());

                                response.writeHead(200, {
                                        "Content-Type": "application/json"}
                                );

                                response.write(msg);
                                response.end();
                            }
                        }
                    }
                    catch(err){
                        var msg = JSON.stringify({error: 'FAILED TestRail.TestRail.EvalReport: No data to report \n'+ err});

                        console.log(msg);
                        response.writeHead(200, {
                                "Content-Type": "application/json"}
                        );

                        response.write(msg);
                        response.end();

                    }
                }else{
                    var msg = JSON.stringify({error: 'FAILED TestRail.TestRail.EvalReport: returned null'});
                    console.log(msg);
                    response.writeHead(200, {
                            "Content-Type": "application/json"}
                    );

                    response.write(msg);
                    response.end();
                    return;
                }
/*                //for (var key in Object.keys(test)){
                //    var t = Object.keys( test )[key];
                //    try {
                //        console.log(t + " value =: " + test[t]);
                //    }
                //    catch(err){
                //        console.log(t + " value =: " + err);
                //    }
                //}
                //var tt = {"id":2961782,"case_id":539177,"status_id":3,"run_id":11891,"dog":"woof"};


                //var temp = JSON.parse(postData);  //utils.UtilFN.ShowObject(test);//["run_id"]
                //var runid = test["run_id"]; //utils.UtilFN.getStrBetween(test,"\"run_id\"",",");//"11891";//utils.UtilFN.getFieldData(test, "run_id");
                //var caseid = test["case_id"];//utils.UtilFN.getStrBetween(test,"\"case_id\"",",");//"539177";//utils.UtilFN.getFieldData(test, "case_id");
                //var fail = test.indexOf("\"status\":\"failed\"");//"status": "failed"
                //var statusid = "5";
                //
                //var comment = "";
                //var pf = "PASSED";
                //if(fail<0){//not found, try this
                //    fail = test.indexOf("\"status\": \"failed\"");
                //}
                //if(fail<0){//passed
                //    statusid="1";
                //}
                //else{//failed
                //    comment = utils.UtilFN.getStrBetween(test,"\"error_message\":","\"duration\"");
                //    pf = "FAILED";
                //}
                //
                //var elapse = null;
                //var ver = "1.2.3";
                //
                //if (runid.length==0 || caseid.length==0){
                //    console.log("Invalid run_id or case_id");
                //    response.write("Invalid run_id or case_id");
                //    console.log(postData);
                //    response.end();
                //}
                //else {
                //    console.log("TESTRAIL: " + pf + " PostLen=" + ss.length.toString() + " runid=" + runid + " caseid=" + caseid + " statusid=" + statusid);
                //
                //
                //    //ReportStatus: function(sessionresponse,runid, caseid, statusid, comment,elapsed,version){
                //    //TestRail.TestRail.ReportStatus(response, runid, caseid, statusid, comment, elapse, ver);
                //}
                //response.write(JSON.stringify(testreportresponse));*/
            }

            response.end();

        }
        else{//invalid postdata
            var msg = JSON.stringify({error: 'No postdata'});
            console.log(msg);
            response.writeHead(200, {
                    "Content-Type": "application/json",'Content-Length': jsonres.length}
            );

            response.write(msg);
            response.end();
        }
    }
    else{//invalid data
        var msg = JSON.stringify({error: 'request.method type is not\'POST\''});
        console.log(msg);
        response.writeHead(200, {
                "Content-Type": "application/json",'Content-Length': jsonres.length}
        );

        response.write(msg);
        response.end();
    }

}
//***************************************************************
//***************************************************************


exports.gettestrun=gettestrun;
exports.reporttestcase=reporttestcase;
exports.CameraTTY=CameraTTY;