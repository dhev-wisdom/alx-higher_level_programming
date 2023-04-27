#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(url, (err, response, body) => {
  if (err) console.error(err);
  else {
    const body_ = JSON.parse(body);
    const chars = body_.characters;
    for (let i = 0; i < chars.length; i++) {
      request(chars[i], (err, response, body) => {
        if (err) console.error(err);
        const body__ = JSON.parse(body);
        console.log(body__.name);
      });
    }
  }
});
