var io = require('socket.io-client');
var socket = io.connect('http://1fe116ff.ngrok.io')
// var http = require('http')
var PythonShell = require('python-shell');


socket.on('connect', function (socket) {
	console.log('connected')
})

socket.emit('connected')


PythonShell.run('clientest.py', function (err) {
	if (err) throw err;
	console.log('done');
});



// // function to run a python script from the js file
// function runPy() {

// 	console.log('runpy')

// 	var options = {
// 		host: '/',
// 		path: 'clientest.py'
// 	};

// 	callback = function(response) {
// 		console.log('hehehe')
// 	}

// 	http.request(options, callback).end()

// 	// var request = $.ajax({
// 	// 	type: "POST",
// 	// 	url: "/clientest.py",
// 	// 	async: false,
// 	// 	data: { param: 'hello'}
// 	// });

// 	// return request.responseText;
// }

// runPy();





// var spawn = require('child_process').spawn
// var trusttheprocess = spawn('python', ['/Users/nikhil/development/OpenCV-Face/Website_Code/app/clientest.py'])

// process.stdout.on('data', function (data){
// // Do something with the data returned from python script
// 	console.log('yes')
// });

