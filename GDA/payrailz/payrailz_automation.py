from flask import Flask, json, request
import json

# --------------------------------------------------------------------------
# Very simple REST server using Flask
# --------------------------------------------------------------------------
JSON_FIELD = "payrailz_automation"
PORT = 8082
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


# --------------------------------------------------------------------------
# Function router defined by the api string
# --------------------------------------------------------------------------
@app.route('/payrailzauto', methods=['POST', 'GET'])
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
            if "api" in _data and "payrailzauto" in _data:
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
# P A Y R A I L Z  H E L P E R  F U N C T I O N S
# --------------------------------------------------------------------------

def clear_bank_customer_payments(bank_name):

