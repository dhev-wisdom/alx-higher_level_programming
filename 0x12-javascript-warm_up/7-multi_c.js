#!/usr/bin/node
const process = require('process');
let arg_ = process.argv[2];
if (isNaN(arg_) === false) {
	arg_ = parseInt(arg_);
} else {
	console.log("Missing number of occurrences");
	return;
}
if (arg_ > 0) {
	for (let i = 0; i < arg_; i++) {
		console.log("C is fun");
	}
}
