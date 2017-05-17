var https = require('https');
var fs = require('fs');

var options = {
	hostname:'127.0.0.1',
	port:5000,
	path:'/',
	method:'GET',
	key:fs.readFileSync('./client.key'),
	cert:fs.readFileSync('./client.cert'),
	ca: [fs.readFileSync('./ca.cert')],
	agent:false
};

options.agent = new https.Agent(options);
var req = https.request(options,function(res){
console.log("statusCode: ", res.statusCode);
  console.log("headers: ", res.headers);
	res.setEncoding('utf-8');
	res.on('data',function(d){
		console.log(d);
	})
});

req.end();

req.on('error',function(e){
	console.log(e);
})

