#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(url, async (err, response, body) => {
  if (err) console.error(err);
  else {
    const body_ = JSON.parse(body);
    const chars = body_.characters;
    for (let i = 0; i < chars.length; i++) {
      const name = await new Promise((resolve, reject) => {
        request(chars[i], (err, res, body) => {
          if (err) reject(err);
          else resolve(JSON.parse(body).name);
        });
      });
      console.log(name);
    }
  }
});
