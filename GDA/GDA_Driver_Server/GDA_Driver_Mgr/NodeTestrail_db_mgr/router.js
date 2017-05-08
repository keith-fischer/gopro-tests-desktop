

function route(handle, pathname, response, request, urlData, postData, session) {
	console.log(session + " - Request: " + pathname + " - postData: " + urlData);
	//response.write("About to route a request for " + pathname);
	if (typeof handle[pathname] === 'function') {
		try {
			console.log(session + " - Starting " + pathname + " - " + urlData);
			response = handle[pathname](response, request, urlData, postData, session);
		} catch (e) {
			console.log(session + " ERROR: " + pathname + " - " + urlData+"\n"+e);
			response.writeHead(401, {
				"Content-Type" : "text/html"
			});
			var err="";
			if ("message" in e){
				err = e.message;
			}
			console.log(pathname +"\n"+ err);
			response.write("ERROR: 401 " + pathname +"<p>"+ err+"</p>");
			response.end();
		}
		
	} else {
		console.log(session + " No request handler found for " + pathname + " - " + urlData);
		response.writeHead(404, {
			"Content-Type" : "text/html"
		});
		response.write("404 Not found");
		response.end();
		
	}
	return response;
}

exports.route = route;
