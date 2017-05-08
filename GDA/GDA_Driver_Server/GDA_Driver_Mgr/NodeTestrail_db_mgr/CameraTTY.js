/**
 * Created by keithfisher on 12/16/14.
 */



var CamTTY = [];

var t_cmds =[];

var TTYBuffer = {
    maxbuffer:999999,
    buffdata:""

};

function init(){
    this.t_cmds["wireless_off"]="t api wireless mode off";
    this.t_cmds["wireless_on"]="t api wireless mode app";

}

function isConnected(){
    rc =false;

    return rc;
}

function RebootCamera(){
    rc =false;

    return rc;
}


function WifiOff(){
    rc =false;
//[02027946][CA9_0] wiman_csi_wireless_mode_cb: wireless enable - 0, mode - 1
    return rc;
}


function WifiOn(){
    rc =false;
//[02103176][CA9_0] wiman_csi_wireless_mode_cb: wireless enable - 1, mode - 1
    return rc;
}


function SetLogBuffer(_size){
    rc =false;

    return rc;
}

function GetLogBuffer(){
    rc =false;

    return rc;
}

exports.TTYBuffer=TTYBuffer;
