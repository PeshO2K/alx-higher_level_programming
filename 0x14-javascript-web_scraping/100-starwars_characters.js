#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterPromises = movieData.characters.map(characterUrl => fetchCharacterName(characterUrl));

    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(err => console.error(err));
  }
});

function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}
