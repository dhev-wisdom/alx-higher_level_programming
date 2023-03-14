#!/usr/bin/node
const process = require('process');
let arg_ = process.argv[2];
if (!arg_) {
	console.log('No argument');
} else {
	console.log(arg_);
}
