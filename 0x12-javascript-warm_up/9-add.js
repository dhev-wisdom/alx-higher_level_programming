#!/usr/bin/node
const process = require('process');
let arg1 = process.argv[2];
let arg2 = process.argv[3];
if (isNaN(arg1) === false && isNaN(arg2) === false) {
	arg1 = parseInt(arg1);
	arg2 = parseInt(arg2);
} else {
	console.log("One of the arguments can't be added");
	return;
}

function add(a, b) {
	console.log(a + b);
}
add(arg1, arg2);
