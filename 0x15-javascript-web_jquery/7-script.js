// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Fetch character data from the URL
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
      // Display the character name in DIV#character
      $('#character').text(data.name);
    });
  });
