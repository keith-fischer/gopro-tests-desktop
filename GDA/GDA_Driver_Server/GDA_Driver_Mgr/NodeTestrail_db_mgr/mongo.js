/**
 *
 * Created by Keith Fisher on 2/7/14.
 * Framework Test Run
 * recieve the testrun list json file
 * iterate the testrun list which each contains the testname and case_id
 * with the case_id query db for the same testcase containing the teststeps
 * Add db testcase steps to the current testrun testcase object
 * Tests not found in db indicate out-of synch state and the
 * python testcase generator tool needs to be run to re-synch the db with testrail.
 * The testcase list is returned to the http client to run the tests
 *db=db_suite_8554
 * db = bawa4885
 *collection=suite_8554
 */
//var mongo_client = require('./mongodataadapter');
//mg = new mongo_db();
//mg.Mongo_Client=MongoClient;
//mg.connect('mongodb://localhost:27017/testReports');

// Retrieve
var MongoClient = require('mongodb').MongoClient;
var debug = true;
var collection;
var db;
//var mongoUT = require("./mongoUtils");


function OnCreate(){
    console.log("Connected: ");
}
function FindIt(){

}

function doTeststeps(err,sessionResponse, db,collection,  testrun, runid){
    if (err) { return console.log(err); }
    collection = db.collection('suite_8554');
    if(collection != undefined) {
        console.log("Connected: " + ipconnect + ":" + collectionname);
        var runlist = JSON.parse(testrun);
        var item;
        for (testcase in runlist) {
            test = runlist[testcase];

            collection.findOne({id: test.case_id}, function (err, item) {
                if (item.id == test.case_id) {
                    test.custom_steps = item.custom_steps;
                    runlist[testcase] = test;
                    if (debug) {
                        console.log("Updated: " + test.case_id);
                    }
                }

            })
        }
        db.close();
        sessionResponse.write(runlist); // JSON.stringify(data));
        console.log("TestRail.onResponse_get_test:"+JSON.stringify(runlist));
        console.log("TestRail.onResponse_get_test:"+res);
        sessionResponse.end();
        console.log("runlist="+runlist.length);
        return runlist;
    }
    else{
        console.log("collection=undefined");
    }
}



function getTestcaseSteps2(callback, sessionResponse, url, testrun, runid){
    url = 'localhost:27017';
    ipconnect = 'mongodb://'+url+'/db_BAWAP1Android';  //db_suite_8554   bawa4885
    collectionname= 'col_BAWAP1Android';//suite_8554   bawa8558
    if (db === undefined) {
        MongoClient.connect(ipconnect, function (err, db) {
            if (err) {
                if(err) { return callback(err)};
            }
            //Z:\Projects\MongoDB\data\db\testReports

            return callback(null,sessionResponse,db, collection, testrun, runid);
        });

    }
    else{
        if(collection === undefined){
            db.collection(collectionname);
        }
        if(collection != undefined) {
            callback(null,sessionResponse,db, collection, testrun, runid);
        }
        else{
            callback("Failed: setting the colection:"+collectionname,
                sessionResponse,db, collection, testrun, runid);
        }
    }

}
/*

MongoClient:MongoClient.connect('mongodb://localhost:27017/testReports', testsuitename, testrunlist, function(err, db) {
    if(err) { return console.dir(err); }
    //Z:\Projects\MongoDB\data\db\testReports
    var collection = db.collection('test');
    var doc1 = {'hello':'doc1'};
    var doc2 = {'hello':'doc2'};
    var lotsOfDocs = [{'hello':'doc3'}, {'hello':'doc4'}];

    collection.insert(doc1);

    collection.insert(doc2, {w:1}, function(err, result) {});

    collection.insert(lotsOfDocs, {w:1}, function(err, result) {});



})
*/

/*
 mongo_db = {
 Mongo_Client: [],
 connect:function(mongodb, function(err, db) {
 this.Mongo_Client(mongodb, )
 })
 // Connect to the db



 }

 mg = new mongo_db();
 mg.Mongo_Client=MongoClient;
 mg.connect('mongodb://localhost:27017/testReports');*/

//exports.getTestcaseSteps=getTestcaseSteps;
exports.doTeststeps=doTeststeps;
