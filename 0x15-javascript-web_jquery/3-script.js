// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Handle the click event on DIV#red_header
    $('#red_header').click(function() {
      // Add the class 'red' to the <header> element
      $('header').addClass('red');
    });
  });
