/**
 * Created by keithfisher on 12/28/15.
 */


var WebSocketServer = {
    /**
     * Created by keithfisher on 12/23/15.
     * https://github.com/sitegui/nodejs-websocket
     */
    ws :require("nodejs-websocket"),

    //on_text : function (conn, str){
    //    console.log("Received:"+str);
    //    var m1 = str.toUpperCase()+'!!!';
    //    var m2 = "qgoproapp.showTestMessage('"+m1+"');";
    //    var msg = "try{"+m2+"}catch(err){connection.send('EVAL ERROR'+err.message);}";
    //    console.log(msg);
    //    conn.sendText(msg);
    //},
    //on_close : function(conn, code, reason){
    //    console.log("Connection closed");
    //},

    start_ws : function(port ,wsm){
        console.log("Start New connection");
        //var _this=this;
        this.server = this.ws.createServer(function (conn) {

            console.log("connection created");

            conn.on("text", function (str) {
                wsm.on_text(conn,str);
            })
            conn.on("close", function (code, reason) {
                wsm.on_close(conn,code,reason);
            })
        }).listen(port);
    }

}

exports.WebSocketServer = WebSocketServer;
