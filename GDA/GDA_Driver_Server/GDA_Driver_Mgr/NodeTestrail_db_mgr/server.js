
var http = require("http");
var url = require("url");
var sessionid = 0;
var concurrent = 0;
// Startup database connection
//require('./DataAccessAdapter').InitDB();

function start(route, handle) {
	function onRequest(request, response) {
		
		var thissession = ++sessionid;
		
		var pathname1 = url.parse(request.url).pathname;
		console.log(pathname1);
		var postData="";
		//var ss = new Array();

		var ss = pathname1.split("/");
		var urlData = "";
		var pathname = ss[1];


		if (ss.length > 1) {
			//postData = ss[2]; //assumes alternate delimiter of not "/"
			ss.splice(1, 1);//more [/segment/segment/]
			urlData = ss.join("/");
		}
		else if (ss.length > 0)
			urlData = ss[1];

		console.log(++concurrent + " - Request for " + pathname + " postData - " + urlData);


		request.setEncoding("utf8");
		
		request.addListener("data", function (postDataChunk) {
			postData += postDataChunk;
			//console.log("Received POST data chunk len='" + postDataChunk.length + "'.");
		});
		
		request.addListener("end", function () {
			//route(handle, pathname, response, request, urlData, JSON.parse(JSON.stringify(postData)), thissession);
			try{
				var js;
				if(postData.length>0)
					js = JSON.parse(postData);
				route(handle, pathname, response, request, urlData, js, thissession);
				console.log(--concurrent + " - Request for " + pathname + " END.");

				//else{
				//	console.log(--concurrent + " - FAILED REQUEST for " + pathname + " No POST data END.");

			}
			catch(err){
				console.log(--concurrent + " - FAILED REQUEST for " + pathname + "\n"+err+"\n END.");
			}

			
		});
		
	}
	
	http.createServer(onRequest).listen(8888);
	console.log("Server has started.");
}

exports.start = start;
