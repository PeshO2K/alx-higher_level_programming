#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      let filmsData;

      try {
        filmsData = JSON.parse(body).results || JSON.parse(body);
      } catch (parseError) {
        console.error(parseError);
        return;
      }

      const wedgeMovies = filmsData.filter(movie =>
        movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );

      console.log(wedgeMovies.length);
    }
  });
