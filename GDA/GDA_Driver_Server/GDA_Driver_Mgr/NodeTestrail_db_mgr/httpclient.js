/**
 * Created by keithfisher on 7/1/14.
 */
var request = require('request');
//var async = require('async');
//var wait = require('waitfor');
//var wait2=require('wait.for-es6');
var Sync = require('sync');

var httpVARS=[];
//var Q = require("q");
//var Return_Data=null;
//var rest = require('restler');
var util = require('./Utils');
//var utils=new util();

function onResponse_get_run(sessionResponse,data) {
    //parsebody(r1)
    console.log(data);

    sessionResponse.write(data);
    sessionResponse.end();
}

function onResponse_get_test(sessionResponse,data) {
    //parsebody(r1)
    console.log("httpclient.onResponse_get_test:"+data);

    sessionResponse.write("httpclient.onResponse_get_test:"+data);
    sessionResponse.end();
}

function onResponse_post_test(sessionResponse,data) {
    //parsebody(r1)
    console.log(data);

    sessionResponse.write(data);
    sessionResponse.end();
}

function HTTPTestRailRequest(sessionResponse,postData,callback){

    HTTPRequest(sessionResponse,EvalPostData(postData),callback);
}

function getObjPropData(obj,propname){
    if(propname in obj)
        return obj[propname];
    else
        return "";
}

function parsebody(body){
    var rc="";
    var item,sitem, i,test;
    //return JSON.stringify(body);
    var obj = JSON.parse(body);
    console.log("NUMBER OF TEST FOUND:"+obj.length)
    for( i = 0; i<obj.length;i++) {
        //console.log(JSON.stringify(body[i]));
        item="\n<br>";
        test=obj[i];
        item=i.toString()+" - "+
            getObjPropData(test,"case_id")+"-"+
            getObjPropData(test,"status_id")+"-"+
            getObjPropData(test,"title")+"<br>";

        //console.log(item);
        rc+=item;
    }
    return rc;
}

function HTTPRequestPost(sessionResponse,url,callback,postdata){
    var Step    = require('step');
    var username = "qaauto1@gopro.com";
    var password = "sdauto1";
    var form=request.form();
    //form.append('status_id','1');
    //form.append('comment','My_comment');
    if(url.indexOf("http") != 0){
        callback(sessionResponse,"Invalid url:"+url);
    }
    console.log(url);
// request returns body as 3rd argument
// we have to move it so it works with Step :(
    request.getBody = function(o, cb){
        request.post(o, function(err, resp, body){
            cb(err, body)
        })
    }
    Step(
        function getData(){
            request.getBody(           {
                headers: {'Content-Type': 'application/json'},
                url : url,
                'auth' : {
                    'username' : username,
                    'password' : password
                }
            }, this.parallel())

        },
        function doStuff(err, r1,r2,r3){
            if(err)
                callback(sessionResponse,err);
            else
                callback(sessionResponse,r1);

        }

    )
}
//'status_id': 1,
//    'comment': 'test_comment'}
function HTTPRequest_Post (sessionResponse,url,callback,statusid,comment,elapse){
    var Step    = require('step');
    var username = "qaauto1@gopro.com";
    var password = "sdauto1";
//    var statid=Number(statusid);
//    var comm =comment.replace("%20"," ");
    //var form=request.form();
    //form.append('status_id','1');
    //form.append('comment','My_comment');
    if(url.indexOf("http") != 0){
        callback(sessionResponse,"Invalid url:"+url);
    }
    console.log(url);

// request returns body as 3rd argument
// we have to move it so it works with Step :(
    request.getBody = function(o, cb){
        request.post(o, function(err, resp, body){
            cb(err, body)
        })
    }
    Step(
        function getData(){
            request.getBody(           {
                headers: {'Content-Type': 'application/json'},
                uri : url,
                'auth' : {
                    'username' : username,
                    'password' : password
                },
                json:{'status_id' :statusid,
                    'comment': comment,'elapsed':elapse
                }

            }, this.parallel())

        },
        function doStuff(err, r1,r2,r3){
            if(err)
                callback(sessionResponse,err);
            else
                callback(sessionResponse,r1);

        }

    )

}

function HTTPRequest (sessionResponse,url,callback,testinfo){
    var Step    = require('step');
    var username = "qaauto1@gopro.com";
    var password = "sdauto1";
    if(url.indexOf("http") != 0){
        callback(sessionResponse,"Invalid url:"+url);
    }
    console.log("URL="+url);
// request returns body as 3rd argument
// we have to move it so it works with Step :(
    request.getBody = function(o, cb){
        request.get(o, function(err, resp, body){
            cb(err, body)
        })
    }
    Step(
        function getData(){
            request.getBody(           {
                headers: {'Content-Type': 'application/json'},
                url : url,
                'auth' : {
                    'username' : username,
                    'password' : password
                }
            }, this.parallel())

        },
        function doStuff(err, r1,r2,r3){
            if(err)
                return callback(sessionResponse,err,testinfo);
            else
                return callback(sessionResponse,r1,testinfo);

        }

    )

}

function SetVARS(){
    httpVARS["get_run"] = "/index.php?/api/v2/get_run/[[RUN_ID]]";
    httpVARS["TestRailURL"] = "https://gopro.testrail.com";
    httpVARS["get_test"] = "/index.php?/api/v2/get_tests/[[RUN_ID]]";
}

function EvalPostData(postData){
    var dataitems = postData.split("&");
    SetVARS();

    var rc = "";
    var url;
    try {
        switch(dataitems[0]) {
            case "get_run":
                if (dataitems.length > 1) {

                    url=SetURL(dataitems[0],dataitems[1]);
                }
                break;
            case "get_test":
                if (dataitems.length > 1) {
                    url=SetURL(dataitems[0],dataitems[1]);
                }
                break;
            default:
                url="HTTPRequest:Invalid " + postData;
                console.log(url);
                break;
        }
    }
    catch (err) {
        console.log("ERROR:HTTPRequest=" + err);
        url=err;
    }
    return url;
}

function SetURL(testrailcmd,runid){
    console.log("Found HTTPRequest:"+testrailcmd + " - " +runid);
    var url=httpVARS["TestRailURL"];
    url+=httpVARS[testrailcmd];
    return url.replace("[[RUN_ID]]",runid);

}
/*

var http = {
    httpClient_User: "qaauto1@gopro.com",
    httpClient_PW: "sdauto1",
    httpClient_url:  "http://www.example.com",
//    httpClient_VARS : [],
//    httpRequest: [],
//    httpAuth: [],
//    httpClient: [],

    httpClient_Init : function(){
        console.log(">>HTTPRequest httpClient_Init:" );
        //var client=require('node-rest-client').Client;

        //this.httpClient_InitVARS();
        //request=require('request'),

        //this.httpAuth = "Basic " + new Buffer(this.httpClient_User + ":" + this.httpClient_PW).toString("base64");
        //this.httpClient = new Client();

        //http=require("http");
        //httpClient_url.url=require("url");
        console.log("<<HTTPRequest httpClient_Init:" );
    },



    evalbody: function(body){
        var rc="";
        var item;
        for(var i = 0; i<body.length;i++) {
            console.log(JSON.stringify(body[i]));
            rc+="\n";
            rc += body[i].toString();
//            for (item in body[i]) {
//                rc += item.toString() + "\n";
//            }
        }
        return rc;
    },

    HTTPRequest: function(sessionResponse,url,callback){
        var Step    = require('step');
        var username = this.httpClient_User;
        var password = this.httpClient_PW;
        var response;
// request returns body as 3rd argument
// we have to move it so it works with Step :(
        request.getBody = function(o, cb){
            request(o, function(err, resp, body){
                cb(err, body)
            })
        }

        Step(
            function getData(){
                request.getBody(           {
                    headers: {'Content-Type': 'application/json'},
                    url : url,
                    'auth' : {
                        'username' : username,
                        'password' : password
                    }
                }, this.parallel())
//                request.getBody({ uri: 'http://api.com/?method=2' }, this.parallel())
//                request.getBody({ uri: 'http://api.com/?method=3' }, this.parallel())
            },
            function doStuff(err, r1,r2,r3){
                if(err)
                    callback(sessionResponse,err);
                else
                    callback(sessionResponse,r1);

            }
        )
        console.log(response);
        return response;
    }


*/
/*
    ReturnData: null,
    testRequest2: function(url,callback){
        var rc ;
        //var request = require('request'); ' // Basic Authentication credentials
        var username = this.httpClient_User;
        var password = this.httpClient_PW;
        //var authenticationHeader = "Basic " + new Buffer(username + ":" + password).toString("base64");
        request(
            {
                headers: {'Content-Type': 'application/json'},
                url : url,
                'auth' : {
                    'username' : username,
                    'password' : password
                }
            },
            function (error, response, body) {

                if(!error){
                    if(response.statusCode == 200) {
                        try {

                            if((typeof body) == "string") {
                                var result = JSON.parse(body);

                                rc = result;
                            } else {
                                rc = body;
                            }
                            ReturnData=rc;
                            //console.log(rc);
                            //console.log(this.ReturnData);
                            // Call callback with no error, and result of request
//                            return callback(null, rc);

                        } catch (err) {
                            rc  =err;
                            // Call callback with error
//                            return callback(err);
                        }
                    }
                }
                else{
                    rc  = error;
//                    return callback(error);
                }
                //console.log(JSON.stringify(body));
                //rc = body;//this.evalbody(body);
                //console.log(body);
                this.ReturnData = rc;
                //Return_Data=rc;
                //console.log(rc);
                //console.log(this.ReturnData);
                //return rc;
            }

        );
*//*
*/
/*        console.log("wait");
        var count=0;
        while(rc === undefined) {
            console.log(rc);
            require('deasync').runLoopOnce();
            this.WaitResult(500);
            count++;
            if(count > 5)break;

        }
        console.log("return");
        this.ReturnData = rc;
        console.log(rc);*//*
*/
/*
        return rc;
*//*
*/
/*        this.httpRequest.get(url,function (error, response, body) {
                if (!error && response.statusCode == 200) {
                    console.log(body) // Print the google web page.
                }}
                ).auth(this.httpClient_User, this.httpClient_PW, false);*//*
*/
/*
    }*//*

*/
/*    getRest: function(url, id){
        console.log("HTTPRequest getRest:" + url);
        this.httpRequest.get(url).auth(this.httpClient_User, this.httpClient_PW, false);
        var http = require('https');

        var options = {
            host: this.GoPro_httpClient.httpClient_VARS["TestRailURL"],
            port: 80,
            path: this.GoPro_httpClient.httpClient_VARS["get_run"].replace("[[RUN_ID]]",id),
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            auth: {'user':'qaauto1@gopro.com','password':'sdauto1'}
        };
        var req = http.request(options, function(res) {
            console.log('STATUS: ' + res.statusCode);
            console.log('HEADERS: ' + JSON.stringify(res.headers));
            res.setEncoding('utf8');
            res.on('data', function (chunk) {
                console.log('BODY: ' + chunk);
            });
        });

        req.on('error', function(e) {
            console.log('problem with request: ' + e.message);
        });

// write data to request body
        req.write('data\n');
        req.write('data\n');
        req.end();

    },*//*

*/
/*    gethttp: function(urlpath){
        var urlOpts = {host: this.httpClient_VARS["TestRailURL"], path: urlpath, port: '80'};
        this.httpRequest.get(urlOpts, function (response) {
            response.on('data', function (chunk) {
                console.log(chunk.toString());
                return chunk.toString();
            });
        }).on('error', function (e) {
            console.log('error:' + e.message);
            return "ERROR: "+ e.message;
        });
    },*//*


*/
/*

    HTTPRequestcallback : function(err, body){
        console.log("HTTPRequestcallback");
        this.ReturnData=body;
        console.log(body);
        return body;
    },

    Dummy: function(){
        if(typeof this.ReturnData !== "undefined")
            console.log("Dummy"+this.ReturnData);
    },
    Sleep: function(ms){
        var ret;
        console.log("Sleep-->"+ms.toString());
        setTimeout(function(){
            ret = "DONE";
            console.log("Sleep<--"+ret);
        },ms);
        while(ret === undefined) {
            console.log(".");
            require('deasync').runLoopOnce();
        }
    },
*//*


*/
/********************************************
     *
     * @return {string}
     * @return {string}
     *//*

*/
/*     HTTPRequest: function(response, postData, callback) {

        //console.log("HTTPRequest Session:" + session);
        console.log("HTTPRequest postData:" + postData);


        var dataitems = postData.split("&");

        var result;
        var rc = "";
        var url;
        try {
            switch(dataitems[0]) {
                case "get_run":
                    console.log("FOUND: HTTPRequest:run_id " + postData);
                    if (dataitems.length > 1) {
                        console.log("HTTPRequest:run_id " + postData);
                        rc=this.httpClient_VARS["TestRailURL"];
                        rc+=this.httpClient_VARS["get_run"];
                        rc=rc.replace("[[RUN_ID]]",dataitems[1]);
                        console.log("HTTPRequest: " + rc);
                        result = this.testRequest(rc,callback);
                        console.log("HTTPRequest:Result " + result);
                    }
                    break;
                case "get_test":
                    console.log("FOUND: HTTPRequest:run_id " + postData);
                    if (dataitems.length > 1) {
                        console.log("HTTPRequest:run_id " + postData);
                        url=this.httpClient_VARS["TestRailURL"];
                        url+=this.httpClient_VARS["get_test"];
                        url=url.replace("[[RUN_ID]]",dataitems[1]);
                        console.log("HTTPRequest: " + url);
                        this.ReturnData = null;
                        result=this.testRequest(url,callback);

//                        console.log("wait");
//                        var count=0;
//                        process.nextTick();
*//*
*/
/*                        while(this.ReturnData === null) {
                            process.nextTick();
                            console.log(this.ReturnData);
                            require('deasync').runLoopOnce();
                            this.WaitResult(500);
                            count++;
                            if(count > 5)break;

                        }*//*
*/
/*
                        //result = this.ReturnData;
//                        console.log("return");



                        //require('deasync').runLoopOnce();
                        //this.Sleep(10000);
                        //require('deasync').runLoopOnce();
//                        setTimeout(this.testRequest(rc), 10000);

//                        var counter=0;
//                        while(typeof this.ReturnData === "undefined" ||
//                            this.ReturnData === null){
//                            counter++;
//                            setTimeout(this.Dummy,10000);
//
//                            //console.log("HTTPRequest:WAIT" + this.ReturnData );
//                            //setTimeout(this.testRequest(rc,function(err, body) {this.ReturnData=body;console.log("HTTPRequest:ReturnData " + this.ReturnData);return body;})), 10000);
//                        }

*//*
*/
/*                        console.log("HTTPRequest:Result " +result);
//                        for(var i=1;i<100;i++) {
                            if (result ===undefined ) {

                                console.log("HTTPRequest:WAIT undefined"  );
                                //result = "FAILED:HTTPRequest Result undefined: body ";
                                return result;
                            }
                            else {
                                //result = this.ReturnData;
                                console.log("HTTPRequest:Result body " + result);
                                //result=this.evalbody(result);
                                console.log("HTTPRequest:Result " + result);
                                return result;
                            }*//*
*/
/*
//                        }


                    }
                    break;
                default:
                    result="HTTPRequest:Invalid " + postData;
                    console.log(result);
                    break;

            }

        }
        catch (err) {
            console.log("ERROR:HTTPRequest=" + err);
            result=err;
        }

            //return result;
    }*//*


}
*/

/*

function HTTP_Request(response, postData, callback) {

    console.log("HTTP_Request Start");
    if(typeof this.GoPro_httpClient === "undefined") {
        console.log("undefined GoPro_httpClient");
        this.GoPro_httpClient = Object.create(GoPro_httpClient);
        console.log("undefined GoPro_httpClient");
        this.GoPro_httpClient.httpClient_Init();
    }
    console.log("GoPro_httpClient.HTTPRequest");
    this.GoPro_httpClient.HTTPRequest(response, postData, callback);
    console.log("DONE HTTP_Request");
}
var httpResponseData="";
function HTTP_Done(response){
    //GoPro_httpClient.CallBackRequestDone(response);
    httpResponseData = response;
    console.log(httpResponseData);
    //docallback(response);
};
*/


//this.GoPro_httpClient.httpRequest=require('request');
//exports.GoPro_httpClient=this.GoPro_httpClient;
//exports.GoPro_httpClient.httpClient_Init=this.GoPro_httpClient.httpClient_Init;
//exports.http = http;

//module.exports.GoPro_httpClient = this.GoPro_httpClient;
//exports.httpResponseData = httpResponseData;
//exports.ReturnData = GoPro_httpClient.ReturnData;

//this.httpClient.Init();

//exports.HTTPRequest=HTTPRequest;
//exports.SetURL=SetURL;
exports.HTTPTestRailRequest=HTTPTestRailRequest;
exports.onResponse_get_test=onResponse_get_test;
exports.onResponse_post_test=onResponse_post_test;
exports.HTTPRequest=HTTPRequest;
exports.HTTPRequest_Post=HTTPRequest_Post;