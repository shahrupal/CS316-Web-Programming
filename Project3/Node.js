
//Authors: Jacob Richardson & Rupal Shah

var http = require('http'); //include http module/library
var url = require('url');   //include http module/library

const hostname = 'feverfew.cs.uky.edu'; //set hostname

var STARTPORT = 2000; //minimum port
var ENDPORT = 30000;  //maximum port

//create a random port between 2000 and 30000
//const port = Math.floor(Math.random(STARTPORT) * (ENDPORT + 1)); 
const port = 1996;

//regular expression for url
var regex = /[a-zA-Z0-9_]*[.][mp3|jpg]/;

//loads filesystem
var fs = require('fs');
var temp;
var file = "default.jpg";

//opens specified file, throws error if file is nonexistent
fs.readFile(file, function(err, data){
	if(err) throw err;
	temp = data;
});

//req = request
//rep = response
http.createServer(function serveURL(req, rep){

//	file = "advert.jpg";
//	rep.end(temp);	

//	fs.readFile(file, function(err, data){
//		if(err) throw err;
//		temp = data;
//	});	

	var inputURL = req.url;
	console.log("URL Requested: " + inputURL);

	inputURL = inputURL.substring(1, inputURL.length); //strips '/' character

	console.log("URL without /: " + inputURL);

	if(inputURL.match(regex) == null){
		console.log("false");
	}
	else{
	
		var random = Math.floor(Math.random() * 3);
		var checkExtension = inputURL.substring(inputURL.length - 3, inputURL.length); //stores extension
		
		if(random === 2){
			giveAdvert();
			rep.end(temp);
		}
		else if(checkExtension === "jpg"){
			giveJPG("testjpg.jpg");
			console.log("pls work i swear to god");
			rep.end(temp);
		}
		else if(checkExtension === "mp3"){
			giveMP3(inputURL.toString());
			rep.end(temp);
		}
		
		fs.readFile(file, function(err, data){
			if(err) throw err;
			temp = data;
		});
	}
	

//	rep.write('boop');
//	rep.end(temp);	    DOWNLOADS EVERY URL
//	rep.end();

}).listen(port, hostname);


function giveAdvert(){
	file = "advert.jpg";
}


function giveJPG(jpgFile){
	file = jpgFile;
}


function giveMP3(mp3File) {
	file = mp3File;
}

