#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';
const number = process.argv[2];
request(url, async (error, response, body) => {
  if (!error) {
    const films = JSON.parse(body).results;
    //   console.log(people);
    const keys = Object.keys(films);
    const myFilm = films[keys[number - 1]];
    for (const char of myFilm.characters) {
      await new Promise((resolve) => {
        request(char, (error, response, body) => {
          if (!error) {
            console.log(JSON.parse(body).name);
          }
          resolve();
        });
      });
    }
  }
});
