var connection = new WebSocket('ws://localhost:1234');
connection.onopen = function () {connection.send('GDA_START:');}
connection.onerror = function (error) {printmsg('ERROR:WebSocket Error ' + error);};
connection.onmessage = function (e) {cmdlist.push(e.data)};
connection.onclose = function(){printmsg("***GDA App WebSocket is closed***")}
