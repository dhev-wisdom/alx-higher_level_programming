#!/usr/bin/node
const process = require('process');
let arg_ = process.argv[2];
if (isNaN(arg_) === false || typeof(arg_) === "number") {
	console.log("My number:", parseInt(arg_));
} else {
	console.log("Not a number");
}
