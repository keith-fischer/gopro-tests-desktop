var DEBUG=true;
var express = require('express');
var utils = require("./../libs/utils").utils;
var wss = require("./../libs/websocketserver").WebSocketServer;
var wsm = require("./../libs/wsmessagehandlers").wsmessagehandlers;
wsm.testmgr = require("./../libs/testmgr").testmgr;
var router = express.Router();
var counter =0 ;

//if(DEBUG)wsm.testmgr.loadsampletests();
if(DEBUG)wsm.testmgr.loadtestfromjson("./../Tests/bat_tests.json");

var testjs = function(id, test, js, result) {
    this.id = id;
    this.test = test;
    this.js = js;
    this.result = result;
};

var spawn = require('child_process').spawn;
var prc;
var _results=[];
var _gda=false;
wss.start_ws(1234,wsm);

//if(DEBUG)utils.runGDA();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
/* GET users listing. */
router.get('/keith', function(req, res, next) {
    res.render('keith', { title: 'fischer' });
});
/* GET users listing. */
router.get('/gdajstest', function(req, res, next) {
    console.log('router.get:'+req.body);

    if(_results.length==0)_results.push(new testjs(counter.toString(),'test name','your javascript script','RESULT: GDA eval(your javascript script)'));
    console.log(_results);
    res.render('gdajstest', { title: 'GDA Javascript DOM Tester',testresults: _results ,GDA_status: 'Not Running'});
});

/* GET users listing. */
router.post('/gdajstest', function(req, res, next) {
    console.log('router.post:');
    console.log(req.body.test);
    wsm.wapi=res;

    if(req.body.whichpost=='Test Javascript in GDA') {
        if (req.body.test.length > 0 && req.body.javascript.length > 0) {
            wsm.js_script=req.body.javascript;
            wsm.wapi=res;
            wsm.js_script=req.body.javascript;
            wsm.testmgr.settest(wsm.js_script);
            wsm.Test_Name=req.body.test;
            counter++;
            wsm.Test_Count=counter;
            //the script is in-queue
            //gda will make a request for a test script via websocket
            //we wait for the result from websocket
            // postback the result to browser


            //_results.push(new testjs(counter.toString(), req.body.test, req.body.javascript, 'RESULT' + counter.toString()));
            //console.log(_results);
            //res.render('gdajstest', { title: 'GDA Javascript DOM Tester', testresults: _results});
        }
    }
    else if(req.body.whichpost=='Reset Results List') {
        counter =0 ;
        _results=[];
        _results.push(new testjs(counter.toString(),'test name','your javascript script','RESULT: GDA eval(your javascript script)'));
        console.log(_results);
        res.render('gdajstest', { title: 'GDA Javascript DOM Tester', testresults: _results, GDA_status: 'running'});

    }
    else if(req.body.whichpost=='Start GDA') {
        console.log('Start GDA');
        var spawn = require('child_process').spawn;
        prc = spawn('/Applications/GoPro.app/Contents/MacOS/GoPro',  ['GoProPlayerPlugin', '-testscript', '/Automation/gopro-tests-desktop/GDA/GDA_Test_Lib/servermsgloop.js', '-testinterval', '2000']);
        //noinspection JSUnresolvedFunction
        prc.stdout.setEncoding('utf8');
        var is_done = false;
        is_done=prc.stdout.on('data', function (data) {
            var str = data.toString()
            var lines = str.split(/(\r?\n)/g);
            console.log(lines.join(""));
            return true;
        });

        prc.on('close', function (code) {
            console.log('process exit code ' + code);
        });
        for (var i = 0; i < 30; i++) {
            console.log('wait Start GDA===================================================');
            if(is_done){
                res.render('gdajstest', { title: 'GDA Javascript DOM Tester',testresults: _results , GDA_status: 'running'});
                console.log('running Start GDA==================================================');
                break;
            }
            else{
                setTimeout(function() {
                    console.log('wait Start GDA==============================================');
                }, 1000);
            }
        }
        // /Applications/GoPro.app/Contents/MacOS/GoPro GoProPlayerPlugin -testscript "/Automation/gopro-tests-desktop/GDA/GDA_Test_Lib/servermsgloop.js" -testinterval 2000

    }
    //_results = counter.toString()+'. '+req.body.test+'\n'+req.body.javascript+'\n'+'RESULT'+'----------\n'+_results;
    //console.log(_results);
    //res.render('gdajstest', { title: 'GDA Javascript DOM Tester', testresults: _results});
    //res.send('gdajstest', { title: 'GDA Javascript DOM Tester',results: _results});
});

module.exports = router;
