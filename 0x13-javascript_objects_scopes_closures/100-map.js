#!/usr/bin/node
const list_map = require('./100-data').list;

const new_list = list_map.map((num, idx) => (num * idx));

console.log(list_map);
console.log(new_list);
