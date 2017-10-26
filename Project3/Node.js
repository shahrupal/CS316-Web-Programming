
var http = require('http'); //include http module/library
var url = require('url');   //include http module/library

const hostname = 'feverfew.cs.uky.edu'; //set hostname

var STARTPORT = 2000; //minimum port
var ENDPORT = 30000;  //maximum port

//create a random port between 2000 and 30000
//const port = Math.floor(Math.random(STARTPORT) * (ENDPORT + 1)); 
const port = 8080;

//regular expression for url
var regex = /^[\/][a-zA-Z0-9_]*[.][mp3|jpg]$/;

//req = request
//rep = response
http.createServer(function serveURL(req, rep){

	var inputURL = req.url;
	console.log("URL Requested: " + inputURL);

	if(inputURL.match(regex) == null){
		console.log("false");
	}
	else{
		console.log("true");
	}
	

	rep.write('boop');
	rep.end();

}).listen(port, hostname);
