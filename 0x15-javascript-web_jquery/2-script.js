// script.js
$(document).ready(function() {
    // Wait for the DOM to be ready

    // Handle the click event on DIV#red_header
    $('#red_header').click(function() {
      // Update the text color of the <header> element to red
      $('header').css('color', '#FF0000');
    });
  });
