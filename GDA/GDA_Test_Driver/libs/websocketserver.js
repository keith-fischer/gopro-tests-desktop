/**
 * Created by keithfisher on 12/28/15.
 */


var WebSocketServer = {
    /**
     * Created by keithfisher on 12/23/15.
     * https://github.com/sitegui/nodejs-websocket
     */
    ws :require("nodejs-websocket"),
    server: Object,  //[]
    ws_msg_Handler: require("./../libs/wsmessagehandlers"),


    start_ws : function(port ,wsm){
        console.log("Start New connection");
        this.ws_msg_Handler=wsm;
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
