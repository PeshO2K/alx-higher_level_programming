// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Fetch movie data from the URL
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
      // Extract movie titles
      const movieTitles = data.results.map(movie => movie.title);

      // List movie titles in UL#list_movies
      $('#list_movies').empty(); // Clear existing content
      $.each(movieTitles, function(index, title) {
        $('#list_movies').append('<li>' + title + '</li>');
      });
    });
  });
