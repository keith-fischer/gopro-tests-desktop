/**
 * Created by keithfisher on 11/25/14.
 */
var Db = require('mongodb').Db,
    MongoClient = require('mongodb').MongoClient,
    Server = require('mongodb').Server,
    ReplSetServers = require('mongodb').ReplSetServers,
    ObjectID = require('mongodb').ObjectID,
    Binary = require('mongodb').Binary,
    GridStore = require('mongodb').GridStore,
    Grid = require('mongodb').Grid,
    Code = require('mongodb').Code,
    BSON = require('mongodb').pure().BSON,
    assert = require('assert');
var async = require('async');
var myCollection;
var db;
var dbname = 'db_BAWAP1Android'; //'db_suite_8554';
var collectionName = 'col_BAWAP1Android';//'suite_8554';
//var utils = require('./Utils');
function removeDocument(d1,d2,d3,onRemove){
    myCollection.findAndModify({name: "doduck"}, [], {remove:true}, function(err, object) {
        if(err)
            throw err;
        console.log("document deleted");
        onRemove();
    });
}

function findDocument(d1,onFinded){
    //{"name" : "doduck", "company.officialName" : "doduck LTD" }
    var cursor = myCollection.find(d1);
    cursor.each(function(err, doc) {
        if(err)
            onFinded(null,doc);
        else if(doc==null)//not found
            onFinded(null,null);


        //console.log("document find:");
        //console.log(doc.name);
        //console.log(doc.company.employed);
        else //found match
            onFinded(null,doc);
    });
}

function findOneDocument(q, onFinded){
    myCollection.findOne(q, function(err, document){
        if(err)
            onFinded(err,null);
        if(document){
            //console.log(JSON.stringify(q)+"  doc is null")
            onFinded(null,document);
        }
        else{
            //console.log("found")
            onFinded(null,null);
        }

        //console.log("document find:");
        //console.log(doc.name);
        //console.log(doc.company.employed);

    });
}

function fieldComplexeUpdateDocument(q1,q2,q3,q4,onUpdate){
    myCollection.update(q1, q2, q3, function(err) {
        if(err)
            throw err;
        console.log('entry updated');
        onUpdate();
    });
}

function fieldUpdateDocument(d1,d2,d3,onUpdate){
    myCollection.update(d1, d2, d3, function(err) {
        if(err)
            throw err;
//        console.log('entry updated');
        onUpdate();
    });
}

function simpleUpdateDocument(d1,d2,d3,onUpdate){
    myCollection.update(d1, d2, d3, function(err) {
        if(err)
            throw err;
//        console.log('entry updated');
        onUpdate();
    });
}

function addDocument(doc, onAdded){
    myCollection.insert(doc, function(err, result) {
        if(err)
            throw err;

//        console.log("entry saved");
        onAdded(result);
    });
}

function createConnection(ip,port,dbname, collectionname, onCreate){
//"127.0.0.1:27017/'
    var connstr = 'mongodb://'+ip+':'+port+'/'+dbname;
    MongoClient.connect(connstr,{native_parser:true}, function(err, db2) {
        if(err)
            throw err;
        db = db2;
        console.log("connected "+ip+":"+port+"/"+dbname+" - "+collectionname);
        myCollection = db.collection(collectionname);
        myCollection.stats(function(err2,stat){
            if(err2 != null){
                console.log(err2);
            }
            if(stat != null){
                console.log(stat);
                myCollection.count(function(err3,count){
                    if(err3!= null){
                        console.log(err3);
                    }
                    if (count !=null){
                        console.log("Count="+count);
                    }
                    else
                        console.log("Count not found");
                });
            }
            else{
                console.log("NO Stats");
            }
        });
        onCreate();
    });
}

function getCaseIDquerylist(runlist){
    var caseidlist=[];
    var j;
    var t = [{"id" : 12345},{"id" : 22222},{"id" : 12345},{"id" : 33333}];
    for (testcase in runlist) {
        tcase = runlist[testcase];
        caseidlist[testcase] = {"id" : tcase['case_id']};
    }
    return [caseidlist];
}


function getTestcaseStepsFrom(runlist, callback) {
    var counter = -1;
    //var runlistwsteps = [];
    // http://stackoverflow.com/questions/10730561/in-nodejs-how-to-stop-a-for-loop-until-mongodb-call-returns
    // The 'async.forEach()' function will call 'iteratorFcn' for each element in
    // stuObjList, passing a student object as the first param and a callback
    // function as the second param. Run the callback to indicate that you're
    // done working with the current student object. Anything you pass to done()
    // is interpreted as an error. In that scenario, the iterating will stop and
    // the error will be passed to the 'doneIteratingFcn' function defined below.
    var iteratorFcn = function(caseObj, done) {

        // If the current student object doesn't have the 'honor_student' property
        // then move on to the next iteration.
        if( !caseObj['case_id'] ) {
            done();
            return; // The return statement ensures that no further code in this
                    // function is executed after the call to done(). This allows
                    // us to avoid writing an 'else' block.
        }
        caseid = {"id" : caseObj["case_id"]};
        //caseid = {"_id" : "547399437ed0ff23dc587b5d"};

        //console.log(caseid);
        var col = myCollection;//db.collection("suite_8554");
        col.findOne(caseid,function(err, testcase)
        {
            counter++;
            //console.log(counter);
            if(err != null) {
                console.log(err);
                done(err);
                return;
            }

            if (testcase != null){

                //console.log("found custom_steps");
                //console.log(testcase);

                runlist[counter].custom_steps = testcase.custom_steps;
                //cucumber logs this info. The test results reporter will watch for this value for reporting to testrail
                runlist[counter].custom_steps.push("# case_id="+caseObj["case_id"]);
                runlist[counter]['test_results'] = [];
                done();
                return;

            }
            else {
//                console.log("delete");
                delete runlist[counter];
//                console.log("done");
                done();
                return;
            }

        });
    };

    var doneIteratingFcn = function(err) {
        // In your 'callback' implementation, check to see if err is null/undefined
        // to know if something went wrong.
        callback(err, runlist);
    };

    // iteratorFcn will be called for each element in stuObjList.
    async.forEach(runlist, iteratorFcn, doneIteratingFcn);
}

function getTestcaseSteps(sessionResponse, ip, port,dbname, collectionname,testrun) {
    createConnection(ip,port,dbname,collectionname, function() {
		if(testrun == null || testrun == undefined)
		{
			 console.log("TESTRUN LIST is NULL");            
			sessionResponse.write("TESTRUN LIST is NULL");
			sessionResponse.end();
			console.log("DONE******************************************");
			return;
		}
		console.log(testrun);
        var runlist = JSON.parse(testrun);

        getTestcaseStepsFrom(runlist, function (err, runlistwsteps) {
            if (err) {
                // Handle the error
                console.log(err);
                sessionResponse.write(err);
                sessionResponse.end();
                console.log("DONE******************************************");
            }
            else {
                // Do something with runlistwsteps
                strdoc = JSON.stringify(runlistwsteps);
                //jdoc = JSON.parse(strdoc);
                sessionResponse.write(strdoc);
                sessionResponse.end();
                console.log("DONE******************************************");
            }
            return;
        });

    });

}

/*function domongotest(response){
    createConnection("127.0.0.1","27017",'zdb_suite_8554','zsuite_8554', function(){
        var d = {name: "doduck", description: "learn more than everyone"};

        addDocument(d, function(result){
            var d1 = {name: "doduck"};
            var d2 = {name: "doduck", description: "prototype your idea"};
            var d3 = {w:1};
            simpleUpdateDocument(d1,d2,d3,function(){
                d1 = {name: "doduck"};
                d2 = {$set: {industry: "France"}};
                d3 = {w:1};
                fieldUpdateDocument(d1,d2,d3,function(){
                    d1 = {name: "doduck"}
                    d2 = {$set: {company: {employed: 10, officialName: "doduck LTD", industries: ["it consulting", "passionate programming"]}}}
                    d3 = {w:1};
                    fieldComplexeUpdateDocument(d1,d2,d3,null,function(){
                        var j = {"name" : "doduck", "company.officialName" : "doduck LTD" };
                        findOneDocument(j, function(err,doc){
                            strdoc = JSON.stringify(doc);
                            jdoc = JSON.parse(strdoc);
                            response.write(strdoc);

                            d1 = {name: "doduck"};
                            d2 = [];
                            d3 = {remove:true}
                            removeDocument(d1,d2,d3,function(){
                                console.log("The end");
                                //response.write("The end");
                                response.end();
                            });
                        });
                    });
                });
            });
        });
    });

}*/

//exports.domongotest=domongotest;
exports.getTestcaseSteps=getTestcaseSteps;
