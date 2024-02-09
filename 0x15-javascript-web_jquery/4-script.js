// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Handle the click event on DIV#toggle_header
    $('#toggle_header').click(function() {
      // Toggle between the classes 'red' and 'green' for the <header> element
      $('header').toggleClass('red green');
    });
  });
