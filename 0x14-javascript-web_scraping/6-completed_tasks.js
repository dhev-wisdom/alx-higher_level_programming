#!/usr/bin/node

const r = require('request');
const url = process.argv[2];

const ansDict = {};
r(url, (err, response, body) => {
  if (err) console.error(err);
  else {
    const body_ = JSON.parse(body);
    let a = 1;
    for (let i = 0; i < body_.length; i++) {
      if (body_[i].completed === true) {
        ansDict[a] = body_[i].id;
        a++;
      }
    }
    console.log(ansDict);
  }
});
