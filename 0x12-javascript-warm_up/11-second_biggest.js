#!/usr/bin/node
const process = require('process');
let args = process.argv;
args = args.slice(2);

function find_highest(num) {
  let h = 0;
  for (let i = 0; i < num.length; i++) {
    if (parseInt(num[i]) >= h) h = num[i];
  }
  return (h);
}

let highest = find_highest(args);
let idx_highest = args.indexOf(highest);
args.splice(idx_highest, 1);
let second_highest = find_highest(args);
console.log(second_highest);
