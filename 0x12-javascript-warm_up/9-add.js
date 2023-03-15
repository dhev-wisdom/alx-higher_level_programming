#!/usr/bin/node
const process = require('process');
let arg1 = process.argv[2];
let arg2 = process.argv[3];
if (isNaN(arg1) === false && isNaN(arg2) === false) {
	arg1 = parseInt(arg1);
	arg2 = parseInt(arg2);
}

function add(a, b) {
	console.log(Number(a) + Number(b));
}

add(arg1, arg2);
