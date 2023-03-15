#!/usr/bin/node
const process = require('process');
const arg1 = parseInt(process.argv[2]);
if (isNaN(arg1) === true) {
	console.log(1);
	return;
}

function factorial(num) {
	if (num < 2) return (num);
  return (num * (factorial(num - 1)))
}
console.log(factorial(arg1));
