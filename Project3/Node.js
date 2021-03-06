
//Authors: Jacob Richardson & Rupal Shah

var http = require('http'); //include http module/library
var url = require('url');   //include http module/library

const hostname = 'feverfew.cs.uky.edu'; //set hostname

var STARTPORT = 2000; //minimum port
var ENDPORT = 30000;  //maximum port

//create a random port between 2000 and 30000
const port = Math.floor(Math.random() * (ENDPORT - STARTPORT + 1) + STARTPORT); 

//regular expression for url
var regex = /[a-zA-Z0-9_]*[.][mp3|jpg]/;

//loads filesystem
var fs = require('fs');
var temp;
var file = "advert.jpg";

//req = request
//rep = response
http.createServer(function serveURL(req, rep){

	var inputURL = req.url;
	console.log("URL Requested: " + inputURL);

	inputURL = inputURL.substring(1, inputURL.length); //strips '/' character

	console.log("URL without /: " + inputURL);

	if(inputURL.match(regex) == null){ //if URL does not match regular expression

		rep.write('403 ERROR:\nInput not in correct format.\nMust only include letters, numbers, and underscores. Must also include .jpg or .mp3 extension.');
		rep.end();
		
	}
	else{

		fs.exists(inputURL, function(exists){	

			var random = Math.floor(Math.random() * 3);
			var checkExtension = inputURL.substring(inputURL.length - 3, inputURL.length); //stores extension

			if(exists){  //if the input file exists

				if(random === 2){  //outputs ad 33% of the time
					giveAdvert(rep);
				}
				else if(checkExtension === "jpg"){ 
					giveJPG(inputURL.toString(), rep);
					console.log("JPG: " + inputURL);
				}
				else if(checkExtension === "mp3"){
					giveMP3(inputURL.toString(), rep);
					console.log("MP3: " + inputURL);
				}
			
				fs.readFile(file, function(err, data){
					if(err){
						throw(err);
					}
					console.log(file);
					rep.end(data);
				});
				
			}
			else{ //if the input file does not exist

				rep.write('403 ERROR:\nFile not found.');
				rep.end();

			}
		});
	}

}).listen(port, hostname);


function giveAdvert(rep){
	file = "advert.jpg";
	rep.setHeader('Content-Type', 'image/jpeg');
}


function giveJPG(jpgFile, rep){
	file = jpgFile;
	rep.setHeader('Content-Type', 'image/jpeg');
}


function giveMP3(mp3File, rep) {
	file = mp3File;
	rep.setHeader('Content-Type', 'audio/mpeg');
}

