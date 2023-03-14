#!/usr/bin/node
const process = require('process');
let arg_ = process.argv[2];
if (isNaN(arg_) === false) {
	arg_ = parseInt(arg_);
} else {
	console.log("Missing size");
	return;
}
if (arg_ > 0) {
	for (let i = 0; i < arg_; i++) {
		let arr_ = []
		for (let j = 0; j < arg_; j++) {
			arr_.push("X");
		}
		console.log(arr_.join(''));
	}
}
