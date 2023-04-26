#!/usr/bin/node

const fs = require('fs');

const file_ = process.argv[2];
const str_ = process.argv[3];

fs.writeFile(file_, str_, { encoding: 'utf-8' }, (err) => {
  if (err) console.error(err);
});
