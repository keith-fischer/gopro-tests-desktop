var timeout = 30;
var timecount = timeout;
var root='/Automation/gopro-tests-desktop/GDA/GDA_Test_Lib/';
var eval_js = "";
var loopcount =0;
var nolog=false;
var fullWidth = window.innerWidth;
var fullHeight = window.innerHeight;
var msgelem = document.createElement("div");
var cmdlist=[];
msgelem.textContent = 'Automation>';
msgelem.id="automsg";
msgelem.style.position = "absolute";
msgelem.style.left = Math.round(.4 * fullWidth) + "px";
msgelem.style.top = Math.round((0) * fullHeight) + "px";
document.body.appendChild(msgelem);
function showvarinfo(obj){var z=typeof obj;if(z=='string')z=z+':'+obj;if(z=='number')z=z+':'+obj.toString();if(z=='boolean')z=z+':'+obj.toString();if(z=='object')z=z+':'+obj.toString();qgoproapp.showTestMessage(z);}
function printmsg(txt){this.msgelem=document.getElementById("automsg");this.msgelem.textContent = 'Automation>'+txt;}
function log(msg){if(nolog)return;var m="LOG:"+msg;connection.send(m);printmsg(m);}
qgoproapp.executeTestProgram(root+"server.js");
log("start server_loop");

try {
SERVER_LOOP:
    test_cmd = "";
    loopcount++;
    timecount--;
    log("server_loop>" + loopcount.toString()+"===========================");
    log("cmdlist>" + cmdlist.length.toString()+"-"+timecount.toString());

    log("executeTestProgram>");
    qgoproapp.executeTestProgram(root + "serverhandler.js");
    log("executeTestProgram<");
    log("timecount>" + timecount.toString());
    if(timecount > 0){qgoproapp.gotoTestLabel("SERVER_LOOP");}
    connection.send('GDA_STOP:');
    qgoproapp.quitApp();
}
catch(err){
    connection.send("ERROR:SERVER_LOOP\n"+err.message);
    if (timecount > 0)qgoproapp.gotoTestLabel("SERVER_LOOP");
}

