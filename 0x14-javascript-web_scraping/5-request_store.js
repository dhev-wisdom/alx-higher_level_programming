#!/usr/bin/node

const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const filepath = process.argv[3];

req(url, (err, response, body) => {
  if (err) console.error(err);
  else {
    fs.writeFile(filepath, body, { encoding: 'utf-8' }, (err) => {
      if (err) console.error(err);
    });
  }
});
