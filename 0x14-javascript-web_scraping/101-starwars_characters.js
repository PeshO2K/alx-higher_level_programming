#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    fetchAndPrintCharacterNames(characterUrls)
      .then(() => {
        // All character names have been printed
      })
      .catch(err => console.error(err));
  }
});

function fetchAndPrintCharacterNames (characterUrls) {
  return new Promise((resolve, reject) => {
    let remainingRequests = characterUrls.length;

    characterUrls.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);

          remainingRequests--;
          if (remainingRequests === 0) {
            resolve();
          }
        }
      });
    });
  });
}
