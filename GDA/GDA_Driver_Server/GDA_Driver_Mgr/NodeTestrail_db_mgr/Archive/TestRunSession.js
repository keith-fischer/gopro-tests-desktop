/**
 * Created by keithfisher on 10/3/14.
 */
var utils = require('./../Utils');
var TestSessions = [];

/*
* TestSession object stored in TestSessions
*
* */
var TestSession = { //TestSessions["YYMMDDhhmmss"]
    SessionToken: "", //YYMMDDhhmmss
    TestRailRunID: 0, //>10563<,  https://gopro.testrail.com/index.php?/runs/view/10563
    TestRail: [],//entire test run object
    TestStartDateTime: null,
    TestIndex: -1,
    TestLastDateTime: null,
    TestTimeoutMinutes: 10
}

/*
* Populates a new TestSession
* */
function getNewSession(runID,runSuites){
    var ts = new TestSession();
    ts.TestRailRunID=runID;
    ts.SessionToken=utils.UtilFN.GetDateTimeNow();
    ts.TestStartDateTime = new Date();
    ts.TestLastDateTime= new Date();
    ts.TestRail=JSON.parse(runSuites);
    return ts;
}


/*
 * Populates a new TestSession
 * and queries the Testrail for the entire test suite
 * */
function AddSession(runID,runSuites){
    var rc=false;
    var _TestSession = getNewSession(runID,runSuites);

    if(TestSessions.length>0){
        var found=false;
        for(var i=0;i<TestSessions.length;i++){
            if(TestSessions.SessionToken===_TestSession.SessionToken){
                found=true;
                break;
            }

        }
        if(!found){
            _TestSession.TestRail=null;//query testrail
            rc=true;
        }else{

        }
    }
    else{
        this.TestSessions[_TestSession.SessionToken]=_TestSession;
        rc=true;
    }

    return rc;//true new session created
}
function DeleteSession(sessionToken){
    var id=getSessionID(sessionToken);

    if(id>=0) {
        TestSessions[id] = null;
        return true;
    }
    else
        return false;
}
function getSessionID(sessionToken){
    var foundsession=-1;
    if(TestSessions==undefined || TestSessions ==null || TestSessions.length==0)
        return foundsession;
    for(var i=0;i<TestSessions.length;i++){
        if(TestSessions[i].SessionToken ==sessionToken){
            foundsession= i;
            break;
        }
    }
    return foundsession;
}

function getSession(sessionToken){
    var foundsession=null;

    var id=getSessionID(sessionToken);
    if(id>=0)
        return TestSessions[id];
    return foundsession;
}
exports.AddSession = AddSession;
exports.getSession = getSession;
exports.DeleteSession = DeleteSession;
exports.TestSession=TestSession;