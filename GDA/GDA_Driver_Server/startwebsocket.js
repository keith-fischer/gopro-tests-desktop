/**
 * Created by keithfisher on 12/29/15.
 */


var wss = require("./WebSocketServer");
var wsm = require("./wsmessagehandlers");

wss.WebSocketServer.start_ws(1234,wsm.wsmessagehandlers);

