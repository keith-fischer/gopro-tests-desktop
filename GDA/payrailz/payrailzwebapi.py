from flask import Flask, json, request
import json

# --------------------------------------------------------------------------
# Very simple REST server using Flask
# --------------------------------------------------------------------------
JSON_FIELD = "payrailz"
PORT = 8081
callback = None
app = Flask(__name__)
#tr = None

# --------------------------------------------------------------------------
# USAGE:
# simplerestserver.callback=MyClass.my_callback # static method
# simplerestserver.JSON_FIELD="banner" #this JSON field will get sent to the my_callback
# simplerestserver.start() #main thread get consumed here and return back on the callback
# --------------------------------------------------------------------------
# POST /banner HTTP/1.1
# Host: 127.0.0.1:8081
# Content-Type: application/json
# Cache-Control: no-cache
# {"banner":"camera tests\n Line2\n Line3 camera tests\n Line4\n Line5"}
# --------------------------------------------------------------------------


@app.route('/payrailz', methods=['POST', 'GET'])
def main():
    global callback
    global tr
    resp={}
    #_obj={}
    try:
        #print str(request.form)
        _data=request.data #data from python client using flask
        if not _data:
            _data = request.form # data from sikuli
        else:
            _data=json.loads(_data)
        # validate the received values
        if _data:
            if "api" in _data and "payrailz" in _data:
                _obj=_data
            else:
                info = 'No %s field' % JSON_FIELD
                return json.dumps({'post_data_error': info})
            #_obj = json.loads(_data.decode("utf-8"))
            if _obj and JSON_FIELD in _obj: #JSON_FIELD
                if not callback:
                    callback=_callback
                if not tr:
                    resp = payrailz_init({})
                    if tr and "error" not in resp:
                        resp=callback(_obj)
                    else:
                        tr=None
                else:
                    resp = callback(_obj)
                return json.dumps(resp)

            else:
                info = 'No %s field' % JSON_FIELD
                return json.dumps({'error': info})
        else:
            return json.dumps({"error": "No Data"})

    except Exception as e:
        return json.dumps({"error": str(e)})

# --------------------------------------------------------------------------
# Function router defined by the api string
# --------------------------------------------------------------------------
def _callback(data):
    resp = {}
    if not data:
        return None
    print str(data)
    if "api" not in data:
        resp['error'] = "missing api field"
        return resp
    api = str(data["api"])
    print str(globals)
    if api in globals(): # api string must match function name
        resp = globals()[api](data)
        resp['payrailz'] = api
    return resp

# --------------------------------------------------------------------------
# T E S T R A I L  H E L P E R  F U N C T I O N S
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Get list of runs in the project repo 86
# --------------------------------------------------------------------------
def get_runs(data):
    resp = {}
    resp['payrailz'] = data["api"]
    print "get_runs %s" % str(data)
    if "projid" in data:
        resp["response"] = tr.get_runs(int(data["projid"]))
    else:
        resp["error_data"] = "Invalid data field names: %s" % str(data)
    return resp

# --------------------------------------------------------------------------
# Get list of suites in the project repo 86
# --------------------------------------------------------------------------
def get_suites(data):
    resp={}
    resp['payrailz'] = data["api"]
    print "get_suites %s" % str(data)
    if "projid" in data:
        resp["response"]=tr.get_suites(int(data["projid"]))
    else:
        resp["error_data"] = "Invalid data field names: %s" % str(data)
    return resp

# --------------------------------------------------------------------------
# Delete run in the project repo 86
# --------------------------------------------------------------------------
def delete_run(data):
    resp = {}
    resp['payrailz'] = data["api"]
    print "delete_run %s" % str(data)
    if "suitid" in data and "runid" in data:
        resp["response"] = tr.delete_run(int(data["suitid"]),int(data["runid"]))
    else:
        resp["error_data"] = "Invalid data field names: %s" % str(data)
    return resp


# --------------------------------------------------------------------------
# Set testrun testcase status id in the project repo 86
# --------------------------------------------------------------------------
def add_result(data):
    resp = {}
    resp['payrailz'] = data["api"]
    print "add_result %s" % str(data)
    if "projid" in data and "status_id" in data and "testid" in data:
        projid = int(data["projid"])
        statusid = int(data["status_id"])
        testid = int(data["testid"])
        runid=int(data["runid"])
        comment=""
        if "comment" in data:
            comment=data["comment"]
        elapsed="5s"
        if "elapsed" in data:
            elapsed = data["elapsed"]
        version = ""
        if "version" in data:
            version= data["version"]
        resp["response"]=tr.add_result(projid,testid,runid,statusid,comment,elapsed,version)
    return resp

# --------------------------------------------------------------------------
# Get the list of tests in the testrun of the project repo 86
# --------------------------------------------------------------------------
def get_tests(data):
    resp = {}
    resp['payrailz'] = data["api"]
    print "get_tests %s" % str(data)
    if "projid" in data and "testrunid" in data:
        resp["response"] = tr.get_tests(int(data["projid"]),int(data["testrunid"]))
    else:
        resp["error_data"] = "Invalid data field names: %s" % str(data)
    return resp

# --------------------------------------------------------------------------
# Get testcase latest details of a testrun in the project repo 86
# --------------------------------------------------------------------------
def get_test(data):
    resp = {}
    resp['payrailz'] = data["api"]
    print "get_test %s" % str(data)
    if "projid" in data and "testid" in data:
        resp["response"] = tr.get_test(int(data["projid"]),int(data["testid"]))
    else:
        resp["error_data"] = "Invalid data field names: %s" % str(data)
    return resp

# --------------------------------------------------------------------------
# Get testcase results all historical details of the testrun in the project repo 86
# --------------------------------------------------------------------------
def get_results(data):
    resp = {}
    resp['payrailz'] = data["api"]
    print "get_results %s" % str(data)
    if "projid" in data and "testid" in data:
        resp["response"] = tr.get_test(int(data["projid"]),int(data["testid"]))
    else:
        resp["error_data"] = "Invalid data field names: %s" % str(data)
    return resp

# --------------------------------------------------------------------------
# Create a new testrun derived from specfied test suite in the project repo 86
# --------------------------------------------------------------------------
def add_run(data):#add_run(projid,suitid,sectionid,runname="Automation Quik TestRun", rundescription="",milestoneid=None,assignedto=None)
    resp = {}
    resp['payrailz'] = data["api"]
    print "add_run %s" % str(data)
    if "projid" in data and "suite_id" in data and "run_name" in data and "description" in data:
        resp["response"] = tr.add_run(int(data["projid"]),int(data["suite_id"]), data["run_name"], data["description"])
    else:
        resp["error_data"] = "Invalid data field names: %s" % str(data)
    return resp

# --------------------------------------------------------------------------
# Init the payrailz class which forwards requests to payrailz.gopro.com web rest api service
# --------------------------------------------------------------------------
def payrailz_init(data):
    global tr
    pw="Bro$toke1!"
    login="sqaautomation1@gopro.com"
    projid = 86
    url = "https://payrailz.gopro.com"
    if "projid" in data:
        projid=int(data['projid'])
    if "login" in data:
        login=data['login']
    if "pw" in data:
        pw=data['pw']
    if "url" in data:
        url = data['url']
    tr=test_payrailz.payrailz_API(url,projid,login,pw)
    if tr.ok:
        return tr.lastresponse
    tr.lastresponse["error"]="Failed to init test_payrailz.payrailz_API %d %s %s %s" % (projid, login, pw, url)
    return tr.lastresponse


# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
def start():
    app.run(port=PORT)

if __name__ == "__main__":
    start()