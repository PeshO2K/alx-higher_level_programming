#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    let moviesWithWedgeAntilles = 0;

    // Loop through each film and check if Wedge Antilles is present
    for (const film of filmsData) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        moviesWithWedgeAntilles++;
      }
    }

    console.log(moviesWithWedgeAntilles);
  }
});
