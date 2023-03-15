#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const path1 = process.argv[2];
const path2 = process.argv[3];
const path3 = process.argv[4];
const encoding = 'utf-8';

let content = fs.readFileSync(path1.toString());
content += fs.readFileSync(path2.toString());
fs.writeFile(path3.toString(), content, { encoding },  (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
