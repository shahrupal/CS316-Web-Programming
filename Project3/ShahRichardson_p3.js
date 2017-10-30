//Authors: Jacob Richardson & Rupal Shah

var http = require('http'); //include http module/library
var url = require('url');   //include http module/library

const hostname = 'feverfew.cs.uky.edu'; //set hostname

var STARTPORT = 2000; //minimum port
var ENDPORT = 30000;  //maximum port

//create a random port between STARTPORT and ENDPORT
//const port = Math.floor(Math.random() * (ENDPORT - STARTPORT + 1) + STARTPORT); 
const port = 1092;

//regular expression for url
var regex = /[a-zA-Z0-9_]*[.][mp3|jpg]/;

//loads filesystem
var fs = require('fs');
var file = "advert.jpg";
var firstLoop = true;

//req = request, rep = response
http.createServer(function serveURL(req, rep){

	if(firstLoop == true){
		console.log("---------------------\nServer started. Listing on " + hostname + "\n--------------------\n");
		firstLoop = false;
	}
	
	//gets the url and outputs it to the console
	var inputURL = req.url;
	console.log("URL Requested: " + inputURL + "\n");

	inputURL = inputURL.substring(1, inputURL.length); //strips '/' character from the front

	if(inputURL.match(regex) == null){ //if URL does not match regular expression
		//output an error message
		rep.write('403 ERROR:\nInput not in correct format.\nMust only include letters, numbers, and underscores. Must also include .jpg or .mp3 extension.');
		rep.end();		
	}
	else{//the url is valid
		fs.exists(inputURL, function(exists){	

			if(exists){  //if the input file exists
				var checkExtension = inputURL.substring(inputURL.length - 3, inputURL.length); //stores extension
				var random = Math.floor(Math.random() * 3); //random integer between 0&2
				
				if(random === 2){  //outputs ad 33% of the time
					giveAdvert(rep);
				}
				else if(checkExtension === "jpg"){ //if its a JPEG
					giveJPG(inputURL.toString(), rep);
				}
				else if(checkExtension === "mp3"){ //if its a MP3
					giveMP3(inputURL.toString(), rep);
				}
			
				fs.readFile(file, function(err, data){ //reads the file
					if(err){
						throw(err);
					}
					rep.end(data); //sends the file
				});
				
			}
			else{ //if the input file does not exist

				//output an error message
				rep.write('403 ERROR:\nFile not found.');
				rep.end();

			}
		});
	}

}).listen(port, hostname);

//makes the file to be returned the advertisment, and sets header appropriately 
function giveAdvert(rep){
	file = "advert.jpg";
	rep.setHeader('Content-Type', 'image/jpeg');
}

//makes the file to be returned the JPG requested, and sets header appropriately 
function giveJPG(jpgFile, rep){
	file = jpgFile;
	rep.setHeader('Content-Type', 'image/jpeg');
}

//makes the file to be returned the MP3 requested, and sets header appropriately 
function giveMP3(mp3File, rep) {
	file = mp3File;
	rep.setHeader('Content-Type', 'audio/mpeg');
}

