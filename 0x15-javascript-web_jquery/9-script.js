// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Fetch translation data from the URL
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
      // Display the translation of "hello" in DIV#hello
      $('#hello').text(data.hello);
    });
  });
