#!/usr/bin/node
const process = require('process');
let arg1 = process.argv[2];
let arg2 = process.argv[3];
let print_ = arg1 + " is " + arg2;
console.log(print_);
