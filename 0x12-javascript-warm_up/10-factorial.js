#!/usr/bin/node
const process = require('process');
const arg1 = parseInt(process.argv[2]);
if (isNaN(arg1) === true) {
	console.log(1);
	return;
}

function factorial(arg1) {
	if (arg1 >= 2) {
		return (arg1 * (factorial(arg1 - 1)));
	} else if (arg1 == 0) {
		return (0);
	} else {
		return (1);
	}
}
console.log(factorial(arg1));
