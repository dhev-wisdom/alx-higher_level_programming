#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let url_;
let count;

request(url, (err, response, body) => {
  if (err) console.error(err);
  else {
    const chars = JSON.parse(body).results[0].characters;
    for (let i = 0; i < chars.length; i++) {
      if (chars[i].slice(-3) === '18/') {
        url_ = chars[i];
        break;
      }
    }

    try {
      request(url_, (err, response, body) => {
        if (err) console.error(err);
        else {
          const body__ = JSON.parse(body);
          if (body__.name === 'Wedge Antilles') {
            count = body__.films.length;
            console.log(count);
          }
        }
      });
    } catch (error) {
      console.error(error);
    }
  }
});
