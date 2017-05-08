/**
 * Created by keithfisher on 12/23/15.
 * https://github.com/sitegui/nodejs-websocket
 */
var ws = require("nodejs-websocket");

// Scream server example: "hi" -> "HI!!!"
var server = ws.createServer(function (conn) {
    console.log("New connection");

    conn.on("text", function (str) {
        console.log("Received:"+str);
        var m1 = str.toUpperCase()+'!!!';
        var m2 = "qgoproapp.showTestMessage('"+m1+"');";
        var msg = "try{"+m2+"}catch(err){connection.send('EVAL ERROR'+err.message);}";


        console.log(msg);
        conn.sendText(msg);
    })
    conn.on("close", function (code, reason) {
        console.log("Connection closed")
    })
}).listen(1234)

