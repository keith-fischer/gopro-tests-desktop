/**
 * Created by keithfisher on 4/23/14.
 */
//fs = require('fs');
var fs    = require('fs'),
    properties = require('nconf');

var UtilFN = {
    debug:false,
    debuglog:function(msg){
        if(this.debug==true){
            console.log(msg);
        }
    },
    getSubString: function (txt, lb, rb) {
        try {
            txt.split(lb)[1].split(rb)[0];
        }
        catch(err){

        }

    },

    getStrBetween: function (txt, lb, rb) {
        try {
            var a = txt.indexOf(lb);
            if(a<0)
                return "";
            var b = txt.indexOf(rb,a+1);
            if(b<0)
                return "";
            var aa = a+lb.length;
            return txt.substr(aa+1,b-aa-1);
        }
        catch(err){
            return "";
        }

    },

    StrReplace: function (txt, oldstr, newstr) {
        var rc, s1, s2, s3;
        s2 = txt;
        do
        {
            s1 = s2;
            s2 = s1.replace(oldstr, newstr);

        } while (s1 != s2)
            rc = s2;
        return rc;
    },
    //curl -H "Content-Type: application/json" -u "qaauto1@gopro.com:sdauto1" https://gopro.testrai.com/index.php?/api/v2/get_tests/6889

    //CURL: function (headerurl,apicmd, runid){
    //    var response;
    //
    //
    //    return response;
    //},
    StrHasData: function(str){
        var rc=false;
        if ((typeof str === 'undefined') ||
            (str.length == 0))
            return rc;
        else
            rc=true;

        return rc;
    },

    StrToBase64: function(str){
        if(this.UtilFN_StrHasData(str)) {
            strb64 = new Buffer(str).toString('base64');
            return strb64;
        }
        return "";

    },

    Base64ToStr: function(b64){
        var b64str = "";
        if(this.StrHasData(b64)) {
            b64str = new Buffer(b64, 'base64').toString('ascii');
            return b64str;
        }
        return b64str;
    },

    Pad0: function(str){
        if(typeof(str) === undefined)
            return "";
        else if(typeof(str) === String)
            str= str.toString();
        if(len(str)==1)
            return "0"+str;
        else
            return str;
    },

    EvalStrToDefault: function(teststr,defaultvalue){
        try{
            if(teststr.length>0)
                return teststr;
        }
        catch(err){
            return defaultvalue;
        }
    },

    GetDateTimeNow: function(){

        var dt=new Date();
        var rc=this.Pad0(dt.getYear());
        rc+=this.Pad0(dt.getMonth())
        rc+=this.Pad0(dt.getDay())+"_";
        rc+=this.ad0(dt.getHours());
        rc+=this.Pad0(dt.getMinutes());
        rc+=this.Pad0(dt.getSeconds());

        return rc;
    },

    ShowObject:function (obj) {
        //LOG("ShowObject:" + obj);
        var br ="<br>";
        var proplist = "";
        for (var x1 in obj) {
            try {
                proplist += br+"\n------\n"+br + obj[x1].toString();
                proplist += br+"\n------\n"+br + obj[x1].name();
            }
            catch(err1) { }

            for (var x2 in obj[x1]) {
                try {
                    proplist += br+"\n\t" + obj[x1][x2].toString();
                    proplist += br+"\n\t" + obj[x1][x2].name();
                }
                catch (err2) { }
            }
        }

        return proplist;
    },

    getFieldData:function(obj,propname,defaultval){
        if(obj!=undefined) {
            if (obj.hasOwnProperty(propname))
                return obj[propname];
            else
                return defaultval;
        }
        else
            return defaultval;
    },

    getObjPropData:function(obj,propname){
        if(propname in obj)
            return obj[propname];
        else
            return "";
    },

    getMinutesBetweenDates:function (startDate, endDate) {
        var diff = endDate.getTime() - startDate.getTime();
        return Math.round(diff / 60000);
    },

    UtilFN_WhatPlatformMacOrWin: function(){
        return process.platform;//darwin(Mac),linux,windows
    },

    LastError: "",

    UtilFN_GetUrlData: function(postData){
        try {
            this.LastError = "";
            var dataitems = postData.split("/");
            var lastitem = dataitems[dataitems.length];
            var jsonstr = this.Base64ToStr(lastitem);
            return JSON.stringify(jsonstr);
        }
        catch(err){
            console.log(err);
            this.LastError=err;
        }

    },

    UtilFN_Sleep: function(ms){
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

    UtilFN_WriteToFile: function(path,txt){
        var rc = false;
        try {
            fs.writeFileSync(path, txt);
            rc=true;
        }
        catch(err){
            console.log(err);
        }
        /*, function (err) {
         if (err){
         console.log(err);

         }
         else{
         console.log("UtilFN_WriteToFile > "+path);
         rc= true;

         }
         });*/
        return rc;
    },
    /*********************
     *
     *
     * @param arrayIn  overwrites existing key- values
     * @returns {*}
     * @constructor
     */
    UtilFN_getArgs: function(arrayIn){
        console.log("args -----------");

        var i, key="";
        process.argv.forEach(function(val, index, array) {

            console.log(index + ': ' + val);
            if(val == undefined)
                key="";
            else if(key.length==0 && val.indexOf('-')==0){
                key = val;
            }
            else if(key.length>0 && val.length>0){
                arrayIn[key]=val;
                key="";
            }
            else
                key="";

        });
        for (i in arrayIn){
            console.log(i);
            for (ii in arrayIn[i]){
                console.log( ii + ": " + arrayIn[i][ii]);
            }
        }

        console.log("args -----------");
        return arrayIn;
    }
}

properties.argv().env();
properties=UtilFN.UtilFN_getArgs(properties);
exports.UtilFN = UtilFN;
exports.properties=properties;