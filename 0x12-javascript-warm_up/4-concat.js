#!/usr/bin/node
const process = require('process');
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const print_ = arg1 + " is " + arg2;
console.log(print_);
